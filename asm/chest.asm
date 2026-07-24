.erroronwarning on
.ps2

.open "translated/SLPM_663.60", 0x0

// Patch treasure chest to be interactable
.org 0x140384
li v1, 0x5

.org 0x140354
li v1, 0x5

.org 0x6A810
addiu v1,zero,0x7

.close
