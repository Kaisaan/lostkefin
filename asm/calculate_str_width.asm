calculate_str_width:
	addiu sp, sp, -0x90
	daddu v0, zero, zero // width = 0

	// Save callee-saved registers
	sq fp, 0x80(sp)
	sq s7, 0x70(sp)
	sq s6, 0x60(sp)
	sq s5, 0x50(sp)
	sq s4, 0x40(sp)
	sq s3, 0x30(sp)
	sq s2, 0x20(sp)
	sq s1, 0x10(sp)
	sq s0, 0x0(sp)

	// Check if string is empty
	lbu v1, 0x0(a0)
	beqz v1, @end_of_string
	daddu s5, zero, zero // fullwidth_mode = false

	// Load character constants into registers for fast comparison
	addiu t8, zero, 0x1 // true constant
	addiu t3, zero, 0x46 // 'F'
	addiu t2, zero, 0x66 // 'f'
	addiu a1, zero, 0x3E // '>'
	addiu t1, zero, 0x48 // 'H'
	addiu t0, zero, 0x68 // 'h'
	addiu a3, zero, 0x42 // 'B'
	addiu a2, zero, 0x62 // 'b'
	addiu t6, zero, 0x7265 // "re"
	addiu t5, zero, 0x626C // "bl"
	addiu s7, zero, 0x6772 // "gr"
	addiu fp, zero, 0x7069 // "pi"
	addiu s2, zero, 0x20 // ' '
	addiu s1, zero, 0x81 // Shift-JIS lead byte
	addiu t7, zero, 0x40
	addiu s0, zero, 0x23 // '#'
	addiu t9, zero, 0x3C // '<'
	addiu s3, zero, 0xA // '\n'

@parse_loop:
	lbu s4, 0x0(a0)
	beq s4, s3, @handle_newline
	nop
	beq s4, s2, @handle_space
	nop
	beq s4, s1, @check_sjis_space
	nop
	nop

@after_sjis_check:
	beq s4, s0, @check_color_code
	nop

@after_color_check:
	beq s4, t9, @handle_tag
	nop

@handle_regular_char:
	slti at, s4, 0x81
	beqz at, @handle_multibyte
	nop
	// ASCII; load from table
	li s6, ascii_kerning_table
	addu s6, s6, s4
	lb t7, 0x0(s6)
	addu v0, v0, t7
	addiu t7, zero, 0x40
	b @continue_parse
	addiu a0, a0, 0x1


@handle_multibyte:
	addiu v0, v0, 0x18 // full-width
	addiu a0, a0, 0x2


@continue_parse:
	lbu v1, 0x0(a0)
	bnez v1, @parse_loop
	nop
	nop

@end_of_string:
	lq fp, 0x80(sp)
	lq s7, 0x70(sp)
	lq s6, 0x60(sp)
	lq s5, 0x50(sp)
	lq s4, 0x40(sp)
	lq s3, 0x30(sp)
	lq s2, 0x20(sp)
	lq s1, 0x10(sp)
	lq s0, 0x0(sp)
	jr ra
	addiu sp, sp, 0x90

@handle_newline:
	b @continue_parse
	addiu a0, a0, 0x1

@handle_space:
	bne s5, t8, @space_half_width
	nop
	b @space_done
	addiu v0, v0, 0x14 // full-width space

@space_half_width:
	addiu v0, v0, 0x6
	nop

@space_done:
	b @continue_parse
	addiu a0, a0, 0x1

@check_sjis_space:
	lbu v1, 0x1(a0)
	bne v1, t7, @after_sjis_check // not 0x40, not SJIS space
	nop
	addiu v0, v0, 0x14
	b @continue_parse
	addiu a0, a0, 0x2

@check_color_code:
	lbu t4, 0x1(a0)
	lbu v1, 0x2(a0)
	sll t4, t4, 8
	or v1, t4, v1
	ori v1, v1, 0x2020 // convert to lowercase

	beq v1, t6, @skip_color_code // "re"
	nop
	beq v1, t5, @skip_color_code // "bl"
	nop
	beq v1, s7, @skip_color_code // "gr"
	nop
	beq v1, fp, @skip_color_code // "pi"
	addiu t4, zero, 0x7768
	beq v1, t4, @skip_color_code // "wh"
	nop
	addiu t4, zero, 0x626B
	beq v1, t4, @skip_color_code // "bk"
	addiu t4, zero, 0x676C
	beq v1, t4, @skip_color_code // "gl"
	nop
	addiu t4, zero, 0x6379
	beq v1, t4, @skip_color_code // "cy"
	addiu t4, zero, 0x796C
	bne v1, t4, @after_color_check // not "yl", not a color code
	nop
	nop

