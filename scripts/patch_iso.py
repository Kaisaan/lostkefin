# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "google-api-python-client",
#     "google-auth",
# ]
# ///
from pathlib import Path
import sys
import subprocess
from tasks.from_sheets import from_sheets
from tasks.compile import kscript_to_bin
from tasks.pack import pack
from isotool import rebuild_iso, PAD_NONE

STAGES = ["00", "10", "20", "30", "40", "50", "60", "70", "80", "90", "a0", "b0"]


def run(cmd, **kwargs):
    print(f"Running: {' '.join(cmd)}")
    try:
        subprocess.run(cmd, check=True, **kwargs)
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {' '.join(cmd)}")
        sys.exit(e.returncode)


def main():
    run(["armips", "patch.asm"])
    print("Patching scripts...")
    from_sheets("decompiled")
    print("Done!")

    print("Compiling scripts...")
    for stage in STAGES:
        src = f"decompiled/stage{stage}.kscript"
        dst = f"DATA/script/stage{stage}.bin"
        kscript_to_bin(src, dst)
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


if __name__ == "__main__":
    main()
