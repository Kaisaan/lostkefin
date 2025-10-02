.erroronwarning on
.ps2

.loadtable "kefin.tbl", "UTF8"

.open "extracted/SLPM_663.60", "translated/SLPM_663.60", 0x0

.include "code.asm"

// Fix halfwidth characters not updating textbox size correctly
.orga 0x0004CF38
addiu	t7, t7, 0x0A

.orga 0x0004CF44
addiu	a0, a0, 0x01

.close