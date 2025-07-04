import sys
import os
import math

if (len(sys.argv) != 2):
    print("Usage: pack.py <file.bin>")
    sys.exit(1)

slpm = open("translated/SLPM_663.60", "r+b")

dataName = os.path.basename(sys.argv[1])

dataFile = open(f"translated/{dataName}", "wb")

dataName = dataName.rstrip(".BIN")

logFile = open(f"{dataName}.txt", "r", encoding="utf-8")

filesList = []

seekAddr = 0x001829D0

slpm.seek(seekAddr)

startSector = 0

baseptr = 0xFFF80

sector = 0x800

while(True):
    line = logFile.readline()
    if line == "":
        break
    
    folderInfo = (line).strip("\n").split()

    folderAmount = int(folderInfo[3])
    folderName = folderInfo[0]

    for i in range (folderAmount):
        line = logFile.readline()
        fileInfo = (line).strip("\n").split()

        fileName = fileInfo[0]

        file = open(f"{dataName}{folderName}{fileName}", "rb")

        fileData = file.read()

        fileSize = len(fileData)
        
        sectorSize = math.ceil((len(fileData)) / sector)

        padding = bytes((sectorSize * sector) - fileSize)

        dataFile.write(fileData)
        dataFile.write(padding)

        filePtr = int(fileInfo[1]) + baseptr

        filePtr = filePtr.to_bytes(4, byteorder="little")
        fileSize = fileSize.to_bytes(4, byteorder="little")
        startSectorBytes = startSector.to_bytes(4, byteorder="little")
        sectorSizeBytes = sectorSize.to_bytes(4, byteorder="little")

        slpm.write(filePtr)
        slpm.write(fileSize)
        slpm.write(startSectorBytes)
        slpm.write(sectorSizeBytes)

        startSector = startSector + (sectorSize)


    