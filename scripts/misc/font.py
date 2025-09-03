from PIL import Image
from struct import pack

slpm = open("extracted/SLPM_663.60", "rb")





"""
table = open("font.tbl", "w", encoding="shift-jis")

fileptr = start
while fileptr < end:

    slpm.seek(fileptr)
    charval = slpm.read(2)
    char = charval.decode(encoding="shift-jis", errors="backslashreplace").lstrip(" ")
    # char 
    charval = int.from_bytes(charval, "big")
    charval = hex(charval).removeprefix("0x").upper().removeprefix("20")
    
    table.write(f"{charval}={char}\n")
    print(fileptr)
    print(char)
    print(charval)
    fileptr += 2
"""
#1A3E98
#215D20

#71E88

fontTable = []

def getFontTable():

    fontTableStart = 0x1A31F0
    fontTableEnd = 0x1A3E98

    slpm.seek(fontTableStart)

    while (slpm.tell() < fontTableEnd):

        char = slpm.read(2).decode(encoding="shift-jis", errors="backslashreplace").lstrip(" ")

        fontTable.append(char)

#clut = b""

clutSize = 16 * 4

def getClut():

    clutStart = 0x25E4C0

    slpm.seek(clutStart)

    global clut

    clut = slpm.read(clutSize)



charW = 12
charH = 24

charDataSize = charW * charH

charSize = (charH, charW * 2)

def extractFontGraphics():

    fontGraphicsStart = 0x1A3EA0

    slpm.seek(fontGraphicsStart)

    for x in range(len(fontTable)):
        
        charData = slpm.read(charDataSize)

        imgData = b""

        for byte in charData:
            
            imgData += pack("bb", byte & 0xF, byte >> 4)
        
        image = Image.frombytes("P", charSize, imgData)
        image.putpalette(clut, rawmode="RGBA")
        image.save(f"font/{x}.png")


def main():
    getFontTable()
    getClut()
    #print(clut)
    extractFontGraphics()
    #print(fontTable)
    #print(len(fontTable))

if __name__=="__main__":
    main()


