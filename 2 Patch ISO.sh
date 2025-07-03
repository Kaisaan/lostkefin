#!/bin/bash
set -e

armips patch.asm
echo "Patching scripts..."

python3 kscript/from_csv.py csv/stage00.csv decompiled/stage00.kscript temp.kscript && mv temp.kscript decompiled/stage00.kscript
python3 kscript/from_csv.py csv/stage10.csv decompiled/stage10.kscript temp.kscript && mv temp.kscript decompiled/stage10.kscript
python3 kscript/from_csv.py csv/stage20.csv decompiled/stage20.kscript temp.kscript && mv temp.kscript decompiled/stage20.kscript
python3 kscript/from_csv.py csv/stage30.csv decompiled/stage30.kscript temp.kscript && mv temp.kscript decompiled/stage30.kscript
python3 kscript/from_csv.py csv/stage40.csv decompiled/stage40.kscript temp.kscript && mv temp.kscript decompiled/stage40.kscript
python3 kscript/from_csv.py csv/stage50.csv decompiled/stage50.kscript temp.kscript && mv temp.kscript decompiled/stage50.kscript
python3 kscript/from_csv.py csv/stage60.csv decompiled/stage60.kscript temp.kscript && mv temp.kscript decompiled/stage60.kscript
python3 kscript/from_csv.py csv/stage70.csv decompiled/stage70.kscript temp.kscript && mv temp.kscript decompiled/stage70.kscript
python3 kscript/from_csv.py csv/stage80.csv decompiled/stage80.kscript temp.kscript && mv temp.kscript decompiled/stage80.kscript
python3 kscript/from_csv.py csv/stage90.csv decompiled/stage90.kscript temp.kscript && mv temp.kscript decompiled/stage90.kscript
python3 kscript/from_csv.py csv/stagea0.csv decompiled/stagea0.kscript temp.kscript && mv temp.kscript decompiled/stagea0.kscript
python3 kscript/from_csv.py csv/stageb0.csv decompiled/stageb0.kscript temp.kscript && mv temp.kscript decompiled/stageb0.kscript

echo "Done!"
echo "Compiling scripts..."

echo "1"
python3 kscript/compile.py decompiled/stage00.kscript DATA/stage00.bin
echo "2"
python3 kscript/compile.py decompiled/stage10.kscript DATA/stage10.bin
echo "3"
python3 kscript/compile.py decompiled/stage20.kscript DATA/stage20.bin
echo "4"
python3 kscript/compile.py decompiled/stage30.kscript DATA/stage30.bin
echo "5"
python3 kscript/compile.py decompiled/stage40.kscript DATA/stage40.bin
echo "6"
python3 kscript/compile.py decompiled/stage50.kscript DATA/stage50.bin
echo "7"
python3 kscript/compile.py decompiled/stage60.kscript DATA/stage60.bin
echo "8"
python3 kscript/compile.py decompiled/stage70.kscript DATA/stage70.bin
echo "9"
python3 kscript/compile.py decompiled/stage80.kscript DATA/stage80.bin
echo "10"
python3 kscript/compile.py decompiled/stage90.kscript DATA/stage90.bin
python3 kscript/compile.py decompiled/stagea0.kscript DATA/stagea0.bin
python3 kscript/compile.py decompiled/stageb0.kscript DATA/stageb0.bin

echo "Done!"
echo "Patching ISO. Please wait."
python3 isotool.py -m insert --iso lostkefin.iso -o "Ys V - Lost Kefin, Kingdom of Sand [English Patched].iso" --filelist filelist.txt --files translated 