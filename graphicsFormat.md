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
|$18-$19|Unknown, sometimes matches Image Width|
|$1A-$1B|Unknown, sometimes matches Image Height|
|$1C-$1F|Unknown, always `$00000000`|

## Palette

The Palette (or CLUT) data always starts at $20 in the file and is either $10 colours or $100 colours. Each colour is 32 bits in RGBA8 format.  
The size of the palette determines if the image data is either 4-bits or 8-bits respectively

## Unknown Data

I don't understand yet how this data is used but there are some patterns that emerge when comparing different files.

### Header

The unknown data starts with an info for the number of entries each file has.  

|Size|Description|
|---|---|
|$4|Number of entries (in little Endian)|
|$4|Entry offset (in little Endian), calculated as (Unknown Data Offest + Entry Offset)|

The header is padded with `FF FF FF FF`.

### Entry

Entries can have multiple frames? I'm not sure what each of these items in each entry are so I am calling them "frames" for now.

|Size|Description|
|---|---|
|$10|Number of frames|
|$60|Size of each frame info|

### Frames

Again, not sure what these are but they seem to have a format. It's not very consistent across files though.

|Size|Description|
|---|---|
|$4|Some value? Usually less than $10 in smaller files|
|$2|Another value? Usually less than the previous value|
|$2|Another unknown Value that is somtimes used|
|$4|Unknown value, when not empty is usually larger than `$FF000000` (in little endian)|
|$4|Unknown value again|

The rest of each frame is usually empty and padded to be a total of $60 bytes.


## Image Data

The image data is $10 bytes long per image. It is located based on the offset in the file header. They are formatted as follows:  
|Size|Description|
|---|---|
|$2|Image Width (In little Endian)|
|$2|Image Height (In little Endian)|
|$2|Image Width repeated?|
|$2|Image Height repeated?|
|$4|Image Offset (In little Endian), calculated as (Image Data Offset + Image Offset)|
|$4|Image Index|

## Images

Images are based on the palette info.