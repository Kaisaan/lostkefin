@echo off
echo Copy the original .iso next to this batch file and rename it to lostkefin.iso
echo Extracting iso...
isotool.py -m extract --iso lostkefin.iso --filelist filelist --files extracted
echo Done!
::echo Dumping the (raw) script from DATA.BIN to multiple files...
::perl scripts\abcde\abcde.pl -cm abcde::Cartographer "extracted\DATA.BIN" datacommands.txt "scripts\dump" -m
::echo Done!
::echo Dumping the (raw) script from DATA.BIN to a single text file...
::perl scripts\abcde\abcde.pl  -cm abcde::Cartographer "extracted\DATA.BIN" datacommands.txt "scripts\dump" -s
::echo Dumping the script (with pointers) from DATA.BIN to multiple text files...
::perl scripts\abcde\abcde.pl --multi-table-files -cm abcde::Cartographer "extracted\DATA.BIN" scriptcommands.txt "scripts\dump" -m
::echo Done!
echo Dumping the script (with pointers) from DATA.BIN to a single text file...
perl scripts\abcde\abcde.pl --multi-table-files -cm abcde::Cartographer "extracted\DATA.BIN" scriptcommands.txt "scripts\dump" -s
echo Done!
copy /Y scripts\dump.txt scripts\translated.txt
echo Done!
pause