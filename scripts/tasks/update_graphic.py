import os
import shutil
import sys
from pathlib import Path
from PIL import Image
from .extract_graphic import GRAPHICS_FILES


def intlit(bytes):
    return int.from_bytes(bytes, "little")


def writeint(num, size):
    return num.to_bytes(size, byteorder="little")


def insert_graphics(filepath: str | Path, insert_frames: bool = False):
    """
    Insert edited graphics back into an _anm.bin file.
    
    Args:
        filepath: Path to the _anm.bin file
        insert_frames: Whether to insert frame data (for files like menu00_anm.bin)
    """
    filepath = Path(filepath).resolve()
    filedir = filepath.parent
    filename = filepath.name

    origFile = open(filepath, "rb")

    filename = filename[:filename.rfind("_anm.bin")]

    input_dir = filedir / filename

    shutil.copy(filepath, filedir / f"{filename}_new.bin")

    newFile = open(filedir / f"{filename}_new.bin", "r+b")

    header = origFile.read(0x20)
    identifier = header[0x0:0x8]
    verify = b'NAXA5010'

    if (identifier != verify):
        exit("Identifier not found! Might not be a graphics file.")

    newFile.seek(0)
    newFile.write(header)

    clutSize = intlit(header[0x8:0xC])
    clutOffset = intlit(header[0xC:0x10])
    pxlOffset = intlit(header[0x10:0x14])
    anmOffset = intlit(header[0x14:0x18])

    bpp = 0

    if (clutSize == 256):
        bpp = 8
    elif (clutSize == 16):
        bpp = 4
    else:
        exit("other BPP formats not supported yet")

    palSize = 4

    with open(input_dir / f"{filename}_orig.pal", "rb") as palFile:
        clut = palFile.read(clutSize * palSize)

    newFile.seek(clutOffset)
    newFile.write(clut)

    if insert_frames:

        origFile.seek(anmOffset)
        newFile.seek(anmOffset)
        frameCount = intlit(origFile.read(4))

        anmPadding = 16 - ((frameCount * 0x4 + 0x4) % 16)
        anmSize = (frameCount * 0x4 + 0x4) + anmPadding
        newFile.write(writeint(frameCount, 4))

        frameOffset = anmSize

        for x in range(frameCount):
            
            size = os.stat(input_dir / f"{filename}_frame_{x}.bin").st_size
            newFile.write(writeint(frameOffset, 4))
            frameOffset = frameOffset + size

        for x in range(anmPadding):
            newFile.write(b"\xFF")

        for x in range(frameCount):
            frame = open(input_dir / f"{filename}_frame_{x}.bin", "rb")
            frameData = frame.read()
            newFile.write(frameData)
            print(f"{filename}/{filename}_frame_{x}.bin written!")

    origFile.seek(pxlOffset + 8) # Read the first image offset to calculate how many images there are
    newFile.seek(pxlOffset)

    spriteCount = intlit(origFile.read(4)) // 0x10 # Each sprite entry is 16 bytes long

    dataOffset = spriteCount * 0x10
    sprOffset = dataOffset

    padding = 0

    for x in range(spriteCount):
        graphic = Image.open(input_dir / f"{filename}_{x}.png", "r")
        size = graphic.width * graphic.height
        if bpp == 4:
            size = size // 2
            if (size % 16 != 0):
                padding = size % 16
        
        if insert_frames:
            newFile.write(writeint(graphic.height, 2))
            newFile.write(writeint(graphic.width, 2))
        
        else:
            newFile.read(4)
        newFile.write(writeint(graphic.height, 2))
        newFile.write(writeint(graphic.width, 2))

        newFile.write(writeint(sprOffset, 4))
        newFile.write(writeint(x, 4))
        sprOffset = sprOffset + size + padding

    for x in range(spriteCount):
        graphic = Image.open(input_dir / f"{filename}_{x}.png", "r")

        data = list(graphic.getdata())
        
        binData = b""
        if (bpp == 8):
            for i in range(len(data)):
                byte = data[i].to_bytes(1)
                binData = binData + byte
        elif (bpp == 4):
            for i in range(0, len(data), 2):
                byte1 = data[i]
                byte2 = data[i+1]
                if byte1 == 16:
                    byte1 = 1
                if byte2 == 16:
                    byte2 = 1
                byte2 = byte2 << 4
                byte = byte2 + byte1
                byte = byte.to_bytes(1)
                binData = binData + byte

        if x != (spriteCount - 1):          # No need to add padding to the last sprite
            for i in range(padding):
                binData = binData + b"\xFF"
        
        newFile.write(binData)

        print(f"{filename}/{filename}_{x}.png written!")

    origFile.close()
    newFile.close()
    
    print(f"{filename}_new.bin saved!")


def copy_tree(src, dst):
    """Copy directory tree, merging with existing files."""
    src_path = Path(src)
    dst_path = Path(dst)
    
    if not src_path.exists():
        print(f"Warning: {src} does not exist, skipping")
        return
    
    dst_path.mkdir(parents=True, exist_ok=True)
    
    for item in src_path.rglob("*"):
        if item.is_file():
            relative_path = item.relative_to(src_path)
            dest_file = dst_path / relative_path
            dest_file.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(item, dest_file)
            print(f"Copied {item} to {dest_file}")


def insert_all_graphics():
    """Insert edited graphics back into all _anm.bin files."""
    print("\nInserting edited graphics into _anm.bin files...")
    
    graphics_orig = Path("graphics/orig")
    graphics_processed = Path("graphics/processed")
    graphics_frames = Path("graphics/frames")
    
    # Merge processed and frames into orig
    print("\nMerging processed graphics into orig...")
    copy_tree(graphics_processed, graphics_orig)
    
    print("\nMerging frame data into orig...")
    copy_tree(graphics_frames, graphics_orig)
    
    # Insert graphics into each file
    for name in GRAPHICS_FILES.keys():
        anm_file = graphics_orig / f"{name}_anm.bin"
        if anm_file.exists():
            print(f"\nInserting {name}...")
            # Special case for menu00: insert frame data
            insert_frames = (name == "menu00")
            insert_graphics(anm_file, insert_frames)
        else:
            print(f"Warning: {anm_file} not found, skipping")
    
    # Copy _new.bin files back to DATA
    print("\nCopying patched graphics back to DATA...")
    for name, dest_path in GRAPHICS_FILES.items():
        new_file = graphics_orig / f"{name}_new.bin"
        if new_file.exists():
            dest = Path(dest_path)
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(new_file, dest)
            print(f"Copied {new_file} to {dest}")
        else:
            print(f"Warning: {new_file} not found, skipping")
    
    print("\nGraphics insertion complete!")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python insert.py <filepath> [frame]")
        sys.exit(1)
    
    filepath = sys.argv[1]
    insert_frames = len(sys.argv) == 3 and sys.argv[2] == "frame"
    
    insert_graphics(filepath, insert_frames)
