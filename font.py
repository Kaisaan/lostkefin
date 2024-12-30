import os

slpm = open("extracted/SLPM_663.60", "rb")

table = open("font.tbl", "w", encoding="shift-jis")

start = 0x1A31F0
end = 0x1A3E98

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