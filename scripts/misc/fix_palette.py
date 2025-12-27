# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "numpy",
#     "pillow",
# ]
# ///
"""
uv run scripts/misc/fix_palette.py ~/Downloads/3\ Processed/acc_name_5.png /tmp/acc_name_5.png
uv run scripts/misc/fix_palette.py ~/Downloads/3\ Processed/acc_name_6.png /tmp/acc_name_6.png
uv run scripts/misc/fix_palette.py ~/Downloads/3\ Processed/acc_name_7.png /tmp/acc_name_7.png
uv run scripts/misc/fix_palette.py ~/Downloads/3\ Processed/acc_name_8.png /tmp/acc_name_8.png
uv run scripts/misc/fix_palette.py ~/Downloads/3\ Processed/acc_name_9.png /tmp/acc_name_9.png
uv run scripts/misc/fix_palette.py ~/Downloads/3\ Processed/acc_name_10.png /tmp/acc_name_10.png
uv run scripts/misc/fix_palette.py ~/Downloads/3\ Processed/acc_name_11.png /tmp/acc_name_11.png
uv run scripts/misc/fix_palette.py ~/Downloads/3\ Processed/acc_name_12.png /tmp/acc_name_12.png
"""

import sys
from PIL import Image
import numpy as np


def remap_color_index(source_path, dest_path):
    """
    Load a color-indexed PNG, remap color 16 to color 0, and save.

    Args:
        source_path: Path to source PNG file
        dest_path: Path to destination PNG file
    """
    # Load the image
    img = Image.open(source_path)

    # Verify it's a palette (indexed) image
    if img.mode != 'P':
        raise ValueError(f"Image is not color-indexed (mode is {img.mode}, expected 'P')")

    # Convert to numpy array for easier manipulation
    pixels = np.array(img)

    # Remap: change all pixels with value 16 to value 0
    pixels[pixels == 16] = 0

    # Create new image from modified pixel data
    result = Image.fromarray(pixels, mode='P')

    # Copy the palette and transparency info from original
    result.putpalette(img.getpalette())
    if 'transparency' in img.info:
        result.info['transparency'] = img.info['transparency']

    # Save the result
    result.save(dest_path, 'PNG')
    print(f"Successfully remapped color 16 to 0: {source_path} -> {dest_path}")


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python remap_color.py <source.png> <dest.png>")
        sys.exit(1)

    source = sys.argv[1]
    dest = sys.argv[2]

    remap_color_index(source, dest)
