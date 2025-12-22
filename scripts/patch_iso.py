# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "google-api-python-client",
#     "google-auth",
#     "pillow",
# ]
# ///
import argparse
import subprocess
import sys
from pathlib import Path

from isotool import PAD_NONE, rebuild_iso
from tasks.compile import kscript_to_bin
from tasks.from_csv import from_csv
from tasks.from_sheets import from_sheets
from tasks.pack import pack
from tasks.update_graphic import insert_all_graphics
from tasks.patch_font import patch_font

STAGES = ["00", "10", "20", "30", "40", "50", "60", "70", "80", "90", "a0", "b0"]


def run(cmd, **kwargs):
    print(f"Running: {' '.join(cmd)}")
    try:
        subprocess.run(cmd, check=True, **kwargs)
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {' '.join(cmd)}")
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

    print("Patching SLPM")
    run(["armips", "patch.asm"])
    print("Done!")

    print("Compiling scripts...")
    for stage in STAGES:
        src = f"decompiled/stage{stage}.kscript"
        dst = f"DATA/script/stage{stage}.bin"
        kscript_to_bin(src, dst)
    print("Done!")

    print("Inserting graphics...")
    insert_all_graphics()
    print("Done!")

    print("Patching font...")
    patch_font()
    print("Done!")

    print("Repacking DATA.BIN")
    pack("DATA.BIN")

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
