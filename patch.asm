.erroronwarning off
.ps2

.loadtable "kefinold.tbl", "SJIS"

.open "extracted/SLPM_663.60", "SLPM_663.60", 0x0

.orga 0x0025FD45
.strn "KaisaanTest", 0x81, 0xA5

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