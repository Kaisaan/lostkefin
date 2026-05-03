# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "google-api-python-client",
#     "google-auth",
#     "pillow",
# ]
# ///
import argparse
import re
import subprocess
import sys
import shutil
from pathlib import Path

from isotool import PAD_NONE, rebuild_iso
from tasks.compile import kscript_to_bin
from tasks.from_csv import from_csv
from tasks.from_sheets import from_sheets
from tasks.pack import pack
from tasks.update_graphic import insert_all_graphics
from tasks.patch_font import patch_font_from_atlas

STAGES = ["00", "10", "20", "30", "40", "50", "60", "70", "80", "90", "a0", "b0"]


def run(cmd, **kwargs):
    print(f"Running: {' '.join(str(arg) for arg in cmd)}")
    try:
        subprocess.run(cmd, check=True, **kwargs)
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {' '.join(str(arg) for arg in cmd)}")
        sys.exit(e.returncode)


def main(sheets: bool = False):
    print("Patching scripts and generating strings.asm...")
    if sheets:
        print("Pulling latest translations from Google Sheets...")
        from_sheets("decompiled")
    else:
        print("Updating using CSV files")
        from_csv(
            csv_dir="csv",
            kscript_dir="decompiled",
        )
    print("Done!")

    print("Compiling scripts...")

    """
    # Insert OpenShop command at line 1708 in stage40.kscript
    with open("decompiled/stage40.kscript", "r") as f:
        lines = f.readlines()
    lines.insert(1707, "  OpenShop\targ:0401\n")
    with open("decompiled/stage40.kscript", "w") as f:
        f.writelines(lines)
    """

    for stage in STAGES:
        src = f"decompiled/stage{stage}.kscript"
        dst = f"DATA/script/stage{stage}.bin"
        kscript_to_bin(src, dst)
    print("Done!")

    print("Inserting graphics...")
    insert_all_graphics()
    print("Done!")

    print("Applying first round of SLPM patches")

    # Total hack: we use notice: directives in patch.asm in order to keep track of pointers
    # as we are writing them.
    out = open("asm/credits_ptrs.asm", "w")
    pattern = re.compile(r"notice:\s*(L[0-9A-Fa-f]+)=([0-9A-Fa-f]+)")
    proc = subprocess.Popen(
        ["/usr/local/bin/armips", Path("asm/patch.asm")],
        stdout=subprocess.PIPE,
        text=True,
        shell=False,
    )

    seen = set()
    for line in proc.stdout:
        match = pattern.search(line)
        if match:
            label, addr = match.groups()

            if label in seen:
                continue

            out.write(f"{label} equ 0x{addr}\n")
            seen.add(label)
        else:
            print(line)

    proc.wait()
    out.close()
    print("Done!")

    print("Patching font...")
    patch_font_from_atlas("font_atlas.png")
    print("Done!")

    # This needs to be done after patched font because I
    # reclaim some of the unused font space :)
    print("Applying second round of SLPM patches")
    run(["armips", Path("asm/kerning.asm")])
    print("Done!")

    print("Repacking DATA.BIN")
    pack("DATA.BIN")

    shutil.copyfile(
        Path("scripts/data/stein.pss"),
        Path("translated/DUMMY.BIN"),
    )

    print("Patching ISO. Please wait.")
    rebuild_iso(
        Path("lostkefin.iso"),
        Path("filelist.txt"),
        Path("translated"),
        Path("Ys V - Lost Kefin, Kingdom of Sand [English Patched].iso"),
        PAD_NONE,
    )
    print(
        "Patched ISO saved to Ys V - Lost Kefin, Kingdom of Sand [English Patched].iso"
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Patch ISO with translations")
    parser.add_argument(
        "--sheets",
        action="store_true",
        help="Pull latest translations from Google Sheets. If unset, uses local CSV files",
    )
    args = parser.parse_args()
    main(args.sheets)
