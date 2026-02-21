// strcat wrapper
// Wraps a call to strcat and makes a second call to append a space
// Used to add a space to the "+1", "+2", weapons on refine screen
space:
.string " "

.align 

strcat_wrapper:
addiu   sp, sp, -0x4
sw      ra, 0x00(sp)
jal strcat
nop

daddu    a0, v0, zero
li      a1, space

jal     strcat
nop

lw      ra, 0x00(sp)
addiu   sp, sp, 0x4
jr      ra
nop
