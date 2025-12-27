# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "numpy",
#     "pillow",
# ]
# ///
"""
Fix palette indices in a processed image to match the original's palette.

This script takes pixel data from a processed image and remaps the palette indices
so that each color value uses the same index as in the original image's palette.
"""

from PIL import Image
import numpy as np
import sys

"""
uv run scripts/misc/fix_palette.py ./graphics/orig/acc_name/acc_name_5.png ~/Downloads/3\ Processed/acc_name_5.png /tmp/acc_name_5.png
uv run scripts/misc/fix_palette.py ./graphics/orig/acc_name/acc_name_6.png ~/Downloads/3\ Processed/acc_name_6.png /tmp/acc_name_6.png
uv run scripts/misc/fix_palette.py ./graphics/orig/acc_name/acc_name_7.png ~/Downloads/3\ Processed/acc_name_7.png /tmp/acc_name_7.png
uv run scripts/misc/fix_palette.py ./graphics/orig/acc_name/acc_name_8.png ~/Downloads/3\ Processed/acc_name_8.png /tmp/acc_name_8.png
uv run scripts/misc/fix_palette.py ./graphics/orig/acc_name/acc_name_9.png ~/Downloads/3\ Processed/acc_name_9.png /tmp/acc_name_9.png
uv run scripts/misc/fix_palette.py ./graphics/orig/acc_name/acc_name_10.png ~/Downloads/3\ Processed/acc_name_10.png /tmp/acc_name_10.png
uv run scripts/misc/fix_palette.py ./graphics/orig/acc_name/acc_name_11.png ~/Downloads/3\ Processed/acc_name_11.png /tmp/acc_name_11.png
uv run scripts/misc/fix_palette.py ./graphics/orig/acc_name/acc_name_12.png ~/Downloads/3\ Processed/acc_name_12.png /tmp/acc_name_12.png
"""


def fix_palette_indices(orig_path, processed_path, output_path):
    """
    Remap processed image indices to use original's palette structure.

    Args:
        orig_path: Path to original image with reference palette
        processed_path: Path to processed image to remap
        output_path: Path to save the remapped image
    """
    # Load images
    orig_img = Image.open(orig_path)
    proc_img = Image.open(processed_path)

    if orig_img.mode != 'P' or proc_img.mode != 'P':
        print(f"Error: Both images must be in palette mode (P)")
        print(f"  Original mode: {orig_img.mode}")
        print(f"  Processed mode: {proc_img.mode}")
        sys.exit(1)

    # Get palettes
    orig_palette = orig_img.getpalette()
    proc_palette = proc_img.getpalette()

    # Build color-to-index mapping for original palette
    orig_color_to_index = {}
    for i in range(len(orig_palette) // 3):
        r = orig_palette[i * 3]
        g = orig_palette[i * 3 + 1]
        b = orig_palette[i * 3 + 2]
        color = (r, g, b)
        # Use first occurrence of each color
        if color not in orig_color_to_index:
            orig_color_to_index[color] = i

    # Build remapping table: processed index -> original index
    remap = {}
    proc_data = np.array(proc_img)
    unique_indices = np.unique(proc_data)

    print(f"Building index remapping table...")
    for proc_idx in unique_indices:
        # Get color from processed palette
        r = proc_palette[proc_idx * 3]
        g = proc_palette[proc_idx * 3 + 1]
        b = proc_palette[proc_idx * 3 + 2]
        color = (r, g, b)

        # Find matching color in original palette
        if color in orig_color_to_index:
            orig_idx = orig_color_to_index[color]
            remap[proc_idx] = orig_idx
            print(f"  {proc_idx:3d} -> {orig_idx:3d}  RGB{color}")
        else:
            print(f"  Warning: Color RGB{color} at index {proc_idx} not found in original palette")
            print(f"           Keeping index {proc_idx} unchanged")
            remap[proc_idx] = proc_idx

    # Apply remapping to pixel data
    print(f"\nRemapping pixel data...")
    output_data = np.copy(proc_data)
    for old_idx, new_idx in remap.items():
        output_data[proc_data == old_idx] = new_idx

    # Create output image with original palette
    output_img = Image.fromarray(output_data, mode='P')
    output_img.putpalette(orig_palette)

    # Save
    output_img.save(output_path)
    print(f"\nSaved to: {output_path}")
    print(f"  Size: {output_img.size}")
    print(f"  Mode: {output_img.mode}")
    print(f"  Unique indices used: {len(np.unique(output_data))}")


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: fix_palette.py <original.png> <processed.png> <output.png>")
        print()
        print("Remaps processed image indices to match original's palette structure.")
        sys.exit(1)

    orig_path = sys.argv[1]
    processed_path = sys.argv[2]
    output_path = sys.argv[3]

    fix_palette_indices(orig_path, processed_path, output_path)
