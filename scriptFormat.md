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
In `SLPM_663.60` the font is located at $1A3E90 as 4BPP graphics, its palette is stored at $25E4C0, and the fontmap is at $1A31F0.  
`font.py` extracts the fontmap from `SLPM_663.60` to create a quick `font.tbl` table file.  
Use `kefin.tbl` for corrected values and control codes.  

### Control codes
|Hex Values|Meaning|Table file|
|---|---|---|
|`$0A`|Newline|`[LINE]\n`|
|`$2F $XXXX`|Normally `/`, unknown, $XXXX is stored in little-endian|   |
|`$3B $XX`|Show character name in dialoague box (see Character section)|`[CHAR]`|
|`$44 $XXXXXXXX`|Normally `D`, jump to new text with given Script Text (see above)|`[INDEX]`|
|`$XX $80`|Print $XX number of bytes|`[LEN]`|
|`$FF`|End text?|`[END]`|
|`$81A5`|Normally `▼`, wait for player input|`[WAIT]`|
|`$FFFD $XX`|Pause printing text for $XX frames(?)|`[PAUSE]`|

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
| $5 | スタン | Stan |
| $6 | ドーマン | Dorman |
| $7 | リジェ | Rije |
| $8 | ジャビル | Jabil |
| $9 | エフィ | Efi |
| $A | ケフィン王 | King Kefin |
| $B | アルガ | Arga |
| $C | ディオス | Dios |
| $D | ノティス | Notis |
| $E | チェイス | Chase |
| $F | アイシャ | Aisha |
| $10 | ウイリー | Willie |
| $11 | ムバーハ | Mubaha |
| $12 | バルク | Balk |
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
| $2B | レジスタンスＡ | Resistance A |
| $2C | レジスタンスＢ | Resistance B |
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
| $3B | 誘拐スタン | Kidnapped Stan |
| $3C | ノティス＆ディオス | Notis & Dios |
| $40 | 綺麗な女性 | Beautiful Woman |
| $41 | 女の子 | Girl |
| $42 | 乱暴者Ａ | Thug A |
| $43 | 乱暴者Ｂ | Thug B |
| $44 | 謎の声 | Mysterious Voice |
| $45 | 謎の男 | Mysterious Man |
| $46 | 大男 | Big Man |
| $47 | おばさん | Woman |
