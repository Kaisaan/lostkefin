.erroronwarning on
.ps2

.loadtable "kefin.tbl", "UTF8"

.open "extracted/SLPM_663.60", "translated/SLPM_663.60", 0x0

.include "asm/code.asm"

// Patch treasure chest to be interactable
.org 0x140384
li v1, 0x5

.org 0x140354
li v1, 0x5

.org 0x6A810
addiu v1,zero,0x7


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

// Fix pointer alignment on gallery
.orga 0x130794
addiu a2,zero,0x2f

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
addiu a2,zero,0x5A

// Shift inventory item desc left
.orga 0xA1208
addiu v1,v0,0x55

// Same as above

.orga 0xA11D0
addiu v1,v0,0x55

// Shift shop screen item desc left and down
.orga 0xA8F08
addiu a1,zero,0x66
addiu a2,zero,0x14A

// Same as above, but for some other shops
.orga 0xA4444
addiu a1,zero,0x66
addiu a2,zero,0x14A

// Same as above, for sell screen
.orga 0xA7950
addiu a1,zero,0x66
addiu a2,zero,0x14A

// Shift "acquired" text slightly left and up
.orga 0xA0A44
addiu a1,zero,0xD5
addiu a2,zero,0x46

// Extend the two triangles that make up the grey rectangle background for Gallery names
.orga 0x130618
addiu a3,zero,0x24B

.orga 0x130630
addiu a3,zero,0x24B

//
// Normal textbox quad select tweaks
//

// Decrease text indent
.orga 0x9d270
addiu v1,v0,0x2

// Decrease pointer indent
.orga 0x9d394
addiu a2,s6,0x16

// Fix buffer size calculator to round up when calculating
// quadwords
.orga 0x3EDF8
mult v0,a3,a1
addiu v0,v0,0x1f 
jr ra
sra v0,v0,0x05
default_case:
jr ra
daddu v0,zero,zero

.orga 0x3ED9C
beq v0,zero,default_case

// The game does a wacky thing where it loads in "%03d" but then tweaks
// the second byte as needed to make it %05d, %03d, etc. 
// I switched the format string to %d so I need to patch to stop that 
// tweak from happening

.orga 0xA41F8
addiu v0,zero,0x64

.orga 0xA4B68
addiu v1,zero,0x64

.orga 0xA4D88
addiu v1,zero,0x64

.orga 0xA56F8
addiu v0,zero,0x64

.orga 0xA5700
addiu v0,zero,0x64

.orga 0xA57C8
addiu v0,zero,0x64

.orga 0xA58B0
addiu v0,zero,0x64

.orga 0xA5980
addiu v0,zero,0x64

.orga 0xA5A8C
addiu v0,zero,0x64

.orga 0xA5B1C
addiu v0,zero,0x64

.orga 0xA5B20
addiu v0,zero,0x64



.close