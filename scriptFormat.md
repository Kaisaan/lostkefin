# Script File Format Documentation
This is information for the `stageXX.bin` files that are found in `DATA.BIN` of the game's ISO. There are 12 script files.

## The Format

|Address|Section|
|---|---|
|$0-$2000|Pointer Table|
|$2001-EOF|Script|

## Pointer Table
The pointer table has a repeating pattern of a **Script Index** and **Pointer**.  
**Script Index** is 4 bytes long and is stored in little-endian  
**Pointer** is 4 bytes long and is stored in little-endian
To get the true offset of the pointer add $2000 to the value  
For example, a pointer value of `00 E1 0C 00` ($CE100) means the true offset is at `$D0100`  
The table is always $2000 bytes long allowing for a maximum of 1024 entries.  
If there is less than 1024 entries the table section is padded with $00  

## Script
One pointer can have as many lines of text and has no length limitations.  
  
### Font Info
All text is Shift-JIS encoded with fullwidth characters being 2 bytes long and 20 pixels wide while halfwidth characters are 1 byte long and 10 pixels wide.  
In `SLPM_663.60` the font is located at $1A3E90 as 4BPP graphics, its palette is stored at $25E4C0, and the fontmap is at $1A31F0  
`font.py` extracts the fontmap from `SLPM_663.60` to create a quick `font.tbl` table file.  
Use `kefin.tbl` for corrected values and control codes  

### Control codes
|Hex Values|Meaning|Table file|
|---|---|---|
|`$0A`|Newline|`[LINE]\n|
|`$2F $XXXX`|Normally `/`, unknown, $XXXX is stored in little-endian|   |
|`$3B $XX`|Show character name in dialoague box (see Character section)|`[CHAR]`|
|`$44 $XXXXXXXX`|Normally `D`, jump to new text with given Script Text (see above)|`[INDEX]`|
|`$XX $80`|Print $XX number of bytes|[LEN]|
|`$FF`|End text?|[END]|
|`$81A5`|Normally `▼`, wait for player input|[WAIT]|
|`$FFFD $XX`|Pause printing text for $XX frames(?)|[PAUSE]|

#### Characters
The value of the `$3B` Character control code comes from the index value from a list of pointers.  
These pointers are found at $2298E0 in `SLPM_663.60` and `pointer.py` can be used to extract this list.  

|Value|Original Text|Translation|
|---|---|---|
|`$0`|アドル|Adol|
|`$1`|ドギ|Dogi|
|`$2`|ニーナ|   |
|`$3`|テラ|   |
|`$4`|マーシャ|   |
|`$5`|スタン|   |
|`$6`|ドーマン|   |
|`$7`|リジェ|   |
|`$8`|ジャビル|   |
|`$9`|エフィ|   |
|`$A`|ケフィン王|   |
|`$B`|アルガ|   |
|`$C`|ディオス|   |
|`$D`|ノティス|   |
|`$E`|チェイス|   |
|`$F`|アイシャ|   |
|`$10`|ウイリー|   |
|`$11`|ムバーハ|   |
|`$12`|バルク|   |
|`$13`|アビス|   |
|`$14`|カリオン|   |
|`$15`|鍛冶屋|   |
|`$16`|水夫|   |
|`$17`|執事|   |
|`$18`|メイド|   |
|`$19`|下級兵士|   |
|`$1A`|兵士|   |
|`$1B`|冒険家Ａ|   |
|`$1C`|冒険家Ｂ|   |
|`$1D`|商人Ａ|   |
|`$1E`|商人Ｂ|   |
|`$1F`|コボルト|   |
|`$20`|砂漠おばあさん|   |
|`$21`|砂漠おじいさん|   |
|`$22`|砂漠女|   |
|`$23`|砂漠男Ａ|   |
|`$24`|砂漠男Ｂ|   |
|`$25`|砂漠女の子|   |
|`$26`|砂漠男の子|   |
|`$27`|ケフィン男Ａ|   |
|`$28`|ケフィン男Ｂ|   |
|`$29`|ケフィン女Ａ|   |
|`$2A`|ケフィン女Ｂ|   |
|`$2B`|レジスタンスＡ|   |
|`$2C`|レジスタンスＢ|   |
|`$2D`|おじさんＡ|   |
|`$2E`|おじさんＢ|   |
|`$2F`|おばさん|   |
|`$30`|街男Ａ|   |
|`$31`|街男Ｂ|   |
|`$32`|街娘Ａ|   |
|`$33`|街娘Ｂ|   |
|`$34`|おばあさん|   |
|`$35`|おじいさん|   |
|`$36`|男の子Ａ|   |
|`$37`|男の子Ｂ|   |
|`$38`|女の子Ａ|   |
|`$39`|犬|   |
|`$3A`|女の子Ｂ|   |
|`$3B`|誘拐スタン|   |
|`$3C`|ノティス＆ディオス|   |
|`$40`|綺麗な女性|   |
|`$41`|女の子|   |
|`$42`|乱暴者Ａ|   |
|`$43`|乱暴者Ｂ|   |
|`$44`|謎の声|   |
|`$45`|謎の男|   |
|`$46`|大男|   |
|`$47`|おばさん|   |