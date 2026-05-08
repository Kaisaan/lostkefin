.ps2

.loadtable "kefin.tbl", "UTF8"
.open "translated/SLPM_663.60", 0xfff80

WORD_SPACING equ 0xd
LINE_SPACING equ 0x18

.org 0x12e9a0
strcat:

.org 0x24f480
credits:

.org 0x312000
kerning_table:
  .incbin "scripts/data/kerning.bin"
ascii_kerning_table:
  .incbin "scripts/data/ascii_kerning.bin"

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

.include "asm/credits.asm"

.include "asm/strcat_wrapper.asm"

.notice "finished writing to reclaimed font area at offset: 0x" + tohex(orga())
.notice "If this is more than 0x215d00, THATS NOT GOOD"

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

// This used to call strlen to calculate centering logic
// Doesn't work with a VWF so we now use calculate_str_width
.org 0x24f270
jal calculate_str_width
addiu s2,v0,0x110
li v1, 0x280
subu a0, v1, v0
srl v0, a0, 1
nop
nop
nop


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

// Item screen layering bugfix
.org 0x1cb0b4
addiu t0,zero,0x2E7

.org 0x1c9db8
addiu t0,zero,0x2E7

// Move "dim screen" effect Z axis up slightly to make room for text
.org 0x0018ceb0
addiu a2,zero,0x468

// Post-credits layering bugfix
.org 0x24ef24
addiu a2,zero,0x362

// Textbox layering bugfixes (move the book up)
.org 0x19dbe8
addiu v1,zero,0x430

.org 0x19cbb8
addiu t8,zero,0x430

.org 0x19c810
addiu a0,zero,0x42C

.org 0x24ff5c
lui a0, hi(start_credits)
jal credits
addiu a0, a0, lo(start_credits)

.org 0x24f7c0
li v0, graphic_table
sll v1,s1,0x1
addu v0,v0,v1

.org 0x24f8a0
li v0, movie_table
sll v1,s1,0x2
addu v0,v0,v1


// Use strcat_wrapper to add a space after "+1", "+2", etc
.org 0x1a49f0
jal strcat_wrapper

.org 0x1a0df0
jal strcat_wrapper

.close
