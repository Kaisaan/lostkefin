# Ys V: Lost Kefin - Kingdom of Sand (PS2) English Translation
Currently using Sam Farron's translation from his [Translation Series](https://www.youtube.com/playlist?list=PLoD4gkRCJkUcgfpU5puBqYy5DX-RJK--b) with permission  

# How to Help
Since this translation project currently uses an existing translation, it would be helpful to have people transcribing all the text in Sam Farron's playthrough since I'm focusing on the hacking side of things.  
**If you want to help with the translation please [contact me!](https://kaisaan.github.io/pages/contact)**

# Current Progress  
Script extract and insertion is now done with [acbde](https://www.romhacking.net/utilities/1392/) with miscellanous text being patched in with [armips](https://github.com/Kingcom/armips).  
Now the goal is to get a proof of concept patch working.

# Building
- Copy the original .iso to the root of this repo and rename it to `lostkefin.iso`
- Run `isotool.py -m extract --iso lostkefin.iso --filelist filelist --files extracted` to extract all the files
- Copy the contents to the `extracted` and `translated` folders
- Make changes as needed to the files in the `translated` folder
- Run `isotool.py -m insert --iso lostkefin.iso -o english.iso --filelist filelist.txt --files translated` to create a modified `english.iso`
Running build.bat automatically patches `patch.asm` and builds `english.iso`

# Hacking Notes
- See [scriptFormat.md](https://github.com/Kaisaan/lostkefin/blob/main/scriptFormat.md) for all information about the game's script system
- The game's base pointer is $FFF80
- Extracted .bin files with `_anm` in the filename are animation files with indexed 8BPP graphics and have the header `NAXA5010`
- Extracted .HGB files are texture files with 32BPP RGBA graphics
- Music files are `.hd` (header), `.bd` (header), and `.sq` (sequence) files
- See my [notes file](https://github.com/Kaisaan/lostkefin/blob/main/notes.txt) for more terribly organized notes

# Extracting the DATA.BIN Files
`extract.py` extracts all the files and folders from DATA.BIN into the `DATA` folder (but does not extract the files into their correct folders yet) and all files from DATA0.bin into the `DATA0` folder, a `logfile.txt` is also created

# To do
- Figure out all the control codes properly
- Update the extraction script to extract `DATA0.BIN` folders, `DATA1.BIN`, and `SLPM_663.60`
- Continue inserting the English script
- Extract, edit, and reinsert graphics

# Game Manual Translation
In the `manual` folder are scans for the game's manual. They were originally from [landofys.narod.ru](https://landofys.narod.ru/) which is now [landofys.com.ru](http://landofys.com.ru/) was scanned by Dragon.

# Related Materials
- Translation of opening cutscene by [mziab](https://www.romhacking.net/forum/index.php?topic=28379.0) (I did not use this translation)
- Hacking attempt by [Hectavus](https://zenhax.com/viewtopic.php@t=15249.html) with only `SLPM_663.60` being translated
- Cheatcodes by [luc-ita](https://gamehacking.org/game/100384)
- Guide and walkthrough by [VoidZankantou](https://gamefaqs.gamespot.com/ps2/921272-ys-v-lost-kefin-kingdom-of-sand/faqs/44007)
- Guide addendum by [uncle5555](https://gamefaqs.gamespot.com/ps2/921272-ys-v-lost-kefin-kingdom-of-sand/answers/71872-help-with-getting-into-the-south-tower) (South Tower enterance requirements)
- Review the game by [Kurt Kalata](http://www.hardcoregaming101.net/ys-v-ushinawareta-suna-no-miyako-kefin/) (includes review for original SFC game)
- Original game website from [Taito](https://web.archive.org/web/20070804063125/http://www.taito.co.jp/d3/cp/ys/ys5/)

# Credits
- [Etokapa](https://github.com/Etokapa/) - Big help with this project! Text insertion and also texting extraction and rebuilding
- [Sam Farron](https://www.youtube.com/@samfarron) - Allowing me to use his translation as the basis of this project
- [Hilltop](https://x.com/HilltopWorks) - Providing valuable and informatative videos such as [hacking with Ghidra](https://youtu.be/qCEZC3cPc1s) and [PS1/PS2 graphics](https://youtu.be/lePKUCYakqM)
- [Life Bottle Productions](https://www.lifebottle.org/#/) - Providing me with their [isotool.py script](https://github.com/lifebottle/PythonLib/blob/main/isotool.py) and their tutorial for [finding the base pointer](https://youtu.be/q5aEj-aSw50)
- [The Geofront](https://geofront.esterior.net/) - Specifically folks on their [Discord Server](https://discord.gg/sXx2Ck6Cxn) for their support of this project
- My friend for introducing me to the world of *Ys*, also the biggest Lost Kefin fan so I'm doing this for him
- Sugunii for giving me motivation to play more *Ys*
- Falcom for making the wonderful *Ys* series
