import os

slpm = open("extracted/SLPM_663.60", "rb")
datafile = open('extracted/DATA.BIN', 'rb')

fileptrstart = 0x001829D0
fileptrend = 0x001875E0

fileptr = fileptrstart

baseptr = 0xFFF80
sector = 0x800

fileorder = 0
filenamesize = 32
terminator = "\x00"

logfile = open("logfile.txt", "w", encoding="shift-jis")
logfile.write("\nDATA.BIN Files\n\n")

while fileptr < fileptrend:

    slpm.seek(fileptr)
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

    newfile = open(f"DATA/{filename}", "wb")
    newfile.write(filedata)
    newfile.close

    logfile.write(f"Current Pointer: {fileptr:X}\tFile name: {fileorder:X} {filename}\tFilename location: {filenameloc:X}\tFilename pointer: {filenameptr:X}\tFile size: {filesize:X}\tFile data start in DATA.BIN: {filesectorstart:X}\tFile data sector size: {filesectorsize:X}\n")

    fileptr += 16
    fileorder += 1

logfile.write("\nDATA.BIN Folders\n\n")

folderptrstart = 0x001875E0
folderptrend = 0x00187A18

folderptr = folderptrstart

while folderptr < folderptrend:

    slpm.seek(folderptr)
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

    os.makedirs(f"C:/Users/kaisaan/Downloads/ps2 stuff/lostkefin/DATA/{foldername}", exist_ok=True)

    logfile.write(f"Current Pointer: {folderptr:X}\tFolder name: {foldername}\tFoldername location: {foldernameloc:X}\tFilename pointer: {foldernameptr:X}\tFolder Order start {folderorderstart}\tFolder file count: {foldercount}\n")

    folderptr += 12
