# Graphics Formats

*Ys V: Lost Kefin - Kingdom of Sand* uses unique file formats for different graphics.  

**Note: All values are stored in Little Endian unless otherwise specified.**

# HGK Files

3D Model files?

# HGB Files

Textures for 3D models. 2-dimensional, 32BPP (RGBA8888) encoded.

# Sprite Files

`.bin` files whose filenames end with `_anm`.  
`graphics.py` can be used to extract all sprites from a given file.  
Use [texture_dump_alpha_scaler.py](https://github.com/PCSX2/pcsx2/blob/master/tools/texture_dump_alpha_scaler.py) to scale/unscale the transparency of the extracted images.

## Header

The `NAXA5010` file header indicates that it is a sprite file.

|Offset|Description|
|---|---|
|$00-$07|Always `4E 41 58 41 35 30 31 30` or `NAXA5010` in ASCII|
|$08-$0B|Palette size , either $10 or $100|
|$0C-$0F|Palette Data offset, always `$20000000`|
|$10-$13|Offset to Image Data|
|$14-$17|Offset to Animation Data|
|$18-$19|Unknown, sometimes matches Image Width|
|$1A-$1B|Unknown, sometimes matches Image Height|
|$1C-$1F|Unknown, always `$00000000`|

## Palette

The Palette (or CLUT) data always starts at $20 in the file and is either $10 colours or $100 colours. Each colour is 32 bits in RGBA8 format.  
The size of the palette determines if the image data is either 4 bits per pixel or 8 bits per pixel respectively.  
**The Palette data is Swizzled**

## Animation Data

I don't understand yet how this data is used but there are some patterns that emerge when comparing different files.

### Header

The animation data starts with an info for the number of entries each file has.  

|Size|Description|
|---|---|
|$4|Number of entries |
|$4|Entry offset , calculated as (Animation Data Offest + Entry Offset)|

The header is padded with `FF FF FF FF`.

### Entry

Entries can have multiple frames

|Size|Description|
|---|---|
|$10|Number of frames|
|$60|Size of each frame info|

### Frames

Frames are also used for static images.

|Size|Description|
|---|---|
|$4|Frame length (in frames)|
|$2|Usually set to `$01`, image will appear|
|$2|Image Index number|
|$2|Horizontal offset|
|$2|Vertical offset|
|$4|Unknown value again|

The rest of each frame is usually empty and padded to be a total of $60 bytes.

## Image Data

The image data is $10 bytes long per image. It is located based on the offset in the file header. They are formatted as follows:  
|Size|Description|
|---|---|
|$2|Image Width in-game?|
|$2|Image Height in-game?|
|$2|Image Data Width|
|$2|Image Data Height|
|$4|Image Offset, calculated as (Image Data Offset + Image Offset)|
|$4|Image Index|

## Images

Images are indexed on the palette info.  
The size (in bytes) of each image's data is Image Data Width * Image Data Height