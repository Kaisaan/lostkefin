import shutil
import sys
from pathlib import Path
from struct import pack
from PIL import Image


# Map of graphics files to extract (name without _anm.bin suffix -> source path in DATA)
GRAPHICS_FILES = {
    "adol_d": "DATA/anm/adol_d_anm.bin",
    "adol_t": "DATA/anm/adol_t_anm.bin",
    "aname_are": "DATA/event/aname_arena_anm.bin",
    "aname_ekke": "DATA/event/aname_ekken_anm.bin",
    "aname_fertek": "DATA/event/aname_fertek_anm.bin",
    "aname_fertet": "DATA/event/aname_fertet_anm.bin",
    "aname_forest": "DATA/event/aname_foresta_anm.bin",
    "aname_gisik": "DATA/event/aname_gisiki_anm.bin",
    "aname_himitsu": "DATA/event/aname_himitsu_anm.bin",
    "aname_kef": "DATA/event/aname_kefin_anm.bin",
    "aname_kefine": "DATA/event/aname_kefine_anm.bin",
    "aname_kefinjc": "DATA/event/aname_kefinjc_anm.bin",
    "aname_kefinjc2": "DATA/event/aname_kefinjc2_anm.bin",
    "aname_kefinjc3": "DATA/event/aname_kefinjc3_anm.bin",
    "aname_kefinjc4": "DATA/event/aname_kefinjc4_anm.bin",
    "aname_kefinjc5": "DATA/event/aname_kefinjc5_anm.bin",
    "aname_kefinjc6": "DATA/event/aname_kefinjc6_anm.bin",
    "aname_kefinjc7": "DATA/event/aname_kefinjc7_anm.bin",
    "aname_kefinje": "DATA/event/aname_kefinje_anm.bin",
    "aname_kefinje2": "DATA/event/aname_kefinje2_anm.bin",
    "aname_kefinje3": "DATA/event/aname_kefinje3_anm.bin",
    "aname_kefinje4": "DATA/event/aname_kefinje4_anm.bin",
    "aname_kefinjw": "DATA/event/aname_kefinjw_anm.bin",
    "aname_kefinjw2": "DATA/event/aname_kefinjw2_anm.bin",
    "aname_kefinjw3": "DATA/event/aname_kefinjw3_anm.bin",
    "aname_kefinjw4": "DATA/event/aname_kefinjw4_anm.bin",
    "aname_kefinr": "DATA/event/aname_kefinr_anm.bin",
    "aname_kefinr1": "DATA/event/aname_kefinr1_anm.bin",
    "aname_kefinr2": "DATA/event/aname_kefinr2_anm.bin",
    "aname_kefinr3": "DATA/event/aname_kefinr3_anm.bin",
    "aname_kefinr4": "DATA/event/aname_kefinr4_anm.bin",
    "aname_kefinr5": "DATA/event/aname_kefinr5_anm.bin",
    "aname_kefinw": "DATA/event/aname_kefinw_anm.bin",
    "aname_kenj": "DATA/event/aname_kenja_anm.bin",
    "aname_kessyou": "DATA/event/aname_kessyou_anm.bin",
    "aname_library": "DATA/event/aname_library_anm.bin",
    "aname_masse": "DATA/event/aname_massea_anm.bin",
    "aname_meretseger": "DATA/event/aname_meretseger_anm.bin",
    "aname_neadcave": "DATA/event/aname_neadcave_anm.bin",
    "aname_oasis": "DATA/event/aname_oasis_anm.bin",
    "aname_priso": "DATA/event/aname_prison_anm.bin",
    "aname_ramzenc": "DATA/event/aname_ramzenc_anm.bin",
    "aname_ramzenc2": "DATA/event/aname_ramzenc2_anm.bin",
    "aname_ramzeno": "DATA/event/aname_ramzeno_anm.bin",
    "aname_ramzens": "DATA/event/aname_ramzens_anm.bin",
    "aname_ramzent": "DATA/event/aname_ramzent_anm.bin",
    "aname_rase": "DATA/event/aname_rasen_anm.bin",
    "aname_renk": "DATA/event/aname_renkin_anm.bin",
    "aname_seitans": "DATA/event/aname_seitansai_anm.bin",
    "aname_sekhet": "DATA/event/aname_sekhet_anm.bin",
    "aname_sekhet2": "DATA/event/aname_sekhet2_anm.bin",
    "aname_sekhet3": "DATA/event/aname_sekhet3_anm.bin",
    "aname_sekhet4": "DATA/event/aname_sekhet4_anm.bin",
    "aname_sekhet5": "DATA/event/aname_sekhet5_anm.bin",
    "aname_sekhet6": "DATA/event/aname_sekhet6_anm.bin",
    "aname_sekhet7": "DATA/event/aname_sekhet7_anm.bin",
    "aname_sekhet8": "DATA/event/aname_sekhet8_anm.bin",
    "aname_sekhet9": "DATA/event/aname_sekhet9_anm.bin",
    "aname_sekhet10": "DATA/event/aname_sekhet10_anm.bin",
    "aname_shal": "DATA/event/aname_shal_anm.bin",
    "aname_the": "DATA/event/aname_thebani_anm.bin",
    "aname_thebani2": "DATA/event/aname_thebani2_anm.bin",
    "aname_thebani3": "DATA/event/aname_thebani3_anm.bin",
    "aname_thebans": "DATA/event/aname_thebans_anm.bin",
    "aname_tower": "DATA/event/aname_tower_anm.bin",
    "aname_tower1": "DATA/event/aname_tower1_anm.bin",
    "aname_tower2": "DATA/event/aname_tower2_anm.bin",
    "aname_tower3": "DATA/event/aname_tower3_anm.bin",
    "aname_tower4": "DATA/event/aname_tower4_anm.bin",
    "aname_tower5": "DATA/event/aname_tower5_anm.bin",
    "aname_tower6": "DATA/event/aname_tower6_anm.bin",
    "aname_under": "DATA/event/aname_under_anm.bin",
    "aname_xands": "DATA/event/aname_xands_anm.bin",
    "aname_xandt": "DATA/event/aname_xandt_anm.bin",
    "bname_abyss": "DATA/event/bname_abyss_anm.bin",
    "bname_agunhy": "DATA/event/bname_agunhy_anm.bin",
    "bname_azort": "DATA/event/bname_azort_anm.bin",
    "bname_balk": "DATA/event/bname_balk_anm.bin",
    "bname_cario": "DATA/event/bname_carion_anm.bin",
    "bname_daw": "DATA/event/bname_dawman_anm.bin",
    "bname_hyudol": "DATA/event/bname_hyudol_anm.bin",
    "bname_javil": "DATA/event/bname_javil_anm.bin",
    "bname_kef": "DATA/event/bname_kefin_anm.bin",
    "bname_valte": "DATA/event/bname_valte_anm.bin",
    "category": "DATA/shop/category_anm.bin",
    "g_guide": "DATA/gallery/g_guide_anm.bin",
    "help01": "DATA/help/help01_anm.bin",
    "help02": "DATA/help/help02_anm.bin",
    "help03": "DATA/help/help03_anm.bin",
    "help04": "DATA/help/help04_anm.bin",
    "help05": "DATA/help/help05_anm.bin",
    "help06": "DATA/help/help06_anm.bin",
    "load_bg00": "DATA/saveload/load_bg00_anm.bin",
    "m_guide": "DATA/gallery/m_guide_anm.bin",
    "magic_name": "DATA/gameother/magic_name_anm.bin",
    "menu00": "DATA/gameother/menu00_anm.bin",
    "opt_bg01": "DATA/option/opt_bg01_anm.bin",
    "opt_menu00": "DATA/option/opt_menu00_anm.bin",
    "opt_menu02": "DATA/option/opt_menu02_anm.bin",
    "save_bg00": "DATA/saveload/save_bg00_anm.bin",
    "vbg_ev40": "DATA/event/vbg_ev40_anm.bin",
    "vbg_ev45": "DATA/event/vbg_ev45_anm.bin",
    "vbg_ev49": "DATA/event/vbg_ev49_anm.bin",
    "number00": "DATA/gameother/number00_anm.bin",
    "number01": "DATA/gameother/number01_anm.bin",
}


