text_box_size:
	addiu sp, sp, -0x90

	// Initialize variables
	daddu t7, zero, zero // current_line_width = 0
	sq fp, 0x80(sp)
	daddu v0, zero, zero // max_width = 0
	sq s7, 0x70(sp)
	daddu t6, zero, zero // total_height = 0

	// Save callee-saved registers
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
	daddu t5, zero, zero // fullwidth_mode = false

	// Load character constants into registers for fast comparison
	addiu t2, zero, 0x8
	addiu t8, zero, 0x3E // '>' tag close
	addiu s4, zero, 0x1 // true constant
	addiu s3, zero, 0x46 // 'F'
	addiu s2, zero, 0x66 // 'f'
	addiu s1, zero, 0x48 // 'H'(halfwidth)
	addiu s0, zero, 0x68 // 'h'(halfwidth)
	addiu t9, zero, 0x42 // 'B'(unknown)
	addiu s7, zero, 0x62 // 'b'(unknown)
	addiu fp, zero, 0xA // '\n'

@parse_loop:
	lbu v1, 0x0(a0)
	beq v1, fp, @handle_newline
	slt at, v0, t7 //(delay slot)check if current > max

	// Check for space character(0x20)
	addiu t3, zero, 0x20
	beq v1, t3, @handle_space
	addiu t3, zero, 0x81

	// Check for Shift-JIS fullwidth space(0x81 0x40)
	beq v1, t3, @check_sjis_space
	nop

@after_sjis_check:
	// Check for 0xFF escape sequence
	addiu t3, zero, 0xFF
	beq v1, t3, @check_ff_escape
	nop
	nop

@after_ff_check:
	// Check for // color code
	addiu t3, zero, 0x23 // '//'
	beq v1, t3, @check_color_code
	nop
	nop

@after_color_check:
	// Check for < tag start
	addiu t3, zero, 0x3C // '<'
	beq v1, t3, @handle_tag
	nop
	nop

@handle_regular_char:
	// Check if digit(0x30-0x39 = '0'-'9')
	slti t3, v1, 0x30
	bnez t3, @not_digit
	slti at, v1, 0x3A
	beqz at, @not_digit
	nop

	// Digits are full-width
	addu t7, t7, a3 // current_line_width += char_width
	b @continue_parse
	addiu a0, a0, 0x1 // str++

@not_digit:
	// Check if ASCII char(< 0x81)
	slti at, v1, 0x81
	beqz at, @handle_multibyte
	nop

	// ASCII chars are half-width, call external width function

	addiu sp, sp, -0x4
	sw s0, 0x00(sp)

	li s0, ascii_kerning_table
	addu s0, s0, v1
	lb v1, 0x0(s0)
	addu t7, t7, v1

	lw s0, 0x00(sp)
	addiu sp, sp, 0x4
	b @continue_parse
	addiu a0, a0, 0x1

@handle_multibyte:
	beqz t1, @multibyte_no_exceptions
	daddu t3, zero, zero // found_exception = false
	daddu t4, zero, zero // index = 0
	nop

@check_zero_width_loop:
	addu s6, t1, t4 // ptr = zero_width_pairs + index
	lbu s5, 0x0(s6)// first byte of pair
	beqz s5, @multibyte_no_exceptions // null terminator = end of list
	nop
	bne v1, s5, @next_zero_width_pair
	nop

	// First byte matched, check second byte
	lbu s5, 0x1(s6)// second byte of pair
	lbu s6, 0x1(a0)// second byte of input
	bne s6, s5, @next_zero_width_pair
	nop

	// Both bytes match - this is a zero-width character pair
	daddu t3, s4, zero // found_exception = true
	nop

@multibyte_no_exceptions:
	bnez t3, @multibyte_skip_width
	nop
	addu t7, t7, a3 // current_line_width += char_width(full-width)
	nop

@multibyte_skip_width:
	b @continue_parse
	addiu a0, a0, 0x2 // str += 2(multi-byte char)

@next_zero_width_pair:
	b @check_zero_width_loop
	addiu t4, t4, 0x2 // index += 2

