# Script File Format Documentation
This is information for the `stageXX.bin` files that are found in `DATA.BIN` of the game's ISO. There are 12 script files.

## The Format

|Address|Section|
|---|---|
|$0-$2000|Pointer Table|
|$2001-EOF|Script|

## Pointer Table
The pointer table has a repeating pattern of a **Script Index** and **Pointer**.  
**Script Index** is 4 bytes long and is stored in little-endian.  
**Pointer** is 4 bytes long and is stored in little-endian.  
To get the true offset of the pointer add $2000 to the value.  
For example, a pointer value of `00 E1 0C 00` ($CE100) means the true offset is at `$D0100`.  
The table is always $2000 bytes long allowing for a maximum of 1024 entries.  
If there is less than 1024 entries the table section is padded with `$00`'s.  

## Script
Executed one opcode at a time, and executes until a $FF opcode is reached. There are relative and absolute jump opcodes though, so a script can realistic executes any opcode in the whole file. 


# Opcodes
Each script is a series of opcodes, each with 0 or more bytes of data passed as parameters. Below is a table of what opcodes do and how many bytes they take up.
Code that parses through the script files is located at `$1BF0E0`. The table of opcode handlers is at `$331EC0.`

| Command | Description | Size/Format |
|---------|-------------|-------------|
| $02 | ScreenEffect | 1 |
| $03 | ScreenEffect2 | 1 |
| $04 | Unkn_4 | 0 |
| $05 | Unkn_5 | 0 |
| $06 | Unkn_6 | 0 |
| $07 | Unkn_7 | 1 |
| $08 | Debug (null-terminated string) | variable |
| $09 | Debug2 (null-terminated string) | variable |
| $0A | CutsceneText | 4 bytes + 1 byte length + string |
| $0B | Unkn_B | 0 |
| $0C | Unkn_C | 0 |
| $0E | Unkn_E | 1 |
| $10 | Unkn_10 | 0 |
| $11 | Unkn_11 | 0 |
| $12 | Unkn_12 | 0 |
| $13 | Unkn_13 | 3 |
| $14 | Unkn_14 | 1 |
| $15 | Unkn_15 | 2 |
| $16 | Unkn_16 | 3 |
| $17 | Debug3 (null-terminated string + 2 bytes) | variable |
| $18 | Unkn_18 | 3 |
| $19 | Unkn_19 | 8 |
| $1A | Unkn_1A | 3 |
| $1B | Unkn_1B | 6 |
| $1C | Unkn_1C | 4 |
| $1D | Unkn_1D | 3 |
| $1E | Unkn_1E | 9 |
| $1F | Unkn_1F | 4 |
| $20 | Unkn_20 | 3 |
| $21 | Unkn_21 | 3 |
| $22 | Unkn_22 | 4 |
| $23 | Unkn_23 | 5 |
| $24 | FourChoice | 4 bytes + choices (see Choices section) |
| $25 | FourChoiceType2 | 2 bytes + choices (see Choices section) |
| $26 | FourChoiceType3 | 2 bytes + choices (see Choices section) |
| $27 | BubbleChoice | 4 bytes + choices (see Choices section) |
| $28 | Choice | 2 bytes + choices (see Choices section) |
| $29 | BubbleChoice2 | 2 bytes + choices (see Choices section) |
| $2A | RotateCamera | 3 |
| $2B | Unkn_2B | 1 |
| $2C | Unkn_2C | 1 |
| $2D | Unkn_2D | 9 |
| $2E | Debug4 (null-terminated string) | variable |
| $2F | Unkn_2F | 2 |
| $30 | Unkn_30 | 1 |
| $31 | Unkn_31 | 1 |
| $33 | PlayEndingCutscene | 1 |
| $34 | Unkn_34 | 0 |
| $35 | TextBubbleNoTail | 4 bytes + 1 byte length + string |
| $36 | Unkn_36 | 10 |
| $37 | CameraPan | 10 |
| $38 | Unkn_38 | 6 |
| $39 | MoveCharacter | 6 |
| $3B | VNText | 2 bytes + 1 byte length + string |
| $3C | ConditionalRelativeJump | 2 bytes target + 2 bytes type |
| $3E | Unkn_3E | 1 |
| $3F | Unkn_3F | 1 |
| $40 | Unkn_40 | 1 |
| $41 | Unkn_41 | 1 |
| $42 | Unkn_42 | 2 |
| $43 | ScreenWipe | 2 |
| $44 | UnconditionalJump | 4 |
| $45 | Unkn_45 | 1 |
| $47 | Unkn_47 | 1 |
| $48 | Unkn_48 | 1 |
| $49 | Unkn_49 | 2 |
| $4A | Unkn_4A | 3 |
| $4B | Unkn_4B | 3 |
| $4C | Unkn_4C | 1 |
| $4D | Unkn_4D | 1 |
| $4E | Unkn_4E | 0 |
| $4F | Unkn_4F | 2 |
| $50 | ShowCharacters | 6 |
| $51 | StartVNSection | 0 |
| $52 | TextBubble | 2 bytes + 1 byte length + string |
| $53 | Unkn_53 | 2 |
| $54 | Debug5 (null-terminated string) | variable |
| $55 | Unkn_55 | 0 |
| $56 | Unkn_56 | 1 |
| $57 | Unkn_57 | 2 |
| $58 | Unkn_58 | 2 |
| $59 | Unkn_59 | 2 |
| $5A | EndVNSection | 0 |
| $5B | Unkn_5B | 3 |
| $5C | Unkn_5C | 3 |
| $5D | Unkn_5D | 3 |
| $5E | Unkn_5E | 1 |
| $5F | Unkn_5F | 1 |
| $60 | Unkn_60 | 2 |
| $62 | Unkn_62 | 3 |
| $63 | Unkn_63 | 3 |
| $64 | Teleport | 14 |
| $65 | OpenShop | 2 |
| $66 | Unkn_66 | 9 |
| $67 | Unkn_67 | 0 |
| $FF | EndScript | 0 |


