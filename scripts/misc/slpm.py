import sys
import csv

slpm = open("extracted/SLPM_663.60", "rb")

start = sys.argv[1]
end = sys.argv[2]

out = sys.argv[3]

csvFile = open(f"{out}.csv", "w", newline="", encoding="utf-8")
writer = csv.writer(csvFile)

writer.writerow(["Offset", "JP Text", "EN Text", "Comments"])

#start = 0x2C1C70
#end = 0x2C1CF0#0x2C2F60

start = int(start, 16)
end = int(end, 16)

if end < start:
    exit("end can't be before start")

slpm.seek(start)

org = slpm.tell()

#print(f"0x{org:X}")

buffer = bytearray()
text = ""

while slpm.tell() < end:
    byte = slpm.read(0x01)
    #org = slpm.tell()
    if byte != b"\x00":
        buffer += byte
        #print(byte)
    elif buffer != b"": 
        #print(buffer)
        length = len(buffer)
        org = slpm.tell() - length - 0x1 # Minus one because we read the first null byte
        text = buffer.decode(encoding="shift-jis", errors="backslashreplace")
        #print(text)
        
        writer.writerow([f"{org:X}", f"{text}", "", ""])
        
        #csv.write(f".orga 0x{org:X}\n.str \"{text}\"\n\n")
        buffer = bytearray()
    



"""
mem = open("mem.txt", "w", encoding="utf-8")


items = open("items.txt", "w", encoding="utf-8")


miscText = open("slpm_text.txt", "w", encoding="utf-8")

gallery = open("gallery.txt", "w", encoding="utf-8")

slpm.seek(0x002638D0)

while (slpm.tell() < 0x267240):
    buffer = slpm.read(32)
    text = buffer.decode(encoding="shift-jis", errors="backslashreplace")
    text = text.replace("\x00", "\n")

    miscText.write(text)

slpm.seek(0x002C1C70)

while (slpm.tell() < 0x2C2F60):
    buffer = slpm.read(32)
    text = buffer.decode(encoding="shift-jis", errors="backslashreplace")
    text = text.replace("\x00", "\n")

    gallery.write(text)


slpm.seek(0x00265A00)

while (slpm.tell() < 0x267300):

    buffer = (slpm.read(0x1900))
    #buffer = buffer.replace(b"\x0A", b"\x0A\x01")
    text = buffer.decode(encoding="shift-jis", errors="backslashreplace")
    
    text = text.replace("\n", "\\n")
    text = text.replace("\x00", "\n")

    items.write(text)


slpm.seek(0x0025FBF0)

while (slpm.tell() < 0x2608F0):
    buffer = slpm.read(0xD00)
    text = buffer.decode(encoding="shift-jis", errors="backslashreplace")
    text = text.replace("\n", "\\n")
    text = text.replace("\x00", "\n")

    mem.write(text)

"""

