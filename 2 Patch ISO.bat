@echo off
armips patch.asm
echo Patching ISO. Please wait.
perl scripts\abcde\abcde.pl --multi-table-files -cm abcde::Atlas "translated\DATA.BIN" "scripts\translated.txt"
isotool.py -m insert --iso lostkefin.iso -o "Ys V - Lost Kefin, Kingdom of Sand [English Patched].iso" --filelist filelist.txt --files translated
pause