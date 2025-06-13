from PIL import Image
import sys
import numpy as np
from struct import pack

def intlit(bytes):
    return int.from_bytes(bytes, "little")

def quit(message):
    print(message)
    exit()

if(len(sys.argv) != 2):
    quit("Usage: graphics.py <filename>")

filename = sys.argv[1]

print(filename)

graphic = open(f"{filename}", "rb")

filename = filename.rstrip("_anm.bin")

print(filename)

header = graphic.read(0x20)

identifier = header[0x0:0x8]

verify = b'NAXA5010'

bpp = 0

if (identifier != verify):
    quit("Identifier not found! Might not be a graphics file.")

print(identifier)

clutSize = intlit(header[0x8:0xC])

if (clutSize == 256):
    bpp = 8
elif (clutSize == 16):
    bpp = 4
else:
    quit("other BPP Image not supported yet")

print(clutSize)
print(bpp)

clutOffset = intlit(header[0xC:0x10])

print("clutoffset")
print(clutOffset)

pxlOffset = intlit(header[0x10:0x14])

print(pxlOffset)

anmOffset = intlit(header[0x14:0x18])

print(anmOffset)



palSize = 4

sectionSize = 0x20

clut = b''

palOffset = 0

sectionOffset = 0

graphic.seek(clutOffset)

clutPos = clutOffset

if clutSize == 256:

    for i in range(8):
        palOffset = i * 0x80
        print("paloffset")
        print(f"{palOffset:X}")



        clutPos = (clutOffset + (palOffset + 0))
        print("clutpos")
        print(f"{clutPos:X}")
        graphic.seek(clutPos)
        colours = graphic.read(sectionSize)
        clut = clut + colours


        clutPos = (clutOffset + (palOffset + (0x40)))

        print(f"{clutPos:X}")
        graphic.seek(clutPos)
        colours = graphic.read(sectionSize)
        clut = clut + colours

        clutPos = (clutOffset + (palOffset + (0x20)))

        print(f"{clutPos:X}")
        graphic.seek(clutPos)
        colours = graphic.read(sectionSize)
        clut = clut + colours

        clutPos = (clutOffset + (palOffset + (0x60)))

        print(f"{clutPos:X}")
        graphic.seek(clutPos)
        colours = graphic.read(sectionSize)
        clut = clut + colours

elif bpp == 4:
    clut = graphic.read(clutSize * palSize) 
    print(clut)

#PIL.ImagePalette.ImagePalette("RGBA", clut)

graphic.seek(pxlOffset + 8) # Read the first image offset to calculate how many images there are

sprCount = intlit(graphic.read(4)) // 0x10 # Each sprite entry is 16 bytes long

print(sprCount)

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

#clut = np.array(clut)

#print(clut)

for x in range(sprCount):
    
    print(x)

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

    #print(sprDataSize)
    
    graphic.seek(pxlOffset + sprOffset)

    #print(sprData)

    #if (bpp == 4):

    if (bpp == 4):
        sprData4 = graphic.read(sprDataSize)
        sprData = b""
        for byte in sprData4:
            # These might be backwards
            sprData += pack("bb", byte & 0xF, byte >> 4)
    else: 
        sprData = graphic.read(sprDataSize)

    sprite = Image.frombytes("P", sprSize, bytes(sprData))
    sprite.putpalette(clut, rawmode="RGBA")
    sprite.save(f"{filename}_{x}.png")



"""
    sprite = open(f"menu{x}.tm2", "wb")

    sprDataSizeByte = sprDataSize.to_bytes(4, "little")

    timSize = (clutSizeInt * 4) + sprDataSize + 0x30

    timSize = timSize.to_bytes(4, "little")

    sprWbyte = sprW.to_bytes(2, "little")
    sprHbyte = sprH.to_bytes(2, "little")

    print(clutSize)

    sprite.write(b'TIM2')
    sprite.write(b'\x04\x00\x01\x00')
    sprite.write(b'\x00\x00\x00\x00\x00\x00\x00\x00')
    sprite.write(timSize)

    if bpp == 8:
        sprite.write(b'\x00\x04\x00\x00')
    else:
        sprite.write(b'\x40\x00\x00\x00')
    
    sprite.write(sprDataSizeByte)
    sprite.write(b'\x30\x00')
    sprite.write(b'\x00\x00')
    sprite.write(b'\x00')
    sprite.write(b'\x01')
    sprite.write(b'\x03')
    sprite.write(b'\x05')
    sprite.write(sprWbyte)
    sprite.write(sprHbyte)

    for i in range (24):
        sprite.write(b'\x00')
    sprite.write(clut)
    sprite.write(sprData)

    #image = Image.fromarray(sprData)
    #image.palette.colors = clut
    #image.save(f"{x}.png")


    #image = Image.frombytes("RGBA", sprSize, "raw")
    #image.save(f"{x}.png")
"""