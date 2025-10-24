
import sys, os, shutil
from PIL import Image

def intlit(bytes):
    return int.from_bytes(bytes, "little")

def writeint (num, size):
    return num.to_bytes(size, byteorder="little")

frame = False

if (len(sys.argv) == 3):
    if (sys.argv[2] == "frame"):
        frame = True
else:
    frame = False
print(frame)

(filedir, filename) = os.path.split(os.path.abspath(sys.argv[1]))

origFile = open(f"{filedir}\\{filename}", "rb")

filename = filename.rstrip("_anm.bin")

shutil.copy(f"{filedir}\\{filename}_anm.bin", f"{filedir}\\{filename}_new.bin")

newFile = open(f"{filedir}\\{filename}_new.bin", "r+b")

header = origFile.read(0x20)
identifier = header[0x0:0x8]
verify = b'NAXA5010'

bpp = 0

if (identifier != verify):
    exit("Identifier not found! Might not be a graphics file.")

newFile.seek(0)
newFile.write(header)

clutSize = intlit(header[0x8:0xC])
clutOffset = intlit(header[0xC:0x10])
pxlOffset = intlit(header[0x10:0x14])
anmOffset = intlit(header[0x14:0x18])

if (clutSize == 256):
    bpp = 8
elif (clutSize == 16):
    bpp = 4
else:
    exit("other BPP formats not supported yet")

palSize = 4

with open(f"{filedir}\\{filename}\\{filename}_orig.pal", "rb") as palFile:
    clut = palFile.read(clutSize * palSize)

newFile.seek(clutOffset)
newFile.write(clut)

if (frame == True):

    origFile.seek(anmOffset)
    newFile.seek(anmOffset)
    frameCount = intlit(origFile.read(4))

    anmPadding = 16 - ((frameCount * 0x4 + 0x4) % 16)
    anmSize = (frameCount * 0x4 + 0x4) + anmPadding
    newFile.write(writeint(frameCount, 4))

    frameOffset = anmSize

    for x in range (frameCount):
        
        size = os.stat(f"{filedir}\\{filename}\\{filename}_frame_{x}.bin").st_size
        newFile.write(writeint(frameOffset, 4))
        frameOffset = frameOffset + size

    for x in range(anmPadding):
        newFile.write(b"\xFF")

    for x in range (frameCount):
        frame = open(f"{filedir}\\{filename}\\{filename}_frame_{x}.bin", "rb")
        frameData = frame.read()
        newFile.write(frameData)
        print(f"{filename}\\{filename}_frame_{x}.bin written!")


origFile.seek(pxlOffset + 8) # Read the first image offset to calculate how many images there are
newFile.seek(pxlOffset)

spriteCount = intlit(origFile.read(4)) // 0x10 # Each sprite entry is 16 bytes long

dataOffset = spriteCount * 0x10
sprOffset = dataOffset

for x in range(spriteCount):
    graphic = Image.open(f"{filedir}\\{filename}\\{filename}_{x}.png", "r")
    size = graphic.width * graphic.height
    
    newFile.write(writeint(graphic.height, 2))
    newFile.write(writeint(graphic.width, 2))
    newFile.write(writeint(graphic.height, 2))
    newFile.write(writeint(graphic.width, 2))

    newFile.write(writeint(sprOffset, 4))
    newFile.write(writeint(x, 4))
    sprOffset = sprOffset + size


for x in range(spriteCount):
    graphic = Image.open(f"{filedir}\\{filename}\\{filename}_{x}.png", "r")

    data = list(graphic.getdata())

    binData = b""
    for i in range(len(data)):
        byte = data[i].to_bytes(1)
        binData = binData + byte
    
    newFile.write(binData)

    print(f"{filename}\\{filename}_{x}.png written!")

print(f"{filename}_new.bin saved!")
