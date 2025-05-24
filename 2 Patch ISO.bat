@echo off
xcopy extracted translated /E /I /Y
armips patch.asm
echo Patching ISO. Please wait.
perl scripts\abcde\abcde.pl --multi-table-files -cm abcde::Atlas "translated\DATA.BIN" "scripts\translated.txt"
armips patch.asm
isotool.py -m insert --iso lostkefin.iso -o "Ys V - Lost Kefin, Kingdom of Sand [English Patched].iso" --filelist filelist.txt --files translated
pause