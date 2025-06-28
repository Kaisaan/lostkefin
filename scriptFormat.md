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
One pointer can have as many lines of text and has no length limitations.  
  
### Font Info
All text is Shift-JIS encoded with fullwidth characters being 2 bytes long and 20 pixels wide while halfwidth characters are 1 byte long and 10 pixels wide.  
In `SLPM_663.60` the font graphics are located at $1A3E99 as 4BPP graphics, its palette is stored at $25E4C0, and the fontmap is at $1A31F0.  
`font.py` extracts the fontmap from `SLPM_663.60` to create a `font.tbl` table file.  
Use `kefin.tbl` for corrected values and control codes.  

### Textbox Sizing
The calculations for the size of the textbox can be found at the function located at `$4CE00` in `SLPM_663.60` (Loaded into `$0014CD80`)

# Opcodes
Each script is a series of opcodes, each with 0 or more bytes of data passed as parameters. Below is a WIP table of what opcodes do and how many bytes they take up.
Code that parses through the script files is located at `0x1BF0E0`. The table of opcode handlers is at `0x331EC0.`

# Script Command Reference

| Command | Description | Size/Format |
|---------|-------------|-------------|
| 0x4 | - | 1 |
| 0x5 | - | 1 |
| 0x6 | - | 1 |
| 0x7 | - | 2 |
| 0xa | text | 5 bytes then XX80 read XX bytes |
| 0xe | - | 2 |
| 0x10 | Init? | 1 |
| 0x11 | - | 1 |
| 0x12 | - | 1 |
| 0x15 | - | 3 |
| 0x18 | - | 4 |
| 0x1d | - | 4 |
| 0x1e | - | 10 |
| 0x20 | - | 4 |
| 0x28 | choice* | See below |
| 0x2f | - | 3 |
| 0x30 | - | 2 |
| 0x31 | - | 2 |
| 0x36 | - | 10 |
| 0x37 | camera pan? | 11 |
| 0x3b | - | 3 bytes then XX80 read XX bytes |
| 0x3f | - | 2 |
| 0x40 | - | 2 |
| 0x44 | - | 6 ? |
| 0x45 | - | 2 |
| 0x47 | - | 2 |
| 0x48 | - | 2 |
| 0x49 | - | 3 |
| 0x4c | fadeout? | 2 |
| 0x4d | cutscene? | 2 |
| 0x4f | - | 3 |
| 0x50 | - | 7 |
| 0x51 | - | 1 |
| 0x52 | - | reads 2 bytes then XX80 read XX bytes |
| 0x53 | - | 3 |
| 0x55 | - | 1 |
| 0x59 | - | 3 |
| 0x5a | end VN dialog | 1 |
| 0xFF | end script. stop parsing here | 1 |

### Choices

The choice opcode encodes the text of a question, the text of both responses, and indices to where to jump to in the script based on the response. 

`0x28 0xAA 0xBB` where AA and BB are some params, 

`0xXX 0x80 <question>...` for the question text, XX is # of bytes

`0xCC` where CC is another param.

`0xXX 0x80 <response 1>... 0xYY 0xYY 0xYY 0xYY` where YY is index to jump to if this option is chosen. XX is # of bytes

`0xZZ 0xXX 0x80 <response 2>... 0xZZ 0xZZ 0xZZ 0xZZ` where ZZ is index to jump to if this option is chosen. XX is # of bytes

`0xFF` to terminate the sequence

It's possible >2 options can be present, I think.

### Control Codes
Control codes occur mixed in with text and affect its formatting. (Everdred note: I think some of these are actually opcodes but not positive yet)

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