### Debug

Reads a string until a null byte. Strings look like "#door_b_1_door3" so I'm guessing this is a debug print.

### Conditional relative jump (opcode 0x3c)

Based on a condition type, will check some other areas of memory and either jump ahead X bytes, or just execute the next instruction. 

For example: 
3C 05 00 46 00 4E 44

This is a 0x46 type jump which will jump 5 bytes ahead if true. So it will either execute the next opcode (0x4e) or jump 5 bytes (0x44).

I've only looked at type 0x46 so far.

### Choices

The choice opcode encodes the text of a question, the text of both responses, and indices to where to jump to in the script based on the response. 

`0x28 0xAA 0xBB` where AA and BB are some params, 

`0xXX 0x80 <question>...` for the question text, XX is # of bytes

`0xXX 0x80 <response 1>... 0xYY 0xYY 0xYY 0xYY` where YY is index to jump to if this option is chosen. XX is # of bytes

`0xZZ 0xXX 0x80 <response 2>... 0xZZ 0xZZ 0xZZ 0xZZ` where ZZ is index to jump to if this option is chosen. XX is # of bytes

`0xFF` to terminate the sequence

Depending on the opcode there are either 2 choices or 4.


# Strings

Prefixed by XXYY. XX is the string length and YY is a set of string flags though I've only ever seen it set to 0x80.

### Font Info
All text is Shift-JIS encoded with fullwidth characters being 2 bytes long and 20 pixels wide while halfwidth characters are 1 byte long and 10 pixels wide.  
In `SLPM_663.60` the font graphics are located at $1A3E99 as 4BPP graphics, its palette is stored at $25E4C0, and the fontmap is at $1A31F0.  
`font.py` extracts the fontmap from `SLPM_663.60` to create a `font.tbl` table file.  
Use `kefin.tbl` for corrected values and control codes.  

### Textbox Sizing
The calculations for the size of the textbox can be found at the function located at `$4CE00` in `SLPM_663.60` (Loaded into `$0014CD80`)


### Control Codes
Control codes occur mixed in with text and affect its formatting. 

|Hex Values|Meaning|Table file|
|---|---|---|
|`$0A`|Newline|`[LINE]`|
|`$1D $XXXX`|Move NPC? If `$XXXX` is not `$3000` then the NPC will not face Adol|`[MOVE]`|
|`$1D $XXXX $YYYY`|Move NPC? `$YYYY` is the direction the NPC will face|`[MOVE]`|
|`$23 $XXXX`|Normally `#`, change colour of text based on ASCII values of $XXXX (See Colour Section)|`[HASH]`|
|`$2F $XXXX`|Normally `/`, unknown, $XXXX is stored in little-endian|`/<$XX><$XX>`|
|`$3B $XX`|Show character name in dialoague box (see Character section)|`[CHAR]`|
|`$44 $XXXXXXXX`|Normally `D`, jump to new text with given Script Text (see above)|`[INDEX]`|
|`$52 $XXXX`|Normally `R`, set textbox? If `$XXXX` is not `$3000` then it will not point to the speaker|[BOX]|
|`$XX $80`|Print $XX number of bytes|`[LEN]`|
|`$FF`|End text?|`[END]`|
|`$81A5`|Normally `▼`, wait for player input|`[WAIT]`|
|`$FFFD $XX`|Pause printing text for $XX frames(?)|`[PAUSE]`|

