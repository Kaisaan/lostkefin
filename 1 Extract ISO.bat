@echo off
echo Copy the original .iso next to this batch file and rename it to lostkefin.iso
echo Extracting iso...
isotool.py -m extract --iso lostkefin.iso --filelist filelist.txt --files extracted
xcopy extracted translated /E /I /Y
echo Done!
echo Unpacking DATA.BIN...
unpack.py DATA.BIN
echo Decompiling script files into .kscript files...
if not exist decompiled mkdir decompiled
kscript\decompile.py DATA\script\stage00.bin decompiled\stage00.kscript
kscript\decompile.py DATA\script\stage10.bin decompiled\stage10.kscript
kscript\decompile.py DATA\script\stage20.bin decompiled\stage20.kscript
kscript\decompile.py DATA\script\stage30.bin decompiled\stage30.kscript
kscript\decompile.py DATA\script\stage40.bin decompiled\stage40.kscript
kscript\decompile.py DATA\script\stage50.bin decompiled\stage50.kscript
kscript\decompile.py DATA\script\stage60.bin decompiled\stage60.kscript
kscript\decompile.py DATA\script\stage70.bin decompiled\stage70.kscript
kscript\decompile.py DATA\script\stage80.bin decompiled\stage80.kscript
kscript\decompile.py DATA\script\stage90.bin decompiled\stage90.kscript
kscript\decompile.py DATA\script\stagea0.bin decompiled\stagea0.kscript
kscript\decompile.py DATA\script\stageb0.bin decompiled\stageb0.kscript
echo Done!
echo Extracting text from .kscript files and dumping to CSV...
if not exist csv mkdir csv
kscript\to_csv.py decompiled\stage00.kscript csv\stage00.csv
kscript\to_csv.py decompiled\stage10.kscript csv\stage10.csv
kscript\to_csv.py decompiled\stage20.kscript csv\stage20.csv
kscript\to_csv.py decompiled\stage30.kscript csv\stage30.csv
kscript\to_csv.py decompiled\stage40.kscript csv\stage40.csv
kscript\to_csv.py decompiled\stage50.kscript csv\stage50.csv
kscript\to_csv.py decompiled\stage60.kscript csv\stage60.csv
kscript\to_csv.py decompiled\stage70.kscript csv\stage70.csv
kscript\to_csv.py decompiled\stage80.kscript csv\stage80.csv
kscript\to_csv.py decompiled\stage90.kscript csv\stage90.csv
kscript\to_csv.py decompiled\stagea0.kscript csv\stagea0.csv
kscript\to_csv.py decompiled\stageb0.kscript csv\stageb0.csv
echo Done!
pause