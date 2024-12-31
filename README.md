# Ys V: Lost Kefin - Kingdom of Sand (PS2) English Translation
Currently using Sam Farron's translation from his [Translation Series](https://www.youtube.com/watch?v=LfZZPwIdhzg&list=PLoD4gkRCJkUcgfpU5puBqYy5DX-RJK--b) with permission

# Building
- Copy the contents of the game's .iso into the `extracted` and `translated` folders
- Run `build.bat` or manually run the commands

# Hacking Notes
- The game uses SHIFT-JIS encoding for its text
- The game's base pointer is $FFF80
- Extracted .bin files with `_anm` in the filename are animation files with indexed 8BPP graphics and have the header `NAXA5010`
- Extracted .HGB files are texture files with 32BPP RGBA graphics
- Music files are `.hd` (header), `.bd` (header), and `.sq` (sequence) files

# Extracting the DATA.BIN Files
`extract.py` extracts all the files from DATA.BIN and its folders into a `DATA` folder but does not extract the files into their correct folders yet, a `logfile.txt` is also created for fixing issues with the script

# Font info
The game uses Shift-JIS encoding but I decided to make table files so I can include control codes  
`font.py` extracts the fontmap from `SLPM_663.60` to create a quick `font.tbl` table file. Use `kefin.tbl` for corrected values and control codes (also used by `patch.asm`)  
In `SLPM_663.60` the font is located at $1A3E90 as 4BPP graphics, its palette is stored at $25E4C0, and the fontmap is at $1A31F0  

# To do
- Updated extraction script to extract `DATA0.BIN`, `DATA1.BIN`, and `SLPM_663.60`
- Add more hacking notes (my notes.txt file is a mess so I haven't added it here)
- Continue inserting the English script

# Credits
- [Sam Farron](https://www.youtube.com/@samfarron) - Allowing me to use his translation as the basis of this project
- [Hilltop](https://x.com/HilltopWorks) - Providing valuable videos such as [hacking with Ghidra](https://youtu.be/qCEZC3cPc1s) and [PS1/PS2 graphics](https://youtu.be/lePKUCYakqM)
- [Life Bottle Productions](https://www.lifebottle.org/#/) - Providing me with their [isotool.py script](https://github.com/lifebottle/PythonLib/blob/main/isotool.py) and their tutorial for [finding the base pointer](https://youtu.be/q5aEj-aSw50)
- [The Geofront](https://geofront.esterior.net/) - Specifically folks on their [Discord Server](https://discord.gg/sXx2Ck6Cxn) for their support of this project
- My friend for introducing me to the world of *Ys*, also the biggest Lost Kefin fan so I'm doing this for him
- Sugunii for giving me motivation to play more *Ys*
- Falcom for making the wonderful *Ys* series
