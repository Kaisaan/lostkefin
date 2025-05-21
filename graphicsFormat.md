# Graphics Formats

*Ys V: Lost Kefin - Kingdom of Sand* uses unique file formats for different graphics.

# HGK Files

3D Model files?

# HGB Files

Textures for 3D models. 2-dimensional, 32BPP (RGBA8888) encoded.

# Animation Files

`.bin` files whose filenames end with `_anm`.

|Offset|Description|
|---|---|
|$00-$07|Always `4E 41 58 41 35 30 31 30` or `NAXA5010` in ASCII|
|$08-$0B|Palette size (In little Endian), usually either $10 or $100|
|$0C-$0F|Always `$20000000`|
|$10-$13|Offset to PXL Data (in little Endian)|
|$14-$17|Offset to Unknown Data (in little Endian)|
|$18-$1B|Unknown|
|$1C-$1F|Always `$00000000`|
|$20-$20+Palette Size|Palette as RGBA8888 format|
|Unknown Data offset to PXL Data offset-$1|Unknown Data|
|PXL Data Offset to End of File|PXL Data using indexed palette data|