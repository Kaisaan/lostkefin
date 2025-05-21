# Graphics Formats

*Ys V: Lost Kefin - Kingdom of Sand* uses unique file formats for different graphics.

# HGK Files

3D Model files?

# HGB Files

Textures for 3D models. 2-dimensional, 32BPP (RGBA8888) encoded.

# Sprite Files

`.bin` files whose filenames end with `_anm`.

## Header

The `NAXA5010` file header indicates that it is a sprite file.

|Offset|Description|
|---|---|
|$00-$07|Always `4E 41 58 41 35 30 31 30` or `NAXA5010` in ASCII|
|$08-$0B|Palette size (In little Endian), either $10 or $100|
|$0C-$0F|Palette Data offset, always `$20000000`|
|$10-$13|Offset to Image Data (in little Endian)|
|$14-$17|Offset to Unknown Data (in little Endian)|
|$18-$1B|Unknown|
|$1C-$1F|Unknown, always `$00000000`|

## Palette

The Palette (or CLUT) data always starts at $20 in the file and is either $10 colours or $100 colours. Each colour is 32 bits in RGBA8 format.  
The size of the palette determines if the image data is either 4-bits or 8-bits respectively

## Unknown Data

The unknown data usually starts with some file offsets. Most of this data is empty.

## Image Data

The image data is $10 bytes long per image. It is located based on the offset in the file header. They are formatted as follows:  
|Size|Description|
|---|---|
|$2|Image Width (In little Endian)|
|$2|Image Height (In little Endian)|
|$2|Image Width repeated?|
|$2|Image Height repeated?|
|$4|Image Offset (In little Endian), calculated at (Image Data Offset + Image Offset)|
|$4|Image Index|

## Images

Images are based on the palette info.