@continue_parse:
	lbu v1, 0x0(a0)
	bnez v1, @parse_loop
	nop
	b @end_of_string
	nop

@finalize_last_line:
	slt at, v0, t7

@check_max_width:
	beqz at, @store_results
	nop
	daddu v0, t7, zero // max_width = current_line_width

@store_results:
	sw t6, 0x0(a2)// *out_height = total_height
	b @epilogue
	sw v0, 0x0(a1)// *out_width = max_width

@handle_newline:
	addiu a0, a0, 0x1 // str++
	beqz at, @newline_no_update_max
	addu t6, t6, t0 // total_height += line_height
	daddu v0, t7, zero // max_width = current_line_width

@newline_no_update_max:
	b @continue_parse
	daddu t7, zero, zero // current_line_width = 0

@handle_space:
	bne t5, s4, @space_half_width
	nop
	b @space_done
	addu t7, t7, a3 // full-width space

@space_half_width:
	addu t7, t7, t2 // half-width space
	nop

@space_done:
	b @continue_parse
	addiu a0, a0, 0x1

@check_sjis_space:
	lbu t4, 0x1(a0)
	addiu t3, zero, 0x40
	bne t4, t3, @after_sjis_check
	nop
	addu t7, t7, a3 // current_line_width += char_width
	b @continue_parse
	addiu a0, a0, 0x2
	nop

@check_ff_escape:
	lbu t4, 0x1(a0)
	addiu t3, zero, 0xFD
	bne t4, t3, @after_ff_check
	nop
	b @continue_parse
	addiu a0, a0, 0x3 // skip 3-byte escape sequence

@check_color_code:
	lbu t4, 0x1(a0)// first char of color
	lbu t3, 0x2(a0)// second char of color
	sll t4, t4, 8 // combine into 16-bit value
	or t3, t4, t3
	ori t3, t3, 0x2020 // convert to lowercase

	// Check each valid color code
	addiu t4, zero, 0x7265 // "re"(red)
	beq t3, t4, @skip_color_code
	addiu t4, zero, 0x626C // "bl"(blue)
	beq t3, t4, @skip_color_code
	nop
	addiu t4, zero, 0x6772 // "gr"(green)
	beq t3, t4, @skip_color_code
	addiu t4, zero, 0x7069 // "pi"(pink)
	beq t3, t4, @skip_color_code
	nop
	addiu t4, zero, 0x7768 // "wh"(white)
	beq t3, t4, @skip_color_code
	addiu t4, zero, 0x626B // "bk"(black)
	beq t3, t4, @skip_color_code
	nop
	addiu t4, zero, 0x676C // "gl"(gold/glow?)
	beq t3, t4, @skip_color_code
	addiu t4, zero, 0x6379 // "cy"(cyan)
	beq t3, t4, @skip_color_code
	nop
	addiu t4, zero, 0x796C // "yl"(yellow)
	bne t3, t4, @after_color_check
	nop

@skip_color_code:
	b @continue_parse
	addiu a0, a0, 0x3 // skip "//XX"

@handle_tag:
	lbu t4, 0x1(a0)// tag character
	addiu t3, zero, 0x2F // '/'
	beq t4, t3, @handle_close_tag
	nop

@check_open_F_tag:
	beq t4, s3, @check_F_close_bracket // 'F'
	nop
	beq t4, s2, @check_F_close_bracket // 'f'
	nop

@check_open_H_tag:
	beq t4, s1, @check_H_close_bracket // 'H'(halfwidth)
	nop
	beq t4, s0, @check_H_close_bracket // 'h'(halfwidth)
	nop

@check_open_B_tag:
	beq t4, t9, @check_B_close_bracket // 'B'(unknown)
	nop
	beq t4, s7, @check_B_close_bracket // 'b'(unknown)
	nop

@check_W_tag:
	addiu t3, zero, 0x57 // 'W'
	bne t4, t3, @check_lowercase_w
	nop
	nop

