import os
import sys
import shutil
import subprocess
from pathlib import Path
from isotool import dump_iso
from tasks.to_csv import to_csv
from tasks.decompile import bin_to_kscript
from tasks.unpack import unpack

STAGES = ["00", "10", "20", "30", "40", "50", "60", "70", "80", "90", "a0", "b0"]


def main():
    print("Copy the original .iso next to this script and rename it to lostkefin.iso")

    if os.path.exists("extracted"):
        shutil.rmtree("extracted")
    print("Extracting iso...")
    dump_iso(Path("lostkefin.iso"), Path("filelist.txt"), Path("extracted"), True)

    # Copy extracted to translated
    if os.path.exists("translated"):
        shutil.rmtree("translated")
    shutil.copytree("extracted", "translated")
    print("Done!")

    print("Unpacking DATA.BIN...")
    unpack("DATA.BIN")

    print("Decompiling script files into .kscript files...")
    if os.path.exists("decompiled"):
        shutil.rmtree("decompiled")
    os.makedirs("decompiled", exist_ok=True)
    for stage in STAGES:
        src = f"DATA/script/stage{stage}.bin"
        dst = f"decompiled/stage{stage}.kscript"
        bin_to_kscript(src, dst)
    print("Done!")

    print("Extracting text from .kscript files and dumping to CSV...")
    if os.path.exists("csv"):
        shutil.rmtree("csv")
    os.makedirs("csv", exist_ok=True)
    for stage in STAGES:
        src = f"decompiled/stage{stage}.kscript"
        dst = f"csv/stage{stage}.csv"
        to_csv(src, dst)
    print("Done!")


if __name__ == "__main__":
    main()
