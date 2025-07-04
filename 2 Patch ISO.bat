@echo off
armips patch.asm
echo Patching scripts...
kscript\from_csv.py csv\stage00.csv decompiled\stage00.kscript temp.kscript
move temp.kscript decompiled\stage00.kscript
kscript\from_csv.py csv\stage10.csv decompiled\stage10.kscript temp.kscript
move temp.kscript decompiled\stage10.kscript
kscript\from_csv.py csv\stage20.csv decompiled\stage20.kscript temp.kscript
move temp.kscript decompiled\stage20.kscript
kscript\from_csv.py csv\stage30.csv decompiled\stage30.kscript temp.kscript
move temp.kscript decompiled\stage30.kscript
kscript\from_csv.py csv\stage40.csv decompiled\stage40.kscript temp.kscript
move temp.kscript decompiled\stage40.kscript
kscript\from_csv.py csv\stage50.csv decompiled\stage50.kscript temp.kscript
move temp.kscript decompiled\stage50.kscript
kscript\from_csv.py csv\stage60.csv decompiled\stage60.kscript temp.kscript
move temp.kscript decompiled\stage60.kscript
kscript\from_csv.py csv\stage70.csv decompiled\stage70.kscript temp.kscript
move temp.kscript decompiled\stage70.kscript
kscript\from_csv.py csv\stage80.csv decompiled\stage80.kscript temp.kscript
move temp.kscript decompiled\stage80.kscript
kscript\from_csv.py csv\stage90.csv decompiled\stage90.kscript temp.kscript
move temp.kscript decompiled\stage90.kscript
kscript\from_csv.py csv\stagea0.csv decompiled\stagea0.kscript temp.kscript
move temp.kscript decompiled\stagea0.kscript
kscript\from_csv.py csv\stageb0.csv decompiled\stageb0.kscript temp.kscript
move temp.kscript decompiled\stageb0.kscript
echo Done!
echo Compiling scripts...
kscript\compile.py decompiled\stage00.kscript DATA\script\stage00.bin
kscript\compile.py decompiled\stage10.kscript DATA\script\stage10.bin
kscript\compile.py decompiled\stage20.kscript DATA\script\stage20.bin
kscript\compile.py decompiled\stage30.kscript DATA\script\stage30.bin
kscript\compile.py decompiled\stage40.kscript DATA\script\stage40.bin
kscript\compile.py decompiled\stage50.kscript DATA\script\stage50.bin
kscript\compile.py decompiled\stage60.kscript DATA\script\stage60.bin
kscript\compile.py decompiled\stage70.kscript DATA\script\stage70.bin
kscript\compile.py decompiled\stage80.kscript DATA\script\stage80.bin
kscript\compile.py decompiled\stage90.kscript DATA\script\stage90.bin
kscript\compile.py decompiled\stagea0.kscript DATA\script\stagea0.bin
kscript\compile.py decompiled\stageb0.kscript DATA\script\stageb0.bin
echo Done!
echo Repacking DATA.BIN
pack.py DATA.BIN
echo Patching ISO. Please wait.
isotool.py -m insert --iso lostkefin.iso -o "Ys V - Lost Kefin, Kingdom of Sand [English Patched].iso" --filelist filelist.txt --files translated
pause