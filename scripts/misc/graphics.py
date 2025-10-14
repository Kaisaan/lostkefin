from PIL import Image
import sys, os
from struct import pack

def intlit(bytes):
    return int.from_bytes(bytes, "little")

if(len(sys.argv) != 2):
    exit("Usage: graphics.py <filename>")

(filedir, filename) = os.path.split(os.path.abspath(sys.argv[1]))

#filename = sys.argv[1]
#print(filename)
#filedir = os.path.dirname(filename)
#print(filedir)

graphic = open(f"{filename}", "rb")

filename = filename.rstrip("_anm.bin")

os.makedirs(f"{filedir}\\{filename}", exist_ok="true")

logFile = open(f"{filedir}\\{filename}\\{filename}.txt", "w", encoding="utf-8")

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

sectionOffset = 0

graphic.seek(clutOffset)

clutPos = clutOffset

if bpp == 8:

    for i in range(8):          # Swizzle the pallete (there's probably a better way to do this, but it works!)
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

elif bpp == 4:
    clut = graphic.read(clutSize * palSize) 

graphic.seek(pxlOffset + 8) # Read the first image offset to calculate how many images there are

sprCount = intlit(graphic.read(4)) // 0x10 # Each sprite entry is 16 bytes long

graphic.seek(pxlOffset)

sprH = 0
sprW = 0
sprHvram = 0
sprWvram = 0
sprOffset = 0
sprIndex = 0

sprDataSize = 0
sprSize = (0, 0)

entry = 0

with open(f"{filename}\\{filename}.pal", "wb") as palette:
    palette.write(clut)
print(f"{filename}\\{filename}.pal saved!")

for x in range(sprCount):

    entry = x * 0x10

    graphic.seek(pxlOffset + entry)
    sprWvram = intlit(graphic.read(2))
    sprHvram = intlit(graphic.read(2))
    sprW = intlit(graphic.read(2))
    sprH = intlit(graphic.read(2))
    sprOffset = intlit(graphic.read(4))
    sprIndex = intlit(graphic.read(4))
    sprSize = (sprH, sprW)
    sprDataSize = sprH * sprW
    realOffset = pxlOffset + sprOffset
    graphic.seek(realOffset)

    if (bpp == 4):
        sprData4 = graphic.read(sprDataSize)
        with open(f"{filedir}\\{filename}\\{filename}_{x}_4bpp.bin", "wb") as bin: # Save the original indexing data separate from the image to help with re-insertion
            bin.write(sprData4)
        sprData = b""
        for byte in sprData4:
            sprData += pack("bb", byte & 0xF, byte >> 4)
    else: 
        sprData = graphic.read(sprDataSize)
        with open(f"{filedir}\\{filename}\\{filename}_{x}_8bpp.bin", "wb") as bin:
            bin.write(sprData)

    sprite = Image.frombytes("P", sprSize, bytes(sprData))
    sprite.putpalette(clut, rawmode="RGBA")
    sprite.save(fp=f"{filedir}\\{filename}\\{filename}_{x}.png")
    print(f"{filename}\\{filename}_{x}.png saved!")
    logFile.write(f"{filename}_{x}.png is at {realOffset:X}\n")


    #print(f"{filename}\\{filename}_{x}.bin saved!")

    
    newdata = sprite.tobytes()
    #print(sprite.tobytes())

    
