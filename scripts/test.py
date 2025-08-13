from isotool import PAD_NONE, rebuild_iso
from pathlib import Path
rebuild_iso(
    Path("lostkefin.iso"),
    Path("filelist.txt"),
    Path("translated"),
    Path("Ys V - Lost Kefin, Kingdom of Sand [English Patched].iso"),
    PAD_NONE,
)
