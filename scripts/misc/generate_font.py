#!/usr/bin/env python3
"""
Generate 24x24px font images from a TTF font file.
Creates a unified atlas first for consistent palette, then splits into individual files.
"""

import argparse
import json
import os
import subprocess
import tempfile

WIDTH = 24
HEIGHT = 24

def load_mapping(mapping_path: str)  -> list[str]:
    with open(mapping_path, "r", encoding="cp932") as f:
        lines =  [line.rstrip('\n\r') for line in f.readlines()]
        return lines


def generate_font_atlas(
    ttf_path: str,
    mapping: list[str],
    output_path: str,
    font_size: int = 24,
    y_shift: int = 0,
):
    """Generate a single vertical font atlas with all characters."""
    total_height = HEIGHT * len(mapping)
    
    print(f"Generating font atlas with {len(mapping)} characters...")
    print(f"  Atlas size: {WIDTH}x{total_height}px")
    print(os.path.isdir(output_path))

    
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp:
        temp_path = tmp.name
    
    try:
        # Build ImageMagick command to create the full atlas
        # Start with a transparent canvas of the full size
        cmd = [
            "magick",
            "-size", f"{WIDTH}x{total_height}",
            "xc:transparent",
            "-font", ttf_path,
            "-pointsize", str(font_size),
        ]

        # First pass: draw black outline (black fill + black stroke)
        cmd.extend(["-fill", "black", "-stroke", "black", "-strokewidth", "2"])
        for index, char in enumerate(mapping):
            if not char or char == " ":
                continue  # Skip empty/space - leave transparent

            y_offset = (index * HEIGHT) - 5 + y_shift
            if char != '"':
                cmd.extend(["-draw", f'text 0,{y_offset+HEIGHT} "{char}"'])
            else:
                cmd.extend(["-draw", f"text 0,{y_offset+HEIGHT} '{char}'"])

        # Second pass: draw white text on top (white fill, no stroke)
        cmd.extend(["-fill", "white", "-stroke", "none"])
        for index, char in enumerate(mapping):
            if not char or char == " ":
                continue  # Skip empty/space - leave transparent

            y_offset = (index * HEIGHT) - 5 + y_shift
            if char != '"':
                cmd.extend(["-draw", f'text 0,{y_offset+HEIGHT} "{char}"'])
            else:
                cmd.extend(["-draw", f"text 0,{y_offset+HEIGHT} '{char}'"])

            if index % 500 == 0 and index > 0:
                print(f"  Added {index}/{len(mapping)} characters...")
            if index == 1:
                print(cmd)
            if char == "…":
                print(index)
        
        # Output to temp file
        cmd.append(temp_path)
        
        print("  Rendering atlas...")
        subprocess.run(cmd, check=True, capture_output=True)

        # Quantize to 16 colors with pngquant for consistent palette
        print("  Quantizing to 16 colors...")
        quant_cmd = [
            "pngquant", "16",
            "--quality", "1-99",
            "--output", output_path,
            "--force",  # Overwrite if exists
            temp_path 
        ]
        subprocess.run(quant_cmd, check=True)
        
    finally:
        if os.path.exists(temp_path):
            os.unlink(temp_path)
    
    print(f"  Atlas saved: {output_path}")


def split_atlas(atlas_path: str, output_dir: str, num_chars: int):
    """Split a vertical atlas into individual 24x24 PNG files, preserving palette."""
    os.makedirs(output_dir, exist_ok=True)
    
    print(f"Splitting atlas into {num_chars} images...")
    
    for index in range(num_chars):
        y_offset = index * HEIGHT
        output_path = os.path.join(output_dir, f"{index}.png")
        
        # Use ImageMagick to crop each character, preserving the indexed palette
        cmd = [
            "magick",
            atlas_path,
            "-crop", f"{WIDTH}x{HEIGHT}+0+{y_offset}",
            "+repage",  # Reset virtual canvas
            #output_path,
            f"PNG8:{output_path}"  # Force PNG8 to preserve indexed palette
        ]
        subprocess.run(cmd, check=True, capture_output=False)
        
        if index % 100 == 0:
            print(f"  Split {index}/{num_chars}...")
    
    print(f"  Split complete: {output_dir}")


def generate_font_images(
    ttf_path: str,
    mapping_path: str,
    output_dir: str,
    font_size: int = 20,
    y_shift: int = 0,
):
    """Generate font images for all characters in the mapping."""
    os.makedirs(output_dir, exist_ok=True)

    mapping = load_mapping("/Users/cschmidt/git/lostkefin/font_table.txt")

    generate_font_atlas(ttf_path, mapping, "font_atlas.png", font_size, y_shift)

    
    print(f"Done! Generated {len(mapping)} images to {output_dir}")


def main():
    parser = argparse.ArgumentParser(
        description="Generate 24x24px font images from a TTF font file"
    )
    parser.add_argument(
        "ttf_path",
        help="Path to the TTF font file"
    )
    parser.add_argument(
        "-m", "--mapping",
        default="scripts/misc/mapping.json",
        help="Path to mapping.json (default: scripts/misc/mapping.json)"
    )
    parser.add_argument(
        "-o", "--output",
        default="font",
        help="Output directory for generated images (default: font)"
    )
    parser.add_argument(
        "-s", "--size",
        type=int,
        default=24,
        help="Font size in points (default: 24)"
    )
    parser.add_argument(
        "-y", "--y-shift",
        type=int,
        default=0,
        help="Shift entire atlas up (-) or down (+) by N pixels (default: 0)"
    )

    args = parser.parse_args()
    
    generate_font_images(
        ttf_path=args.ttf_path,
        mapping_path=args.mapping,
        output_dir=args.output,
        font_size=args.size,
        y_shift=args.y_shift,
    )


if __name__ == "__main__":
    main()
