armips patch.asm
copy DATA.BIN translated/DATA.BIN
copy "SLPM_663.60" "translated/SLPM_663.60"
isotool.py -m insert --iso lostkefin.iso -o english.iso --filelist filelist.txt --files translated
@pause