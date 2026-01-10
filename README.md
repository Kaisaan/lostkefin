# Ys V: Lost Kefin - Kingdom of Sand (PS2) English Translation [SLPM-66360]
All the files and documentation for the translation of *Ys V: Lost Kefin, Kingdom of Sand* for the Playstation 2

# About The Translation Project 
**The patch is now available for public Beta Testing [Check it out!](https://github.com/Kaisaan/lostkefin/releases/latest) Be sure to report any issues!**
If you want to help please join the project's [Discord Server](https://discord.gg/TNWGBGpZGN).  
The translation is done with [Google Sheets](https://docs.google.com/spreadsheets/d/1kcEely3uIDJAifqj9kn16Bky8mBBoed03CgAwd4B0W8/edit?usp=sharing) and is automatically pulled from during building.

# Patching the Game
Extract the `Lost.Kefin.English.Beta.v01.zip` file from the [release page](https://github.com/Kaisaan/lostkefin/releases/latest).  
Read through the included text file for important information and apply the `.xdelta` to the game's ISO file.  
Use a tool like [DeltaPatcher](https://github.com/marco-calautti/DeltaPatcher) to ensure it is properly patched.

## ISO Info
I suggest following the [Disc Dumping guide by PCSX2's Team](https://pcsx2.net/docs/setup/discs) to get your ISO file.  
Your ISO file should match these sizes and hashes:  
Size: 2534080512 bytes : 2416 MiB  
CRC32: F290D71F  
CRC64: 754F35DCAD2D8F0E  
SHA256: de811d9a51d6422938ac5fc9994358e394e2c878b444a157ec9be962dc32f666  
SHA1: 8f8076ca2817e0260c9780e036ee8d91229b4057  
MD5: e8b38abbf526f12243636d6109d3cb05

# Roadmap

- Wait for more issues to be reported to be fixed
- Possibly change the font and add support for a Variable Width Font (VWF)
  - Most hacking has already been done
- Create maps and a guide for the game
  - Guide has already been translated and maps have been made
- Translate the games manual
  - Ideally get a better scan of the manual
- Add Empty Chest Messages

## Fixed Issues
These issues have been reported for [verison 0.1](https://github.com/Kaisaan/lostkefin/releases/tag/v0.1) of the beta release
- Fixed spacing for textboxes with 4 or 2 options
- Fixed certain highlights overlapping incorrectly
- Fixed boss name graphics not inserting
- Fixed response text ASCII not being updated
- Fixed chests staying closed after loading a quicksave
- Fixed certain character names not showing up in cutscenes (e.g "Young Girl A/B")
- Fixed names of bonus entries in the Galleries
- Various improvements to the translation


# Building
**Please use the above patching instructions to play the game! These instructions are only meant for project developers.**  
(requires a Google client secret file `lostkefin_secret.json`)
- [Python](https://www.python.org/) and [uv](https://docs.astral.sh/uv/) and [Pillow](https://python-pillow.github.io/) must be installed
- Copy the original game's .iso to the root and rename it as `lostkefin.iso`
- Run `1 Extract ISO.bat` (Windows) or `1 Extract ISO.sh` (Linux/Mac OS)
- Make changes to the .csv files in the `csv` folder or edit the project's Google Sheets
- To build from your local CSV files, run `2a Patch ISO from CSV.bat` (Windows) or `2a Patch ISO from CSV.sh` (Linux/Mac OS) (currently still pulls `strings.asm` from Google Sheets)
- To build from Google sheets, run `2b Patch ISO from sheets.bat` (Windows) or `2b Patch ISO from sheets.sh` (Linux/Mac OS) 

# Hacking Notes
- See [scriptFormat.md](https://github.com/Kaisaan/lostkefin/blob/main/scriptFormat.md) for all documented information about the game's script system
- See [kscript.md](https://github.com/Kaisaan/lostkefin/blob/main/kscript.md) for information about the kscript file format
- See [graphicsFormat.md](https://github.com/Kaisaan/lostkefin/blob/main/graphicsFormat.md) for all documented information about the game's graphics formats
- The game's base pointer is $FFF80 meaning all pointers in `SLPM_663.60` are calculated as `(True offset) + $FFF80`
- Music files are in PSF2 format in the form of `.hd` (header), `.bd` (header), and `.sq` (sequence) files
- See my [notes file](https://github.com/Kaisaan/lostkefin/blob/main/notes.txt) for more terribly organized notes

# Game Manual Translation
In the `manual` folder are scans for the game's manual. They were originally from [landofys.narod.ru](https://landofys.narod.ru/) which is now [landofys.com.ru](http://landofys.com.ru/) was scanned by Dragon.

# Contributors
A big thanks to these wonderful people for helping with this project! This project would not be possible without any of them.
- [Sam Farron](https://www.youtube.com/@samfarron) - Allowing me to use his translation as the basis of this project (even if I didn't end up using much in the end)
- [Everdred](https://github.com/cschmidt0121) - Programming, Hacking, Script development, helping with many technical issues
- [Josep](https://twitter.com/jdkluv?mx=1) ([Bluesky](https://bsky.app/profile/did:plc:6kukfqg2ly52abdqkouwbusp)) - Lead Translator
- [Etokapa](https://github.com/Etokapa/) - Text transcribing, making better batch files, making useful scripts, early testing, Graphics Editor
- [Seiichiro Mine](https://github.com/SeiichiroMine) - Translation Assistance, providing save files, making useful scripts
- [Sorcerian](https://bsky.app/profile/sorcerian.bsky.social) - Graphics Editing Assistance
- [Livi](https://bsky.app/profile/anonymusaxolotl.bsky.social) - Translation Editing Assistance
- Sabera - Translation Assistance
- Fishbone - Translation Assistance
- Sugunii - Early Testing

# Related Materials
A list of all webpages I could find that include information about this game. Please update me about anything that is not listed here.
- Article of the game on [Falcom Wiki](https://falcom.wiki/wiki/Ys_V:_Lost_Kefin,_Kingdom_of_Sand_(PS2))
- Article of the game on [Ys Wiki](https://isu.fandom.com/wiki/Ys_V:_Lost_Kefin,_Kingdom_of_Sand_(PS2))
- Article of the game on [Wikipedia](https://en.wikipedia.org/wiki/Ys_V:_Lost_Kefin,_Kingdom_of_Sand)
- Article of the game on [Wikipedia](https://ja.wikipedia.org/wiki/%E3%82%A4%E3%83%BC%E3%82%B9V)<sup>JP</sup>
- Translation of opening cutscene by [mziab](https://www.romhacking.net/forum/index.php?topic=28379.0) (I did not use this translation)
- Hacking attempt by [Hectavus](https://zenhax.com/viewtopic.php@t=15249.html) with only `SLPM_663.60` being translated
- Cheatcodes by [luc-ita](https://gamehacking.org/game/100384)
- Cheatcodes by GodShin: [Action Replay MAX](https://www.european-codebase.de/daten.php?system=ps2&act=detail1&id=8253), [Action Replay V2](https://www.european-codebase.de/daten.php?system=ps2&act=detail1&id=8252), [Xterminator/Xploder](https://www.european-codebase.de/daten.php?system=ps2&act=detail1&id=8251)<sup>DE</sup>
- Cheatcodes by [TOMBOY](https://blog.goo.ne.jp/touffu/e/c484169262662f0dd6632c97c6c695c7)<sup>JP</sup>
- Cheatcodes by [warezhunter_](https://psx-core.ru/forum/2-51-45)<sup>RU</sup>
- Cheatcodes by レインたんラブ [Part 1](https://jp.wazap.com/cheat/%E3%82%B3%E3%83%BC%E3%83%89/521993/) [Part 2](https://jp.wazap.com/cheat/%E3%82%B3%E3%83%BC%E3%83%89%EF%BC%92/522889/)
- Cheatcodes by 世界のマリオ [Original post](https://jp.wazap.com/cheat/%E5%85%A8%E3%82%A8%E3%83%AC%E3%83%A1%E3%83%B3%E3%83%88%EF%BC%99%EF%BC%99%EF%BC%99%EF%BC%99/434220/) [Archived page](https://web.archive.org/web/20150104205942/http://www17.ocn.ne.jp:80/~altcodex/ys5.htm)
- Guide by [Markia](http://maturikasann.web.fc2.com/ys/5_ps2.html)<sup>JP</sup>
  - English translation by [Josep](https://docs.google.com/document/d/1iiSjDg2WAXUBartzzL0PwSB3m9_QVdWjSBQ9JWr3b7A/)
- Guide by [VoidZankantou](https://gamefaqs.gamespot.com/ps2/921272-ys-v-lost-kefin-kingdom-of-sand/faqs/44007) (Incomplete)
- Guide addendum by [uncle5555](https://gamefaqs.gamespot.com/ps2/921272-ys-v-lost-kefin-kingdom-of-sand/answers/71872-help-with-getting-into-the-south-tower) (South Tower entrance requirements)
- Guide by [Sugimo](https://web.archive.org/web/20090922030050/http://homepage1.nifty.com:80/sugimo/falcom/ys/ys5guide2.htm)<sup>JP</sup> (Archived)
- Review the game by [Kurt Kalata](http://www.hardcoregaming101.net/ys-v-ushinawareta-suna-no-miyako-kefin/) (includes review for original SFC game)
- Original game website from [Taito](https://web.archive.org/web/20070804063125/http://www.taito.co.jp/d3/cp/ys/ys5/)<sup>JP</sup> (Archived)

# Special Thanks
- Everyone that supports me in my [Discord Server](https://discord.gg/TNWGBGpZGN)
- Everyone that supports me through my [Ko-fi](https://ko-fi.com/kaisaan)
- Everyone that supports me on [Bluesky](https://bsky.app/profile/kaisaan.bsky.social) and [Twitter](https://twitter.com/KaisaanSiddiqui)
- Everyone that has starred the [Github repo](https://github.com/Kaisaan/lostkefin)
- [Hilltop](https://x.com/HilltopWorks) - Providing valuable and informative videos such as [hacking with Ghidra](https://youtu.be/qCEZC3cPc1s) and [info on PS1 & PS2 graphics](https://youtu.be/lePKUCYakqM)
- [Life Bottle Productions](https://www.lifebottle.org/#/) - Creating their tutorial for [finding the base pointer](https://youtu.be/q5aEj-aSw50) and for having many supportive folks in their [Discord Server](https://discord.gg/rhQBXHKF3J)
- Ethanol - Creating the [isotool.py script](https://github.com/lifebottle/PythonLib/blob/main/isotool.py)
- [The Geofront](https://geofront.esterior.net/) - Specifically folks on their [Discord Server](https://discord.gg/sXx2Ck6Cxn) for their continual support
- [Evie](https://github.com/Epicpkmn11) - Helping with getting graphics extraction working properly
- [PCSX2 Team](https://discord.com/invite/TCz3t9k) - Making the wonderful [PCSX2](https://pcsx2.net/) emulator and also providing the [texture alpha scaler](https://github.com/PCSX2/pcsx2/blob/master/tools/texture_dump_alpha_scaler.py)
- [SnowyAria](https://bsky.app/profile/snowyaria.bsky.social) - Helping with patch creation
- [Eight Mansions Translations](https://github.com/Eight-Mansions) - Specifically folks in their [Discord Server](https://discord.gg/bewGNtm) for offering hacking assistance, advice, and support
- [Haroohie Translation Club](https://haroohie.club/) - Specifically folks in their [Discord Server](https://discord.gg/nesRSbpeFM) for offering hacking assistance, advice, and support
- Dragon for scanning the game's manual
- My friend Armaan for introducing me to the world of *Ys*, also the biggest Lost Kefin fan so I'm doing this for him
- Sugunii for giving me motivation to play more *Ys*
- Nihon Falcom for making the wonderful *Ys* series
