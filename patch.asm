.erroronwarning on
.ps2

.loadtable "kefin.tbl", "SJIS"

.open "extracted/SLPM_663.60", "translated/SLPM_663.60", 0x0

// Fix halfwidth characters not updating textbox size correctly
.orga 0x0004CE40	; 43 50 07 00	sra		t2,a3,0x1
.db 0x03			; change 0x1 to 0x0

.orga 0x0025FD45
.strn "KaisaanTest"

.orga 0x0025FE70
.strn "Ys 3 Data found"

.orga 0x0025FEB0
.strn "No Ys 3 Data"

.orga 0x00260B70
.strn "Ys 3 Data search"

.orga 0x2638D8
.strn "Adol", 0x00, 0x00

.orga 0x2638E0
.strn "Dogi"

.close

.open "extracted/DATA.BIN", "translated/DATA.BIN", 0x0

.orga 0x3B9A880
.db 0xFF

.close