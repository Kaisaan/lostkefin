armips patch.asm
copy "SLPM_663.60" "translated/SLPM_663.60"
perl "scripts/abcde/abcde.pl" -cm abcde::Atlas "translated/DATA.BIN" "scripts/translated.txt"
isotool.py -m insert --iso lostkefin.iso -o english.iso --filelist filelist.txt --files translated
@pause