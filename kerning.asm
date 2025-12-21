.ps2

.open "extracted/SLPM_663.60", 0x0
.org 0x215b00
.incbin "scripts/misc/kerning.bin"
.close

.open "extracted/SLPM_663.60", 0xfff80

.org 0x14e8f8
beq zero,zero,0x0014E908

.org 0x14e8a8
daddiu a3,zero,0x0180

.org 0x14e8cc
nop

.org 0x14e798
lb v0, 0x0(s3)
li a0, 0x315A80
addu a0, a0, v0
lb v0, 0x0(a0)
addu s2, s2, v0

.close
