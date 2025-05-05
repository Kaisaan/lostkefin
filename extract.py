# todo: extract all the files into their appropirate folders (using fileorder)
# also turn the functions into while loops? pass start and end address

import os

slpm = open("extracted/SLPM_663.60", "rb")

logfile = open("logfile.txt", "w", encoding="shift-jis")

baseptr = 0xFFF80
sector = 0x800
filenamesize = 32
terminator = "\x00"

def extractfile(address, file):

    os.makedirs(f"{file}", exist_ok=True)

    datafile = open(f"extracted/{file}.BIN", 'rb')

    slpm.seek(address)
    filenameptr = slpm.read(4)
    filesize = slpm.read(4)
    filesectorstart = slpm.read(4)
    filesectorsize = slpm.read(4)

    filenameptr = int.from_bytes(filenameptr, "little")
    filesize = int.from_bytes(filesize, "little")
    filesectorstart = int.from_bytes(filesectorstart, "little")
    filesectorsize = int.from_bytes(filesectorsize, "little")
    
    filenameloc = filenameptr - baseptr
    slpm.seek(filenameloc)
    filename = slpm.read(filenamesize)
    filename = filename.decode(encoding="shift-jis", errors="backslashreplace")
    filename = filename[:filename.find(terminator)]

    filesectorstart = filesectorstart * sector
    filesectorsize = filesectorsize * sector

    datafile.seek(filesectorstart)
    filedata = datafile.read(filesize)

    newfile = open(f"{file}/{filename}", "wb")
    newfile.write(filedata)
    newfile.close

    return f"Address: {address:X}\tFile name: {filename}\tFilename location: {filenameloc:X}\tFilename pointer: {filenameptr:X}\tFile size: {filesize:X}\tFile data start in {file}.BIN: {filesectorstart:X}\tFile data sector size: {filesectorsize:X}"


fileorder = 0

fileptrstart = 0x001829D0
fileptrend = 0x001875E0

fileptr = fileptrstart

logfile.write("\nDATA.BIN Files\n\n")

while fileptr < fileptrend:

    logfile.write(f"{extractfile(fileptr, "DATA")}\tindex {fileorder}\n")

    fileptr += 16
    fileorder += 1

def extractfolder(address, file):

    slpm.seek(address)
    foldernameptr = slpm.read(4)
    folderorderstart = slpm.read(4)
    foldercount = slpm.read(4)

    foldernameptr = int.from_bytes(foldernameptr, "little")
    folderorderstart = int.from_bytes(folderorderstart, "little")
    foldercount = int.from_bytes(foldercount, "little")
    
    foldernameloc = foldernameptr - baseptr
    slpm.seek(foldernameloc)
    foldername = slpm.read(filenamesize)
    foldername = foldername.decode(encoding="shift-jis", errors="backslashreplace")
    foldername = foldername[:foldername.find(terminator)]

    os.makedirs(f"{file}/{foldername}", exist_ok=True)

    return f"Address: {address:X}\tFolder name: {foldername}\tFoldername location: {foldernameloc:X}\tFilename pointer: {foldernameptr:X}\tFolder Order start {folderorderstart}\tFolder file count: {foldercount}\n"

logfile.write("\nDATA.BIN Folders\n\n")

folderptrstart = 0x001875E0
folderptrend = 0x00187A18

folderptr = folderptrstart

while folderptr < folderptrend:
    logfile.write(f"{extractfolder(folderptr, "DATA")}")

    folderptr += 12

# DATA0.BIN extractions

fileorder = 0

fileptrstart = 0x187A40
fileptrend = 0x18E7C0

fileptr = fileptrstart

logfile.write("\nDATA.BIN Files\n\n")

while fileptr < fileptrend:

    logfile.write(f"{extractfile(fileptr, "DATA0")}\tindex {fileorder}\n")

    fileptr += 16
    fileorder += 1