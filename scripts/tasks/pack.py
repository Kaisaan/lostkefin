import sys
import os
import math

UNUSED_FILE_NAME = "adol_d_anm.bin"
EXPANDED_FILE_NAME = "adol_t_anm.bin"
ADDED_FOLDER_NAME = "/ending/"
ADDED_FILE_NAME = "ys5ed12_anm.bin"
UNUSED_SECTOR_SIZE = 938
FOLDER_TABLE_OFFSET = 0x001875E0
FILE_TABLE_OFFSET = 0x001829D0
BASE_PTR = 0xFFF80


def pack(data_file: str):
    slpm = open(os.path.join("translated", "SLPM_663.60"), "r+b")

    dataName = os.path.basename(data_file)

    dataFile = open(os.path.join("translated", dataName), "wb")

    dataName = dataName.rstrip(".BIN")

    logFile = open(f"{dataName}.txt", "r", encoding="utf-8")

    slpm.seek(FILE_TABLE_OFFSET)

    startSector = 0

    sector = 0x800
    folderTableAddr = FOLDER_TABLE_OFFSET
    reclaimedNamePtr = None

    while True:
        line = logFile.readline()
        if line == "":
            break

        folderInfo = (line).strip("\n").split()

        folderIndex = int(folderInfo[2])
        folderAmount = int(folderInfo[3])
        folderName = folderInfo[0]

        # Reclaim adol_d_anm.bin and use it for the final credits image
        newFolderIndex = folderIndex
        newFolderAmount = folderAmount

        if folderName == "/anm/":
            newFolderAmount -= 1
        elif folderIndex > 0:
            newFolderIndex -= 1

        if folderName == ADDED_FOLDER_NAME:
            newFolderAmount += 1

        slpm.seek(folderTableAddr + 4)
        slpm.write(newFolderIndex.to_bytes(4, byteorder="little"))
        slpm.write(newFolderAmount.to_bytes(4, byteorder="little"))
        folderTableAddr += 12

        slpm.seek(FILE_TABLE_OFFSET + (newFolderIndex * 16))

        for i in range(folderAmount):
            line = logFile.readline()
            fileInfo = (line).strip("\n").split()

            fileName = fileInfo[0]

            if fileName == UNUSED_FILE_NAME:
                reclaimedNamePtr = int(fileInfo[1])
                continue

            filePath = f"{dataName}{folderName}{fileName}"
            filePtr = int(fileInfo[1])
            if fileName == ADDED_FILE_NAME and reclaimedNamePtr is not None:
                filePtr = reclaimedNamePtr

            file = open(filePath, "rb")

            fileData = file.read()

            fileSize = len(fileData)

            sectorSize = math.ceil((len(fileData)) / sector)

            if fileName == EXPANDED_FILE_NAME:
                sectorSize += UNUSED_SECTOR_SIZE

            padding = bytes((sectorSize * sector) - fileSize)

            dataFile.write(fileData)
            dataFile.write(padding)

            filePtr = filePtr + BASE_PTR

            filePtr = filePtr.to_bytes(4, byteorder="little")
            fileSize = fileSize.to_bytes(4, byteorder="little")
            startSectorBytes = startSector.to_bytes(4, byteorder="little")
            sectorSizeBytes = sectorSize.to_bytes(4, byteorder="little")

            slpm.write(filePtr)
            slpm.write(fileSize)
            slpm.write(startSectorBytes)
            slpm.write(sectorSizeBytes)

            startSector = startSector + (sectorSize)

        if folderName == ADDED_FOLDER_NAME:
            if reclaimedNamePtr is None:
                raise RuntimeError(f"Could not find {UNUSED_FILE_NAME} filename slot")

            nameData = ADDED_FILE_NAME.encode("ascii") + b"\x00"
            nextNamePtr = 2384488
            slotSize = nextNamePtr - reclaimedNamePtr
            if len(nameData) > slotSize:
                raise RuntimeError(
                    f"{ADDED_FILE_NAME} needs {len(nameData)} bytes, "
                    f"but reclaimed slot only has {slotSize}"
                )

            slpm.seek(reclaimedNamePtr)
            slpm.write(nameData.ljust(slotSize, b"\x00"))

            filePath = f"{dataName}{folderName}{ADDED_FILE_NAME}"
            file = open(filePath, "rb")
            fileData = file.read()
            fileSize = len(fileData)
            sectorSize = math.ceil(fileSize / sector)
            padding = bytes((sectorSize * sector) - fileSize)

            dataFile.write(fileData)
            dataFile.write(padding)

            slpm.seek(FILE_TABLE_OFFSET + ((newFolderIndex + newFolderAmount - 1) * 16))
            slpm.write((reclaimedNamePtr + BASE_PTR).to_bytes(4, byteorder="little"))
            slpm.write(fileSize.to_bytes(4, byteorder="little"))
            slpm.write(startSector.to_bytes(4, byteorder="little"))
            slpm.write(sectorSize.to_bytes(4, byteorder="little"))

            startSector = startSector + sectorSize


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: pack.py <file.bin>")
        sys.exit(1)
    pack(sys.argv[1])
