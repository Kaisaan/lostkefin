.ps2

.open "translated/SLPM_663.60", 0xfff80

WORD_SPACING equ 0xd
LINE_SPACING equ 0x18

.org 0x314000
kerning_table:
  .incbin "scripts/misc/kerning.bin"
ascii_kerning_table:
  .incbin "scripts/misc/ascii_kerning.bin"

// Increments Z for each glyph so they properly
// layer on top of one another
increment_z:
  addiu   sp, sp, -0x20
  sw      ra, 0x00(sp)
  sw      s0, 0x04(sp)
  sw      s1, 0x08(sp)
  sw      s2, 0x0C(sp)

dsra32 a3,a3,0x00
addiu a3,a3,0x1
dsll32 a3,a3,0x00

lw      ra, 0x00(sp)
lw      s0, 0x04(sp)
lw      s1, 0x08(sp)
lw      s2, 0x0C(sp)
jr      ra
addiu   sp, sp, 0x20 

.include "asm/text_box_size.asm"

.include "asm/calculate_str_width.asm"


// start kerning
.org 0x14e8f8
beq zero,zero,0x14E908

.org 0x14e8a8
daddiu a3,zero,0x0180

.org 0x14e8cc
nop

.org 0x14e798
lb v0, 0x0(s3)
li a0, kerning_table
addu a0, a0, v0
lb v0, 0x0(a0)
addu s2, s2, v0
// end kerning

// If glyph is ASCII, render at 0x18 width
.org 0x14e664
addiu fp,zero,0x18
beq zero,zero,0x0014E6A8
andi a0,v1,0xFFFF

.org 0x19dd28
jal text_box_size

.org 0x19de88
jal text_box_size

.org 0x19b468
jal calculate_str_width

.org 0x19b690
jal calculate_str_width

.org 0x19b768
jal calculate_str_width

.org 0x19bd54
jal calculate_str_width

.org 0x14e1d0
jal increment_z
and t1,t1,a2

.org 0x19c3fc
addiu a1,zero,WORD_SPACING

.org 0x14c44c
addiu v1,zero,WORD_SPACING

.org 0x14c894
addiu v0,zero,WORD_SPACING

.org 0x14c6a8
addiu v0,zero,WORD_SPACING

.org 0x19dcf4
addiu a3,zero,WORD_SPACING

.org 0x19c404
addiu a2,zero,LINE_SPACING

// Swap SJIS '+' to ASCII
.org 0x3636f0
.byte 0x20
.byte 0x2b

// Swap SJIS '+' to ASCII
.org 0x363570
.byte 0x20
.byte 0x2b


// Swap SJIS '+' to ASCII
.org 0x36dfb8
.byte 0x20
.byte 0x2b

// Item screen layering bugfix
.org 0x1cb0b4
addiu t0,zero,0x2E7

.org 0x1c9db8
addiu t0,zero,0x2E7

.close