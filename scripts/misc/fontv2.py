import sys
from PIL import Image

WIDTH = 24
HEIGHT = 24
PIXEL_OFFSET = 0x1A3EA0
CLUT_OFFSET = 0x25E4C0
GLYPH_COUNT = 1620


class Glyph:
    def __init__(self, palette: list[int], pixels: list[int]):
        self.palette = palette
        self.pixels = pixels

    @classmethod
    def from_bytes(cls, some_bytes: bytes, palette: list[int]):
        if len(some_bytes) != (WIDTH * HEIGHT) // 2:
            raise ValueError(f"Bytes length must be {(WIDTH * HEIGHT) // 2}. Got {len(some_bytes)}.")

        pixels = []
        for byte in some_bytes: 
            # 4 bits per pixel
            pixels.append(byte & 0xF)
            pixels.append(byte >> 4)
        return cls(palette, pixels)

    @classmethod
    def from_png(cls, image: Image.Image):
        if image.size != (WIDTH, HEIGHT):
            raise ValueError(f"Image size must be {WIDTH}x{HEIGHT}")
        
        # Get RGB palette and combine with transparency info (tRNS chunk)
        rgb_palette = image.getpalette()  # Returns RGB values
        transparency = image.info.get('transparency', b'')
        
        # Build RGBA palette by interleaving RGB with alpha from transparency
        # Only read 16 colors (4-bit palette)
        palette = []
        num_colors = 16
        for i in range(num_colors):
            color = []
            if i >= (len(rgb_palette) // 3):
                color.append(0)
                color.append(0)
                color.append(128)
                continue

            color.append(rgb_palette[i * 3])      # R
            color.append(rgb_palette[i * 3 + 1])  # G
            color.append(rgb_palette[i * 3 + 2])  # B
            # Get alpha from transparency chunk, default to 255 if not present
            
            if transparency == 0:
                alpha = 128
            else:
                if i < len(transparency):
                    alpha = int(transparency[i]//1.5)
                else:
                    alpha = 128
            if alpha == 127 or alpha > 128:
                alpha = 128

            color.append(alpha)
            palette.append(color)

        
        return cls(palette, list(image.getdata())) 


    def to_bytes(self) -> bytes:
        bytes = b""
        for i in range(0, len(self.pixels), 2):
            p1 = self.pixels[i]
            p2 = self.pixels[i + 1]
            bytes += int.to_bytes((p2 << 4) | (p1 & 0xF), 1)
        return bytes

    def to_png(self, path: str):
        image = Image.new("P", (WIDTH, HEIGHT))
        # Flatten the palette (list of 4-int lists) into a flat list of ints
        clut = [component for color in self.palette for component in color]
        image.putpalette(clut, rawmode="RGBA")
        image.putdata(self.pixels)
        image.save(path)


def dump_font():
    with open("extracted/SLPM_663.60", "rb") as f:
        f.seek(CLUT_OFFSET)
        clut = list(f.read(16 * 4))
        palette = [clut[i:i+4] for i in range(0, len(clut), 4)]
        f.seek(PIXEL_OFFSET)
        for i in range(GLYPH_COUNT):
            glyph = Glyph.from_bytes(f.read(WIDTH * HEIGHT // 2), palette)
            glyph.to_png(f"font/{i}.png")

def patch_font():
    with open("extracted/SLPM_663.60", "r+b") as f:

        prev_palette = []
        for i in range(GLYPH_COUNT):
            atlas = Image.open("font_atlas.png")

            slice = atlas.crop((0, i * HEIGHT, WIDTH, (i + 1) * HEIGHT))
            glyph = Glyph.from_png(slice)
            if prev_palette and prev_palette != glyph.palette:
                print(f"Previous palette: {prev_palette}")
                print(f"Current palette: {glyph.palette}")
                sys.exit("Palette changed")
            prev_palette = glyph.palette

            if i == 0:
                f.seek(CLUT_OFFSET)
                f.write(bytes([component for color in glyph.palette for component in color]))
                f.seek(PIXEL_OFFSET)
                
            f.write(glyph.to_bytes())

def test_roundtrip():
    import tempfile
    import os

    with open("extracted/SLPM_663.60", "rb") as f:
        f.seek(CLUT_OFFSET)
        clut = list(f.read(16 * 4))
        f.seek(PIXEL_OFFSET)
        original_bytes = f.read(WIDTH * HEIGHT // 2)

    glyph = Glyph.from_bytes(original_bytes, clut)

    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp:
        tmp_path = tmp.name

    try:
        glyph.to_png(tmp_path)
        new_glyph = Glyph.from_png(tmp_path)
        assert new_glyph.to_bytes() == original_bytes, "Roundtrip failed: bytes don't match"
        assert new_glyph.clut == clut, f"Roundtrip failed: clut doesn't match. Got {new_glyph.clut} expected {clut}"
        print("Test passed: roundtrip bytes match")
    finally:
        os.unlink(tmp_path)


if __name__ == "__main__":
    #dump_font()
    patch_font()

    #test_roundtrip()