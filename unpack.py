import sys
import os

if (len(sys.argv) != 2):
    print("Usage: unpack.py <file.bin>")
    sys.exit(1)

slpm = open("extracted/SLPM_663.60", "rb")

basePtr = 0xFFF80
readSize = 32
terminator = "\x00"
sector = 0x800

dataName = os.path.basename(sys.argv[1])

dataFile = open(f"extracted/{dataName}", "rb")

dataName = dataName.rstrip(".BIN")

logFile = open(f"{dataName}.txt", "w", encoding="utf-8")

os.makedirs(f"{dataName}", exist_ok=True)

seekAddr = 0x001875E0

foldersInfo = []

while (True):

    slpm.seek(seekAddr)

    folderPtr = int.from_bytes(slpm.read(4), "little")
    folderIndex = int.from_bytes(slpm.read(4), "little")
    filecount = int.from_bytes(slpm.read(4), "little")
    
    if (folderPtr == 0) & (folderIndex == 0):
        break

    folderPtr = folderPtr - basePtr

    slpm.seek(folderPtr)
    folderName = slpm.read(readSize).decode(encoding="shift-jis", errors="backslashreplace")
    folderName = folderName[:folderName.find(terminator)]

    seekAddr = seekAddr + 12

    foldersInfo.append([folderName, folderPtr, folderIndex, filecount])

total = foldersInfo[-1][2] + foldersInfo[-1][3]

seekAddr = 0x001829D0

slpm.seek(seekAddr)

for i in range(len(foldersInfo)):
    logFile.write(f"{foldersInfo[i][0]} {foldersInfo[i][1]} {foldersInfo[i][2]} {foldersInfo[i][3]}\n")
    
    for j in range(foldersInfo[i][3]):

        slpm.seek(seekAddr)
        filePtr = int.from_bytes(slpm.read(4), "little")
        fileSize = int.from_bytes(slpm.read(4), "little")
        fileStart = int.from_bytes(slpm.read(4), "little")
        fileEnd = int.from_bytes(slpm.read(4), "little")

        filePtr = filePtr - basePtr

        slpm.seek(filePtr)
        fileName = slpm.read(readSize).decode(encoding="shift-jis", errors="backslashreplace")
        fileName = fileName[:fileName.find(terminator)]
        
        fileName = fileName.replace(" ", "_")

        os.makedirs(f"{dataName}{foldersInfo[i][0]}", exist_ok=True)
        file = open(f"{dataName}{foldersInfo[i][0]}{fileName}", "wb")

        dataFile.seek(fileStart * sector)
        fileData = dataFile.read(fileSize)

        file.write(fileData)

        logFile.write(f"{fileName} {filePtr} {fileSize} {fileStart} {fileEnd}\n")

        seekAddr = seekAddr + 16