`string.py` can be used to calculate a new [LEN] value.

#### Colours
The value of the `$23` Colour control code translates to the ASCII values of the two bytes after the code.  
White is the default colour for text.

|Hex values|ASCII|Meaning|Colour code|
|---|---|---|---|
|`$77 $68`|`wh`|White|   |
|`$67 $72`|`gr`|Green|   |
|`$62 $6C`|`bl`|Blue|   |
|`$70 $69`|`pi`|Pink|   |
|`$79 $6C`|`yl`|Yellow|   |
|`$72 $65`|`re`|Red|   |
|`$62 $6B`|`bk`|Black|   |
|`$67 $6C`|`gl`|Gray|   |
|`$63 $79`|`cy`|Cyan|   | 


#### Characters
The value of the `$3B` Character control code comes from the index value from a list of pointers.  
These pointers are found at $2298E0 in `SLPM_663.60` and `pointer.py` can be used to extract this list.

| Value | Original Text | Translation |
|---|---|---|
| $0 | アドル | Adol |
| $1 | ドギ | Dogi |
| $2 | ニーナ | Niena |
| $3 | テラ | Terra |
| $4 | マーシャ | Massea |
| $5 | スタン | Stein |
| $6 | ドーマン | Doman |
| $7 | リジェ | Rizze |
| $8 | ジャビル | Jabir |
| $9 | エフィ | Effey |
| $A | ケフィン王 | King Kefin |
| $B | アルガ | Alga |
| $C | ディオス | Dios |
| $D | ノティス | Nottis |
| $E | チェイス | Chase |
| $F | アイシャ | Aisha |
| $10 | ウイリー | Willy |
| $11 | ムバーハ | Mubaja |
| $12 | バルク | Baruq |
| $13 | アビス | Abyss |
| $14 | カリオン | Karion |
| $15 | 鍛冶屋 | Blacksmith |
| $16 | 水夫 | Sailor |
| $17 | 執事 | Butler |
| $18 | メイド | Maid |
| $19 | 下級兵士 | Foot Soldier |
| $1A | 兵士 | Soldier |
| $1B | 冒険家Ａ | Adventurer A |
| $1C | 冒険家Ｂ | Adventurer B |
| $1D | 商人Ａ | Merchant A |
| $1E | 商人Ｂ | Merchant B |
| $1F | コボルト | Kobold |
| $20 | 砂漠おばあさん | Desert Old Woman |
| $21 | 砂漠おじいさん | Desert Old Man |
| $22 | 砂漠女 | Desert Woman |
| $23 | 砂漠男Ａ | Desert Man A |
| $24 | 砂漠男Ｂ | Desert Man B |
| $25 | 砂漠女の子 | Desert Girl |
| $26 | 砂漠男の子 | Desert Boy |
| $27 | ケフィン男Ａ | Kefin Man A |
| $28 | ケフィン男Ｂ | Kefin Man B |
| $29 | ケフィン女Ａ | Kefin Woman A |
| $2A | ケフィン女Ｂ | Kefin Woman B |
| $2B | レジスタンスＡ | Rebel A |
| $2C | レジスタンスＢ | Rebel B |
| $2D | おじさんＡ | Man A |
| $2E | おじさんＢ | Man B |
| $2F | おばさん | Woman |
| $30 | 街男Ａ | Villager Man A |
| $31 | 街男Ｂ | Villager Man B |
| $32 | 街娘Ａ | Villager Girl A |
| $33 | 街娘Ｂ | Villager Girl B |
| $34 | おばあさん | Old Woman |
| $35 | おじいさん | Old Man |
| $36 | 男の子Ａ | Boy A |
| $37 | 男の子Ｂ | Boy B |
| $38 | 女の子Ａ | Girl A |
| $39 | 犬 | Dog |
| $3A | 女の子Ｂ | Girl B |
| $3B | 誘拐スタン | Kidnapped Stein |
| $3C | ノティス＆ディオス | Noties & Deios |
| $40 | 綺麗な女性 | Beautiful Woman |
| $41 | 女の子 | Girl |
| $42 | 乱暴者Ａ | Thug A |
| $43 | 乱暴者Ｂ | Thug B |
| $44 | 謎の声 | Mysterious Voice |
| $45 | 謎の男 | Mysterious Man |
| $46 | 大男 | Big Man |
| $47 | おばさん | Woman |
