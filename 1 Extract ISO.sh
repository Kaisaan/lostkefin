#!/bin/bash
set -e

echo "Copy the original .iso next to this script and rename it to lostkefin.iso"
echo "Extracting iso..."
python3 isotool.py -m extract --iso lostkefin.iso --filelist filelist.txt --files extracted
cp -R extracted translated

echo "Done!"

echo "Unpacking DATA.BIN..."
python3 extract.py

echo "Decompiling script files into .kscript files..."
mkdir -p decompiled
python3 kscript/decompile.py DATA/stage00.bin decompiled/stage00.kscript
python3 kscript/decompile.py DATA/stage10.bin decompiled/stage10.kscript
python3 kscript/decompile.py DATA/stage20.bin decompiled/stage20.kscript
python3 kscript/decompile.py DATA/stage30.bin decompiled/stage30.kscript
python3 kscript/decompile.py DATA/stage40.bin decompiled/stage40.kscript
python3 kscript/decompile.py DATA/stage50.bin decompiled/stage50.kscript
python3 kscript/decompile.py DATA/stage60.bin decompiled/stage60.kscript
python3 kscript/decompile.py DATA/stage70.bin decompiled/stage70.kscript
python3 kscript/decompile.py DATA/stage80.bin decompiled/stage80.kscript
python3 kscript/decompile.py DATA/stage90.bin decompiled/stage90.kscript
python3 kscript/decompile.py DATA/stagea0.bin decompiled/stagea0.kscript
python3 kscript/decompile.py DATA/stageb0.bin decompiled/stageb0.kscript
echo "Done!"

echo "Extracting text from .kscript files and dumping to CSV..."
mkdir -p csv
python3 kscript/to_csv.py decompiled/stage00.kscript csv/stage00.csv
python3 kscript/to_csv.py decompiled/stage10.kscript csv/stage10.csv
python3 kscript/to_csv.py decompiled/stage20.kscript csv/stage20.csv
python3 kscript/to_csv.py decompiled/stage30.kscript csv/stage30.csv
python3 kscript/to_csv.py decompiled/stage40.kscript csv/stage40.csv
python3 kscript/to_csv.py decompiled/stage50.kscript csv/stage50.csv
python3 kscript/to_csv.py decompiled/stage60.kscript csv/stage60.csv
python3 kscript/to_csv.py decompiled/stage70.kscript csv/stage70.csv
python3 kscript/to_csv.py decompiled/stage80.kscript csv/stage80.csv
python3 kscript/to_csv.py decompiled/stage90.kscript csv/stage90.csv
python3 kscript/to_csv.py decompiled/stagea0.kscript csv/stagea0.csv
python3 kscript/to_csv.py decompiled/stageb0.kscript csv/stageb0.csv
echo "Done!" 