.erroronwarning on
.ps2

.loadtable "kefin.tbl", "UTF8"

.open "extracted/SLPM_663.60", "translated/SLPM_663.60", 0x0

.include "code.asm"

// Fix string-centering code incorrectly handling ASCII
.orga 0x4d34c
addiu a0,a0,0x1
addiu a0,a0,0x1


// Fix halfwidth characters not updating textbox size correctly
.orga 0x0004CF38
addiu t7, t7, 0x0A

.orga 0x0004CF44
addiu a0, a0, 0x01

// Patch treasure chest to be interactable
.org 0x000140384
li v1, 0x5

.org 0x000140354
li v1, 0x5

// Fix ASCII characters not printing in some cases
.orga 0x0009B468
addiu v0,zero,0x40
beq v1,v0,0x0009B688
addiu v0,zero,0x23
bne v1,v0,0x0009B660
addu v0,s1,s3
nop
nop
nop
nop

.orga 0x0009B660
sb v1,0x0(v0)
lw v1,0x8(s2)
addu v0,s1,s3
addu v1,v1,s4
lb v1,0x0(v1)
beq zero,zero,0x0009B4C0
sb v1,0x0(v0)
nop
nop

.orga 0x0009B4C0
addiu s4,s4,0x1
beq zero,zero,0x0009B430
addiu s3,s3,0x1

// Change offset of highlights

// "Perform a Quick Save?" and "Return to the title screen?"
.orga 0x0009B744 // "Yes"
addiu a2,v0, -0x1a

.orga 0x0009B81C // "No"
addiu a2,v0, -0x1e

// "Load data?"
.orga 0x7D10C // "Yes"
addiu a2, zero, 0x3

.orga 0x7D18C // "No"
addiu a2,zero,0x63

// Shift inventory item desc left and down
.orga 0xA1208
addiu v1,v0,0x55

.orga 0xA122C
addiu v0,v0,0xb

// Shift shop screen item desc left and down
.orga 0xA8F08
addiu a1,zero,0x66
addiu a2,zero,0x14A

// Same as above, but for some other shops
.orga 0xA4444
addiu a1,zero,0x66
addiu a2,zero,0x14A

.close
