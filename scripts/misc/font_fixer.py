#!/usr/bin/env python3
"""
Font Fixer - Combines font glyphs, runs pngquant, and slices back.

1. Lays out every glyph PNG from font/ into one large PNG
2. Runs pngquant on the combined image
3. Slices back into individual glyph PNGs and saves to converted/
"""

import os
import subprocess
import sys
import tempfile
from pathlib import Path
from PIL import Image


GLYPH_WIDTH = 24
GLYPH_HEIGHT = 24
GLYPH_COUNT = 1620

# Use a grid layout for better image dimensions
GRID_COLS = 45  # 1620 / 45 = 36 rows


def get_font_files(font_dir: Path) -> list[Path]:
    """Get all font PNG files sorted numerically."""
    files = []
    for i in range(GLYPH_COUNT):
        png_path = font_dir / f"{i}.png"
        if not png_path.exists():
            sys.exit(f"Error: Missing glyph file {png_path}")
        files.append(png_path)
    return files

def replacement_exists(png_path: Path) -> bool:

    filename = png_path.name
    font_modifications_dir = Path("font_modifications")
    custom_path = font_modifications_dir / filename
    return custom_path.exists()

def combine_glyphs(font_dir: Path, output_path: Path) -> None:
    """Combine all glyph PNGs into one large PNG in a grid layout."""
    print(f"Combining {GLYPH_COUNT} glyphs from {font_dir}...")
    
    font_files = get_font_files(font_dir)
    
    rows = (GLYPH_COUNT + GRID_COLS - 1) // GRID_COLS
    combined_width = GRID_COLS * GLYPH_WIDTH
    combined_height = rows * GLYPH_HEIGHT
    
    combined = Image.new("RGBA", (combined_width, combined_height))
    
    for i, png_path in enumerate(font_files):
        if replacement_exists(png_path):
            filename = png_path.name
            font_modifications_dir = Path("font_modifications")
            custom_path = font_modifications_dir / filename
            print(f"Using replacement for {filename}")
            img = Image.open(custom_path)
            
        else:
            img = Image.open(png_path)
            transparency = img.info.get('transparency')

            new_transparency = bytes(min(255, a * 2) for a in transparency)
            img.info['transparency'] = new_transparency

            
        
        col = i % GRID_COLS
        row = i // GRID_COLS
        x = col * GLYPH_WIDTH
        y = row * GLYPH_HEIGHT
        
        combined.paste(img, (x, y))
    
    combined.save(output_path)
    print(f"Combined image saved to {output_path} ({combined_width}x{combined_height})")


def run_pngquant(input_path: Path, output_path: Path) -> None:
    """Run pngquant on the combined image."""
    print(f"Running pngquant on {input_path}...")
    
    cmd = [
        "pngquant",
        "16",
        "--quality", "1-90",
        "--output", str(output_path),
        "--force",
        str(input_path)
    ]
    
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(f"pngquant completed successfully")
    except subprocess.CalledProcessError as e:
        print(f"pngquant stderr: {e.stderr}")
        sys.exit(f"Error running pngquant: {e}")
    except FileNotFoundError:
        sys.exit("Error: pngquant not found. Please install pngquant.")


def slice_glyphs(combined_path: Path, output_dir: Path) -> None:
    """Slice the combined image back into individual glyph PNGs."""
    print(f"Slicing combined image into individual glyphs...")
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    combined = Image.open(combined_path)
    
    for i in range(GLYPH_COUNT):
        col = i % GRID_COLS
        row = i // GRID_COLS
        x = col * GLYPH_WIDTH
        y = row * GLYPH_HEIGHT
        
        glyph = combined.crop((x, y, x + GLYPH_WIDTH, y + GLYPH_HEIGHT))
        output_path = output_dir / f"{i}.png"
        glyph.save(output_path)
    
    print(f"Saved {GLYPH_COUNT} glyphs to {output_dir}")


def main():
    # Get the project root (parent of scripts/)
    script_dir = Path(__file__).parent
    project_root = script_dir.parent.parent
    
    font_dir = project_root / "font"
    output_dir = project_root / "converted"
    
    if not font_dir.exists():
        sys.exit(f"Error: Font directory not found: {font_dir}")
    
    # Create temp directory for intermediate files
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        combined_path = temp_path / "combined.png"
        quantized_path = temp_path / "quantized.png"
        
        # Step 1: Combine glyphs into one large PNG
        combine_glyphs(font_dir, combined_path)
        
        # Step 2: Run pngquant
        run_pngquant(combined_path, quantized_path)
        
        # Step 3: Slice back into individual glyphs
        slice_glyphs(quantized_path, output_dir)
    
    print("Done!")


if __name__ == "__main__":
    main()

