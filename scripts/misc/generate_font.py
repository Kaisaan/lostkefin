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
from pathlib import Path

WIDTH = 24
HEIGHT = 24
DATA_DIR = Path(__file__).parent.parent / "data"

FULLWIDTH_DIGITS = ["０", "１", "２", "３", "４", "５", "６", "７", "８", "９"]
FULLWIDTH_UPPERCASE = [
    "Ａ",
    "Ｂ",
    "Ｃ",
    "Ｄ",
    "Ｅ",
    "Ｆ",
    "Ｇ",
    "Ｈ",
    "Ｉ",
    "Ｊ",
    "Ｋ",
    "Ｌ",
    "Ｍ",
    "Ｎ",
    "Ｏ",
    "Ｐ",
    "Ｑ",
    "Ｒ",
    "Ｓ",
    "Ｔ",
    "Ｕ",
    "Ｖ",
    "Ｗ",
    "Ｘ",
    "Ｙ",
    "Ｚ",
]
FULLWIDTH_LOWERCASE = [
    "ａ",
    "ｂ",
    "ｃ",
    "ｄ",
    "ｅ",
    "ｆ",
    "ｇ",
    "ｈ",
    "ｉ",
    "ｊ",
    "ｋ",
    "ｌ",
    "ｍ",
    "ｎ",
    "ｏ",
    "ｐ",
    "ｑ",
    "ｒ",
    "ｓ",
    "ｔ",
    "ｕ",
    "ｖ",
    "ｗ",
    "ｘ",
    "ｙ",
    "ｚ",
]

# Fullwidth Unicode characters share a fixed offset from their ASCII equivalents (U+FF01 block)
FULLWIDTH_OFFSET = 0xFEE0


def fullwidth_to_ascii(char: str) -> str:
    return chr(ord(char) - FULLWIDTH_OFFSET)


# Indices where we use a custom PNG glyph instead of the TTF font
CUSTOM_GLYPH_DIR = DATA_DIR / "glyphs"
CUSTOM_GLYPH_INDICES = {
    int(os.path.splitext(f)[0])
    for f in os.listdir(CUSTOM_GLYPH_DIR)
    if f.endswith(".png") and os.path.splitext(f)[0].isdigit()
}


