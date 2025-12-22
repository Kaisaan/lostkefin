import sys
from pathlib import Path
from PIL import Image


WIDTH = 24
HEIGHT = 24
PIXEL_OFFSET = 0x1A3EA0
CLUT_OFFSET = 0x25E4C0
GLYPH_COUNT = 1620


class Glyph:
    def __init__(self, palette: list[list[int]], pixels: list[int]):
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
    def from_png(cls, image: Image.Image):
        if image.size != (WIDTH, HEIGHT):
            raise ValueError(f"Image size must be {WIDTH}x{HEIGHT}")

        rgb_palette = image.getpalette()
        transparency = image.info.get('transparency', b'')

        palette = []
        num_colors = 16
        for i in range(num_colors):
            color = []
            if i >= (len(rgb_palette) // 3):
                color.append(0)
                color.append(0)
                color.append(128)
                palette.append(color)
                continue

            color.append(rgb_palette[i * 3])
            color.append(rgb_palette[i * 3 + 1])
            color.append(rgb_palette[i * 3 + 2])

            if transparency == 0:
                alpha = 128
            else:
                if i < len(transparency):
                    alpha = int(transparency[i] // 1.5)
                else:
                    alpha = 128
            if alpha == 127 or alpha > 128:
                alpha = 128

            color.append(alpha)
            palette.append(color)

        return cls(palette, list(image.getdata()))

    def to_bytes(self) -> bytes:
        result = b""
        for i in range(0, len(self.pixels), 2):
            p1 = self.pixels[i]
            p2 = self.pixels[i + 1]
            result += int.to_bytes((p2 << 4) | (p1 & 0xF), 1)
        return result


def patch_font(font_dir: str = "font", slpm_path: str = "translated/SLPM_663.60"):
    """
    Patch the game font from individual PNG files back into the SLPM file.

    Args:
        font_dir: Directory containing the font PNGs (0.png, 1.png, etc.)
        slpm_path: Path to the SLPM_663.60 file to patch
    """
    font_dir = Path(font_dir)
    slpm_path = Path(slpm_path)

    if not slpm_path.exists():
        sys.exit(f"Error: {slpm_path} not found")

    if not font_dir.exists():
        sys.exit(f"Error: {font_dir} not found")

    # Copy all PNG files from font_modifications/ into font_dir
    modifications_dir = Path("font_modifications")
    prev_palette = None

    with open(slpm_path, "r+b") as slpm:
        for i in range(GLYPH_COUNT):
            # Check if a modified glyph exists, otherwise use the base font
            mod_path = modifications_dir / f"{i}.png"
            if mod_path.exists():
                png_path = mod_path
            else:
                png_path = font_dir / f"{i}.png"
                if not png_path.exists():
                    sys.exit(f"Error: {png_path} not found")

            image = Image.open(png_path)
            glyph = Glyph.from_png(image)
            print(f"Glyph {i} palette: {glyph.palette}")

            if prev_palette is not None and prev_palette != glyph.palette:
                print(f"Previous palette: {prev_palette}")
                print(f"Current palette: {glyph.palette}")
                sys.exit("Error: Replacement glyphs have >1 palette")
            prev_palette = glyph.palette

            if i == 0:
                # Write the palette once at the start
                slpm.seek(CLUT_OFFSET)
                print(f"Palette: {glyph.palette}")
                palette_bytes = bytes([component for color in glyph.palette for component in color])
                slpm.write(palette_bytes)

            # Write the glyph pixels
            slpm.seek(PIXEL_OFFSET + i * (WIDTH * HEIGHT // 2))
            slpm.write(glyph.to_bytes())

    print(f"Patched {GLYPH_COUNT} glyphs from {font_dir} into {slpm_path}")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        patch_font()
    elif len(sys.argv) == 2:
        patch_font(sys.argv[1])
    elif len(sys.argv) == 3:
        patch_font(sys.argv[1], sys.argv[2])
    else:
        print("Usage: python patch_font.py [font_dir] [slpm_path]")
        sys.exit(1)

