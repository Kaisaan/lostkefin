import os
import sys
from pathlib import Path
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

    def rotate_column(self, amount: int):
        """
        Shift right by amount pixels. The rightmost column "rotates" to the leftmost column.
        """
        amount = amount % WIDTH
        if amount == 0:
            return

        new_pixels = []
        for row in range(HEIGHT):
            row_start = row * WIDTH
            row_pixels = self.pixels[row_start:row_start + WIDTH]
            rotated_row = row_pixels[-amount:] + row_pixels[:-amount]
            new_pixels.extend(rotated_row)

        self.pixels = new_pixels

    @classmethod
    def from_bytes(cls, some_bytes: bytes, palette: list[int]):
        if len(some_bytes) != (WIDTH * HEIGHT) // 2:
            raise ValueError(f"Bytes length must be {(WIDTH * HEIGHT) // 2}. Got {len(some_bytes)}.")

        pixels = []
        for byte in some_bytes:
            pixels.append(byte & 0xF)
            pixels.append(byte >> 4)
        return cls(palette, pixels)

    def to_png(self, path: str):
        image = Image.new("P", (WIDTH, HEIGHT))
        clut = [component for color in self.palette for component in color]
        image.putpalette(clut, rawmode="RGBA")
        image.putdata(self.pixels)
        image.save(path)


def dump_font(slpm_path: str = "extracted/SLPM_663.60", output_dir: str = "font"):
    """
    Dump the game font from the SLPM file to individual PNG files.

    Args:
        slpm_path: Path to the SLPM_663.60 file
        output_dir: Directory to save the font PNGs
    """
    slpm_path = Path(slpm_path)
    output_dir = Path(output_dir)

    if not slpm_path.exists():
        sys.exit(f"Error: {slpm_path} not found")

    output_dir.mkdir(parents=True, exist_ok=True)

    with open(slpm_path, "rb") as f:
        f.seek(CLUT_OFFSET)
        clut = list(f.read(16 * 4))
        palette = [clut[i:i+4] for i in range(0, len(clut), 4)]

        f.seek(PIXEL_OFFSET)
        for i in range(GLYPH_COUNT):
            glyph = Glyph.from_bytes(f.read(WIDTH * HEIGHT // 2), palette)
            if i in (46, 52, -1):
                glyph.rotate_column(2)
            elif i < 87:
                glyph.rotate_column(1)
            glyph.to_png(str(output_dir / f"{i}.png"))

    print(f"Dumped {GLYPH_COUNT} glyphs to {output_dir}")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        dump_font()
    elif len(sys.argv) == 2:
        dump_font(sys.argv[1])
    elif len(sys.argv) == 3:
        dump_font(sys.argv[1], sys.argv[2])
    else:
        print("Usage: python dump_font.py [slpm_path] [output_dir]")
        sys.exit(1)