def load_mapping(mapping_path: str) -> list[str]:
    with open(mapping_path, "r", encoding="cp932") as f:
        lines = [line.rstrip("\n\r") for line in f.readlines()]
        # originally 1620 glyphs
        # Because we don't need 1000 kanji anymore I reclaim the space for code
        return lines[:201]


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
            "-size",
            f"{WIDTH}x{total_height}",
            "xc:transparent",
            "-font",
            ttf_path,
            "-pointsize",
            str(font_size),
        ]

        # First pass: draw black outline (black fill + black stroke)
        cmd.extend(["-fill", "black", "-stroke", "black", "-strokewidth", "2"])
        for index, char in enumerate(mapping):
            print(index, char)
            if index in CUSTOM_GLYPH_INDICES:
                continue  # Will be composited from PNG later
            if not char or char == " ":
                continue  # Skip empty/space - leave transparent
            if char in "[]":
                continue  # Brackets are invisible microspacing

            x_offset = 0
            # Fullwidth numbers
            if char in FULLWIDTH_DIGITS:
                char = fullwidth_to_ascii(char)
                if char in ["1", "2", "3", "5", "7"]:
                    x_offset = 8
                elif char in ["0", "4", "6", "8", "9"]:
                    x_offset = 7
            # Fullwidth uppercase
            elif char in FULLWIDTH_UPPERCASE:
                char = fullwidth_to_ascii(char)
            # Fullwidth lowercase
            elif char in FULLWIDTH_LOWERCASE:
                char = fullwidth_to_ascii(char)

            y_offset = (index * HEIGHT) - 5 + y_shift
            if char != '"':
                cmd.extend(["-draw", f'text {x_offset},{y_offset + HEIGHT} "{char}"'])
            else:
                cmd.extend(["-draw", f"text {x_offset},{y_offset + HEIGHT} '{char}'"])

        # Second pass: draw white text on top (white fill, no stroke)
        cmd.extend(["-fill", "white", "-stroke", "none"])
        for index, char in enumerate(mapping):
            if index in CUSTOM_GLYPH_INDICES:
                continue  # Will be composited from PNG later
            if not char or char == " ":
                continue  # Skip empty/space - leave transparent
            if char in "[]":
                continue  # Brackets are invisible microspacing

            x_offset = 0
            # Fullwidth numbers
            if char in FULLWIDTH_DIGITS:
                char = fullwidth_to_ascii(char)
                if char in ["1", "2", "3", "5", "7"]:
                    x_offset = 8
                elif char in ["0", "4", "6", "8", "9"]:
                    x_offset = 7
            # Fullwidth uppercase
            elif char in FULLWIDTH_UPPERCASE:
                char = fullwidth_to_ascii(char)
            # Fullwidth lowercase
            elif char in FULLWIDTH_LOWERCASE:
                char = fullwidth_to_ascii(char)

            y_offset = (index * HEIGHT) - 5 + y_shift
            if char != '"':
                cmd.extend(["-draw", f'text {x_offset},{y_offset + HEIGHT} "{char}"'])
            else:
                cmd.extend(["-draw", f"text {x_offset},{y_offset + HEIGHT} '{char}'"])

            if index % 500 == 0 and index > 0:
                print(f"  Added {index}/{len(mapping)} characters...")

        # Output to temp file
        cmd.append(temp_path)

        print("  Rendering atlas...")
        subprocess.run(cmd, check=True, capture_output=True)

        # Composite custom glyph PNGs onto the atlas
        for glyph_index in sorted(CUSTOM_GLYPH_INDICES):
            glyph_path = os.path.join(CUSTOM_GLYPH_DIR, f"{glyph_index}.png")
            if not os.path.exists(glyph_path):
                print(f"  WARNING: Custom glyph not found: {glyph_path}")
                continue
            y_offset = glyph_index * HEIGHT
            composite_cmd = [
                "magick",
                temp_path,
                glyph_path,
                "-geometry",
                f"+0+{y_offset}",
                "-geometry",
                f"+0+{y_offset}",
                "-composite",
                temp_path,
            ]
            print(f"  Compositing custom glyph {glyph_index} from {glyph_path}")
            subprocess.run(composite_cmd, check=True, capture_output=True)

        # Quantize to 16 colors with pngquant for consistent palette
        print("  Quantizing to 16 colors...")
        quant_cmd = [
            "pngquant",
            "16",
            "--quality",
            "1-99",
            "--output",
            output_path,
            "--force",  # Overwrite if exists
            temp_path,
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
            "-crop",
            f"{WIDTH}x{HEIGHT}+0+{y_offset}",
            "+repage",  # Reset virtual canvas
            # output_path,
            f"PNG8:{output_path}",  # Force PNG8 to preserve indexed palette
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

    mapping = load_mapping(mapping_path)

    generate_font_atlas(ttf_path, mapping, "font_atlas.png", font_size, y_shift)

    print(f"Done! Generated {len(mapping)} images to {output_dir}")


def main():
    parser = argparse.ArgumentParser(
        description="Generate 24x24px font images from a TTF font file"
    )
    parser.add_argument("ttf_path", help="Path to the TTF font file")
    parser.add_argument(
        "-m",
        "--mapping",
        default=str(DATA_DIR / "font_table.txt"),
        help="Path to font table (default: scripts/data/font_table.txt)",
    )
    parser.add_argument(
        "-o",
        "--output",
        default="font",
        help="Output directory for generated images (default: font)",
    )
    parser.add_argument(
        "-s", "--size", type=int, default=21, help="Font size in points (default: 24)"
    )
    parser.add_argument(
        "-y",
        "--y-shift",
        type=int,
        default=-1,
        help="Shift entire atlas up (-) or down (+) by N pixels (default: 0)",
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