@parse_wait_tag:
	addiu v1, zero, 0x2 // start after "<W"
	nop

@wait_digit_loop:
	addu t3, a0, v1
	lbu t4, 0x0(t3)
	slti t3, t4, 0x30 // < '0'?
	bnez t3, @wait_tag_end

    slti at, t4, 0x3A

	beqz at, @wait_tag_end
	nop
	b @wait_digit_loop
	addiu v1, v1, 0x1 // consume digit
	nop

@handle_close_tag:
	lbu t3, 0x2(a0)// char after '/'

	// Check </F> or </f>
	beq t3, s3, @check_close_F_complete // 'F'
	nop
	beq t3, s2, @check_close_F_complete // 'f'
	nop
	nop

@check_close_H:
	beq t3, s1, @check_close_H_complete // 'H'(halfwidth)
	nop
	beq t3, s0, @check_close_H_complete // 'h'(halfwidth)
	nop

@check_close_B:
	beq t3, t9, @check_close_B_complete // 'B'(unknown)
	nop
	bne t3, s7, @check_open_F_tag // not 'b', try open tags
	nop

@check_close_B_complete:
	lbu t3, 0x3(a0)
	bne t3, t8, @check_open_F_tag // needs '>'
	nop
	b @continue_parse
	addiu a0, a0, 0x4 // skip "</B>"
	nop

@check_close_F_complete:
	lbu s5, 0x3(a0)
	bne s5, t8, @check_close_H // needs '>'
	nop
	addiu a0, a0, 0x4 // skip "</F>"
	b @continue_parse
	daddu t5, s4, zero // fullwidth_mode = true(oddly, closing enables it)

@check_close_H_complete:
	lbu s5, 0x3(a0)
	bne s5, t8, @check_close_B // needs '>'
	nop
	b @continue_parse
	addiu a0, a0, 0x4 // skip "</H>"(end halfwidth)
	nop

@check_F_close_bracket:
	lbu t3, 0x2(a0)
	bne t3, t8, @check_open_H_tag // needs '>'
	nop
	addiu a0, a0, 0x3 // skip "<F>"
	b @continue_parse
	daddu t5, s4, zero // fullwidth_mode = true

@check_H_close_bracket:
	lbu t3, 0x2(a0)
	bne t3, t8, @check_open_B_tag // needs '>'
	nop
	b @continue_parse
	addiu a0, a0, 0x3 // skip "<H>"(begin halfwidth)
	nop

@check_B_close_bracket:
	lbu t3, 0x2(a0)
	bne t3, t8, @check_W_tag // needs '>'
	nop
	b @continue_parse
	addiu a0, a0, 0x3 // skip "<B>"(unknown)
	nop

@check_lowercase_w:
	addiu t3, zero, 0x77 // 'w'
	beq t4, t3, @parse_wait_tag
	addiu t3, zero, 0x4B // 'K'
	beq t4, t3, @check_kerning_tag
	nop
	addiu t3, zero, 0x6B // 'k'
	bne t4, t3, @handle_regular_char
	nop

@check_kerning_tag:
	// <K//> where // is 0-5
	lbu t3, 0x2(a0)
	slti at, t3, 0x30 // < '0'?
	beqz at, @kerning_check_upper

    slti at, t3, 0x36 // < '6'?
	beqz at, @handle_regular_char
	nop

@kerning_check_upper:
	lbu t3, 0x3(a0)
	bne t3, t8, @handle_regular_char // needs '>'
	nop
	b @continue_parse
	addiu a0, a0, 0x4 // skip "<K//>"
	nop

@wait_tag_end:
	bne t4, t8, @wait_no_close_bracket // check for '>'
	nop
	addiu v1, v1, 0x1 // include the '>'
	nop

@wait_no_close_bracket:
	b @continue_parse
	addu a0, a0, v1 // skip entire wait tag

@end_of_string:
	beqz t7, @finalize_last_line // if current_line_width == 0, skip height add
	slt at, v0, t7
	b @finalize_last_line
	addu t6, t6, t0 // total_height += line_height for final line

@epilogue:
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