@skip_color_code:
	b @continue_parse
	addiu a0, a0, 0x3

@handle_tag:
	lbu t4, 0x1(a0)
	addiu v1, zero, 0x2F // '/'
	beq t4, v1, @handle_close_tag
	nop

@check_open_F_tag:
	beq t4, t3, @check_F_close_bracket // 'F'
	nop
	beq t4, t2, @check_F_close_bracket // 'f'
	nop

@check_open_H_tag:
	beq t4, t1, @check_H_close_bracket // 'H'
	nop
	beq t4, t0, @check_H_close_bracket // 'h'
	nop

@check_open_B_tag:
	beq t4, a3, @check_B_close_bracket // 'B'
	nop
	beq t4, a2, @check_B_close_bracket // 'b'
	nop

@check_S_tag:
	addiu v1, zero, 0x53 // 'S'
	beq t4, v1, @check_S_close_bracket
	addiu v1, zero, 0x73 // 's'
	beq t4, v1, @check_S_close_bracket
	nop
	nop

@check_K_tag:
	addiu v1, zero, 0x4B // 'K'
	beq t4, v1, @check_kerning_tag
	addiu v1, zero, 0x6B // 'k'
	bne t4, v1, @handle_regular_char
	nop
	nop

@check_kerning_tag:
	lbu t4, 0x2(a0)
	slti v1, t4, 0x30
	bnez v1, @handle_regular_char // < '0'
	slti at, t4, 0x36
	beqz at, @handle_regular_char // >= '6'
	nop
	lbu v1, 0x3(a0)
	bne v1, a1, @handle_regular_char // not '>'
	nop
	b @continue_parse
	addiu a0, a0, 0x4 // skip "<Kn>"
	nop

@handle_close_tag:
	lbu v1, 0x2(a0)

@check_close_F:
	beq v1, t3, @check_close_F_complete // 'F'
	nop
	beq v1, t2, @check_close_F_complete // 'f'
	nop

@check_close_H:
	beq v1, t1, @check_close_H_complete // 'H'
	nop
	beq v1, t0, @check_close_H_complete // 'h'
	nop

@check_close_B:
	beq v1, a3, @check_close_B_complete // 'B'
	nop
	bne v1, a2, @check_open_F_tag // not 'b', fallthrough to open tag checks
	nop

@check_close_B_complete:
	lbu v1, 0x3(a0)
	bne v1, a1, @check_open_F_tag // not '>'
	nop
	b @continue_parse
	addiu a0, a0, 0x4 // skip "</B>"

@check_close_F_complete:
	lbu v1, 0x3(a0)
	bne v1, a1, @check_close_H // not '>'
	nop
	addiu a0, a0, 0x4 // skip "</F>"
	b @continue_parse
	daddu s5, t8, zero // fullwidth_mode = true

@check_close_H_complete:
	lbu v1, 0x3(a0)
	bne v1, a1, @check_close_B // not '>'
	nop
	b @continue_parse
	addiu a0, a0, 0x4 // skip "</H>"

@check_F_close_bracket:
	lbu v1, 0x2(a0)
	bne v1, a1, @check_open_H_tag // not '>'
	nop
	addiu a0, a0, 0x3 // skip "<F>"
	b @continue_parse
	daddu s5, t8, zero // fullwidth_mode = true

@check_H_close_bracket:
	lbu v1, 0x2(a0)
	bne v1, a1, @check_open_B_tag // not '>'
	nop
	b @continue_parse
	addiu a0, a0, 0x3 // skip "<H>"

@check_B_close_bracket:
	lbu v1, 0x2(a0)
	bne v1, a1, @check_S_tag // not '>'
	nop
	b @continue_parse
	addiu a0, a0, 0x3 // skip "<B>"

@check_S_close_bracket:
	lbu v1, 0x2(a0)
	bne v1, a1, @check_K_tag // not '>'
	nop
	addiu v0, v0, 0x5 // <S> adds 5 to width
	b @continue_parse
	addiu a0, a0, 0x3 // skip "<S>"