def intlit(bytes):
    return int.from_bytes(bytes, "little")


def extract_graphics(filepath: str | Path, extract_frames: bool = False):
    """
    Extract graphics from an _anm.bin file.
    
    Args:
        filepath: Path to the _anm.bin file
        extract_frames: Whether to extract frame data (for files like menu00_anm.bin)
    """
    filepath = Path(filepath).resolve()
    filedir = filepath.parent
    filename = filepath.name

    graphic = open(filepath, "rb")

    filename = filename.rstrip("_anm.bin")

    output_dir = filedir / filename
    output_dir.mkdir(exist_ok=True)

    logFile = open(output_dir / f"{filename}.txt", "w", encoding="utf-8")

    header = graphic.read(0x20)

    identifier = header[0x0:0x8]

    verify = b'NAXA5010'

    bpp = 0

    if (identifier != verify):
        exit("Identifier not found! Might not be a graphics file.")

    clutSize = intlit(header[0x8:0xC])
    clutOffset = intlit(header[0xC:0x10])
    pxlOffset = intlit(header[0x10:0x14])
    anmOffset = intlit(header[0x14:0x18])
    logFile.write(f"pixel offset is {pxlOffset:X}\n")
    logFile.write(f"anm offset is {anmOffset:X}\n")

    if (clutSize == 256):
        bpp = 8
        logFile.write(f"{filename} is 8BPP\n")
    elif (clutSize == 16):
        bpp = 4
        logFile.write(f"{filename} is 4BPP\n")
    else:
        exit("other BPP formats not supported yet")

    palSize = 4

    sectionSize = 0x20

    clut = b''

    palOffset = 0

    graphic.seek(clutOffset)

    clutPos = clutOffset

    if bpp == 8:

        origclut = graphic.read(clutSize * palSize)

        with open(output_dir / f"{filename}_orig.pal", "wb") as palette:
            palette.write(origclut)
        print(f"{filename}/{filename}_orig.pal saved!")

        graphic.seek(clutOffset)

        for i in range(8):          # Swizzle the palette (there's probably a better way to do this, but it works!)
            palOffset = i * 0x80

            clutPos = (clutOffset + (palOffset + 0))
            graphic.seek(clutPos)
            colours = graphic.read(sectionSize)
            clut = clut + colours

            clutPos = (clutOffset + (palOffset + (0x40)))
            graphic.seek(clutPos)
            colours = graphic.read(sectionSize)
            clut = clut + colours

            clutPos = (clutOffset + (palOffset + (0x20)))
            graphic.seek(clutPos)
            colours = graphic.read(sectionSize)
            clut = clut + colours

            clutPos = (clutOffset + (palOffset + (0x60)))
            graphic.seek(clutPos)
            colours = graphic.read(sectionSize)
            clut = clut + colours
        with open(output_dir / f"{filename}_swzl.pal", "wb") as palette:
            palette.write(clut)
        print(f"{filename}/{filename}_swzl.pal saved!")

    elif bpp == 4:
        clut = graphic.read(clutSize * palSize)
        with open(output_dir / f"{filename}_orig.pal", "wb") as palette:
            palette.write(clut)
        print(f"{filename}/{filename}_orig.pal saved!")

    graphic.seek(pxlOffset + 8) # Read the first image offset to calculate how many images there are

    sprCount = intlit(graphic.read(4)) // 0x10 # Each sprite entry is 16 bytes long

    graphic.seek(pxlOffset)

    for x in range(sprCount):

        entry = x * 0x10

        graphic.seek(pxlOffset + entry)
        graphic.read(4)  # Skip sprWvram and sprHvram
        sprW = intlit(graphic.read(2))
        sprH = intlit(graphic.read(2))
        sprOffset = intlit(graphic.read(4))
        graphic.read(4)  # Skip sprIndex
        sprSize = (sprH, sprW)
        sprDataSize = sprH * sprW
        realOffset = pxlOffset + sprOffset
        graphic.seek(realOffset)

        if (bpp == 4):
            sprDataSize = sprDataSize // 2
            sprData4 = graphic.read(sprDataSize)
            
            with open(output_dir / f"{filename}_{x}_packed.bin", "wb") as bin: # Save the original indexing data separate from the image to help with re-insertion
                bin.write(sprData4)
            print(f"{filename}/{filename}_{x}_packed.bin saved!")

            sprData = b""
            for byte in sprData4:
                sprData += pack("bb", byte & 0xF, byte >> 4)
            with open(output_dir / f"{filename}_{x}_unpacked.bin", "wb") as bin:
                bin.write(sprData)
            print(f"{filename}/{filename}_{x}_unpacked.bin saved!")

        else: 
            sprData = graphic.read(sprDataSize)
            with open(output_dir / f"{filename}_{x}_8bpp.bin", "wb") as bin:
                bin.write(sprData)

        sprite = Image.frombytes("P", sprSize, bytes(sprData))
        sprite.putpalette(clut, rawmode="RGBA")
        sprite.save(fp=output_dir / f"{filename}_{x}.png")
        print(f"{filename}/{filename}_{x}.png saved!")
        
        logFile.write(f"{filename}_{x}.png is at {realOffset:X} (sprite offset is {sprOffset:X}) its size is {sprSize[0]:X}H and {sprSize[1]:X}W its data size is {sprDataSize:X} bytes\n")

    if extract_frames:

        graphic.seek(anmOffset)

        anmCount = intlit(graphic.read(4))

        frameSize = 0x70

        for x in range(anmCount):
            entry = x * 0x4
            graphic.seek(anmOffset + entry + 0x4) # Add 4 bytes since the first 4 holds anmCount

            frameOffset = intlit(graphic.read(4))
            realOffset = frameOffset + anmOffset

            graphic.seek(realOffset)

            frameData = graphic.read(frameSize)

            with open(output_dir / f"{filename}_frame_{x}.bin", "wb") as frame:
                frame.write(frameData)
            print(f"{filename}/{filename}_frame_{x}.bin saved!")
            
            logFile.write(f"{filename}_frame_{x}.bin is at {realOffset:X}\n")
    
    graphic.close()
    logFile.close()


