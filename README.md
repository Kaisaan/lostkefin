# Ys V: Lost Kefin - Kingdom of Sand (PS2) English Translation
All the files and documentation for the translation of *Ys V: Lost Kefin, Kingdom of Sand* for the Playstation 2

# How to Help 
If you want to help with the translation please join the project's [Discord Server](https://discord.gg/TNWGBGpZGN) or otherwise [contact me](https://kaisaan.github.io/pages/contact).

# Current Progress  
Script extraction and insertion is now done with [acbde](https://www.romhacking.net/utilities/1392/) with miscellanous text being patched in with [armips](https://github.com/Kingcom/armips).  
Now the goal is to get a proof of concept patch working.

# Building
- Copy the original .iso to the root of this repo and rename it to `lostkefin.iso`
- Run `1 Extract ISO.bat`
- Make changes to `scripts/translated.txt`
- Run `2 Patch ISO.bat`

# Translating
Translation is currently being done with [Google Sheets](https://docs.google.com/spreadsheets/d/1kcEely3uIDJAifqj9kn16Bky8mBBoed03CgAwd4B0W8/edit?usp=sharing) and then copied over to `scripts/translated.txt`

# Hacking Notes
- See [scriptFormat.md](https://github.com/Kaisaan/lostkefin/blob/main/scriptFormat.md) for all information about the game's script system
- See [graphicsFormat.md](https://github.com/Kaisaan/lostkefin/blob/main/graphicsFormat.md) for all information about the game's graphics formats
- The game's base pointer is $FFF80 meaning all pointers in `SLPM_663.60` are calculated as `(True offset) + $FFF80`
- Music files are `.hd` (header), `.bd` (header), and `.sq` (sequence) files
- See my [notes file](https://github.com/Kaisaan/lostkefin/blob/main/notes.txt) for more terribly organized notes

# Extracting the DATA.BIN Files
`extract.py` extracts all the files and folders from DATA.BIN into the `DATA` folder (but does not extract the files into their correct folders yet) and all files from DATA0.bin into the `DATA0` folder, a `logfile.txt` is also created

# To do
- Update the extraction script to extract `DATA0.BIN` folders, files `DATA1.BIN`, and possibly text from `SLPM_663.60`
- Continue translating and inserting English script
- Edit and reinsert graphics
- Translate manual

# Game Manual Translation
In the `manual` folder are scans for the game's manual. They were originally from [landofys.narod.ru](https://landofys.narod.ru/) which is now [landofys.com.ru](http://landofys.com.ru/) was scanned by Dragon.

# Contributors
A big thanks to these wonderful people for helping with this project! This project would not be where it is without any of them.  
- [Sam Farron](https://www.youtube.com/@samfarron) - Allowing me to use his translation as the basis of this project
- [Etokapa](https://github.com/Etokapa/) - Text transcribing, making better batch files, making useful scripts, testing
- [Seiichiro Mine](https://github.com/SeiichiroMine) - Translation
- [Sorcerian](https://bsky.app/profile/sorcerian.bsky.social) - Graphics Editing

# Related Materials
- Translation of opening cutscene by [mziab](https://www.romhacking.net/forum/index.php?topic=28379.0) (I did not use this translation)
- Hacking attempt by [Hectavus](https://zenhax.com/viewtopic.php@t=15249.html) with only `SLPM_663.60` being translated
- Cheatcodes by [luc-ita](https://gamehacking.org/game/100384)
- Cheatcodes by GodShin: [Action Replay MAX](https://www.european-codebase.de/daten.php?system=ps2&act=detail1&id=8253), [Action Replay V2](https://www.european-codebase.de/daten.php?system=ps2&act=detail1&id=8252), [Xterminator/Xploder](https://www.european-codebase.de/daten.php?system=ps2&act=detail1&id=8251)
- Cheatcodes by [TOMBOY](https://blog.goo.ne.jp/touffu/e/c484169262662f0dd6632c97c6c695c7)
- Cheatcodes by [warezhunter_](https://psx-core.ru/forum/2-51-45)
- Cheatcodes by レインたんラブ [Part 1](https://jp.wazap.com/cheat/%E3%82%B3%E3%83%BC%E3%83%89/521993/) [Part 2](https://jp.wazap.com/cheat/%E3%82%B3%E3%83%BC%E3%83%89%EF%BC%92/522889/)
- Cheatcodes by 世界のマリオ [Original post](https://jp.wazap.com/cheat/%E5%85%A8%E3%82%A8%E3%83%AC%E3%83%A1%E3%83%B3%E3%83%88%EF%BC%99%EF%BC%99%EF%BC%99%EF%BC%99/434220/) [Archived page](https://web.archive.org/web/20150104205942/http://www17.ocn.ne.jp:80/~altcodex/ys5.htm)
- Guide by [VoidZankantou](https://gamefaqs.gamespot.com/ps2/921272-ys-v-lost-kefin-kingdom-of-sand/faqs/44007) (incomplete)
- Guide addendum by [uncle5555](https://gamefaqs.gamespot.com/ps2/921272-ys-v-lost-kefin-kingdom-of-sand/answers/71872-help-with-getting-into-the-south-tower) (South Tower enterance requirements)
- Guide by [Markia](http://maturikasann.web.fc2.com/ys/5_ps2.html) (in Japanese)
- Guide by [Sugimo.](https://web.archive.org/web/20090922030050/http://homepage1.nifty.com:80/sugimo/falcom/ys/ys5guide2.htm) (archived, in Japanese)
- Review the game by [Kurt Kalata](http://www.hardcoregaming101.net/ys-v-ushinawareta-suna-no-miyako-kefin/) (includes review for original SFC game)
- Original game website from [Taito](https://web.archive.org/web/20070804063125/http://www.taito.co.jp/d3/cp/ys/ys5/) (archived)

# Special Thanks
- Everyone that supports me in my [Discord Server](https://discord.gg/TNWGBGpZGN)
- [Hilltop](https://x.com/HilltopWorks) - Providing valuable and informatative videos such as [hacking with Ghidra](https://youtu.be/qCEZC3cPc1s) and [info on PS2 graphics](https://youtu.be/lePKUCYakqM)
- [Life Bottle Productions](https://www.lifebottle.org/#/) - Providing me with their [isotool.py script](https://github.com/lifebottle/PythonLib/blob/main/isotool.py), their tutorial for [finding the base pointer](https://youtu.be/q5aEj-aSw50), and for having many supportive folks in their [Discord Server](https://discord.gg/rhQBXHKF3J)
- [The Geofront](https://geofront.esterior.net/) - Specifically folks on their [Discord Server](https://discord.gg/sXx2Ck6Cxn) for their continuing support
- [Evie](https://github.com/Epicpkmn11) - Helping with getting `graphics.py` working properly
- [PCSX2 Team](https://discord.com/invite/TCz3t9k) - Making the wonderful [PCSX2](https://pcsx2.net/) emulator and also providing the [texture alpha scaler](https://github.com/PCSX2/pcsx2/blob/master/tools/texture_dump_alpha_scaler.py)
- My friend for introducing me to the world of *Ys*, also the biggest Lost Kefin fan so I'm doing this for him
- Sugunii for giving me motivation to play more *Ys*
- Nihon Falcom for making the wonderful *Ys* series
