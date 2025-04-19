# Ys V: Lost Kefin - Kingdom of Sand (PS2) English Translation
Currently using Sam Farron's translation from his [Translation Series](https://www.youtube.com/playlist?list=PLoD4gkRCJkUcgfpU5puBqYy5DX-RJK--b) with permission  

# How to Help
Since this translation project currently uses an existing translation, it would be helpful to have people transcribing all the text in Sam Farron's playthrough since I'm focusing on the hacking side of things.  
**If you want to help with the translation please [contact me!](https://kaisaan.github.io/pages/contact)**

# Current Progress  
I am replacing the usage of [armips](https://github.com/Kingcom/armips) with [acbde](https://www.romhacking.net/utilities/1392/) for script extraction and insertion. Currently I have raw dumps only as I need to figure out all the control codes to get a full pointer dump

# Building
- Use [Apache3](https://www.psx-place.com/threads/apache.19171/) to extract the contents of the game's .iso file
- Copy the contents to the `extracted` and `translated` folders
- Run `build.bat` or manually run the commands

# Hacking Notes
- The game uses SHIFT-JIS encoding for its text
- English letters are halfwidth (1 byte, 10 pixels wide) and Japanese letters are fullwith (2 bytes, 20 pixels wide)
- The game's base pointer is $FFF80
- Extracted .bin files with `_anm` in the filename are animation files with indexed 8BPP graphics and have the header `NAXA5010`
- Extracted .HGB files are texture files with 32BPP RGBA graphics
- Music files are `.hd` (header), `.bd` (header), and `.sq` (sequence) files
- See my [notes file](https://github.com/Kaisaan/lostkefin/blob/main/notes.txt) for more terribly organized notes

# Extracting the DATA.BIN Files
`extract.py` extracts all the files and folders from DATA.BIN into the `DATA` folder (but does not extract the files into their correct folders yet) and all files from DATA0.bin into the `DATA0` folder, a `logfile.txt` is also created

# Font info
The game uses Shift-JIS encoding but I decided to make table files so I can include control codes  
`font.py` extracts the fontmap from `SLPM_663.60` to create a quick `font.tbl` table file. Use `kefin.tbl` for corrected values and control codes  
In `SLPM_663.60` the font is located at $1A3E90 as 4BPP graphics, its palette is stored at $25E4C0, and the fontmap is at $1A31F0  

# Script Info
- Script files (named `stageXX.bin`) have the first $2000 bytes as a pointer table
- Each pointer first as an "index" number (4 bytes, little-endian) then the pointer value to the file (4 bytes, little-endian)
- Pointer value are calculated as `pointer + $2000`
- Changing the pointer seems to cause the game to freeze
Before running `script.py` copy the script files (as extracted from `DATA.BIN`) to the `scripts` folder. `script.py` will extract the pointer information for each file into a separate text file. The python script will also include info for control codes.  
Before running `dump.bat` make sure perl is installed. On Windows I recommend isnstalling [Strawberry perl](https://www.lifebottle.org/#/./other/strawberry-perl/index)  
The script can be dumped from `DATA.BIN` and into `scripts` after running `dump.bat`. Currently it is a raw dump because I have not figured out all the control codes, using a pointer dump will cause the scripts to be under-dumped.

# Control codes
`kefin.tbl` already has some control codes documented. The control code `$3B $XX` is to show character names in textboxes. `pointer.py` is used to extract the character names and their indexes to match.

# To do
- Figure out all the control codes properly
- Update the extraction script to extract `DATA0.BIN` folders, `DATA1.BIN`, and `SLPM_663.60`
- Continue inserting the English script

# Game Manual Translation
In the `manual` folder are scans for the game's manual. They were originally from [landofys.narod.ru](https://landofys.narod.ru/) which is now landofys.com.ru(http://landofys.com.ru/) was scanned by Dragon.

# Related Materials
- Translation of opening cutscene by [mziab](https://www.romhacking.net/forum/index.php?topic=28379.0) (I did not use this translation)
- Hacking attempt by [Hectavus](https://zenhax.com/viewtopic.php@t=15249.html) with only `SLPM_663.60` being translated
- Cheatcodes by [luc-ita](https://gamehacking.org/game/100384)
- Guide and walkthrough by [VoidZankantou](https://gamefaqs.gamespot.com/ps2/921272-ys-v-lost-kefin-kingdom-of-sand/faqs/44007)
- Guide addendum by [uncle5555](https://gamefaqs.gamespot.com/ps2/921272-ys-v-lost-kefin-kingdom-of-sand/answers/71872-help-with-getting-into-the-south-tower) (South Tower enterance requirements)
- Review the game by [Kurt Kalata](http://www.hardcoregaming101.net/ys-v-ushinawareta-suna-no-miyako-kefin/) (includes review for original SFC game)
- Original game website from [Taito](https://web.archive.org/web/20070804063125/http://www.taito.co.jp/d3/cp/ys/ys5/)

# Credits
- [Sam Farron](https://www.youtube.com/@samfarron) - Allowing me to use his translation as the basis of this project
- [Hilltop](https://x.com/HilltopWorks) - Providing valuable and informatative videos such as [hacking with Ghidra](https://youtu.be/qCEZC3cPc1s) and [PS1/PS2 graphics](https://youtu.be/lePKUCYakqM)
- [Life Bottle Productions](https://www.lifebottle.org/#/) - Providing me with their [isotool.py script](https://github.com/lifebottle/PythonLib/blob/main/isotool.py) and their tutorial for [finding the base pointer](https://youtu.be/q5aEj-aSw50)
- [The Geofront](https://geofront.esterior.net/) - Specifically folks on their [Discord Server](https://discord.gg/sXx2Ck6Cxn) for their support of this project
- My friend for introducing me to the world of *Ys*, also the biggest Lost Kefin fan so I'm doing this for him
- Sugunii for giving me motivation to play more *Ys*
- Falcom for making the wonderful *Ys* series