def extract_all_graphics():
    """Extract graphics from all _anm.bin files."""
    print("\nExtracting graphics from _anm.bin files...")
    
    # Create graphics/orig directory
    graphics_orig = Path("graphics/orig")
    if graphics_orig.exists():
        shutil.rmtree(graphics_orig)
    graphics_orig.mkdir(parents=True, exist_ok=True)
    
    # Copy _anm.bin files to graphics/orig
    for name, source_path in GRAPHICS_FILES.items():
        source = Path(source_path)
        if source.exists():
            dest = graphics_orig / f"{name}_anm.bin"
            print(f"Copying {source} to {dest}")
            shutil.copy2(source, dest)
        else:
            print(f"Warning: {source} not found, skipping")
    
    # Extract graphics from each file
    for name in GRAPHICS_FILES.keys():
        anm_file = graphics_orig / f"{name}_anm.bin"
        if anm_file.exists():
            print(f"\nExtracting {name}...")
            # Special case for menu00: extract frame data
            extract_frames = (name == "menu00")
            extract_graphics(anm_file, extract_frames)
    
    print("\nGraphics extraction complete!")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python graphics.py <filepath> [frame]")
        sys.exit(1)
    
    filepath = sys.argv[1]
    extract_frames = len(sys.argv) == 3 and sys.argv[2] == "frame"
    
    extract_graphics(filepath, extract_frames)


