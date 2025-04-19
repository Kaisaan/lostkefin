slpm = open("extracted/SLPM_663.60", "rb")

def pointer(address):

    ptrsize = 0x4
    ptr = 0x0
    invalid = [0, 1]
    trueptr = 0x0
    baseptr = 0xFFF80
    readsize = 32
    terminator = "\x00"
    text = ""

    slpm.seek(address)
    ptr = slpm.read(ptrsize)
    ptr = int.from_bytes(ptr, "little")

    if ptr in invalid:
        return "invalid"

    trueptr = ptr - baseptr

    slpm.seek(trueptr)
    text = slpm.read(readsize)
    text = text.decode(encoding="shift-jis", errors="backslashreplace")
    text = text[:text.find(terminator)]

    return f"address {address:X}\tvalue {ptr:X}\tpointer {trueptr:X}\ttext {text}"


startptr = 0x2298E0
read = startptr
endptr = 0x229A00

index = 0x0

log = open("chars.txt", "w", encoding="shift-jis")
log.write("Characters:\n")

while read < endptr: 

    print(f"{read:X}")
    if (pointer(read) == "invalid"):
        pass
    
    else:
        log.write(f"{pointer(read)}\t{index:X}\n")

    index += 0x1
    read += 0x4
