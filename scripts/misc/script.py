def extract(stagefile, logfile, data):  
    script = open(f"scripts/{stagefile}", "rb")

    log = open(f"scripts/{logfile}", "w")
    log.write(f"{stagefile} header info\n")

    currentread = 0x0

    endcode = 0x0
    endsize = 0x2

    count = 0x0
    val1 = 0x0
    val2 = 0x0
    trueoffset = 0x0
    dataoffset = data

    offset = 0x2000

    known = [b'\x00\xff', b'\x32\xff', b'\x11\xff', b'\x02\xff', b'\x4E\xff', b'\x01\xff', b'\x64\xff', b'\x04\xff', b'\x55\xff', b'\x07\xff', b'\x06\xff', b'\x56\xff']
    ignore = [b'\xa5\xff']

    #known = [b'\x00\x00\x00\xff', b'\x02\x00\x00\xff', b'\x04\x00\x00\xff', b'\x00\x4E\x4E\xff']
    #ignore = [b'\x68\x81\xa5\xff', b'\x49\x81\xa5\xff', b'\x42\x81\xa5\xff', b'\x48\x81\xa5\xff',]

    isknown = ""

    while count < 0x400:

        script.seek(currentread)
        
        val1 = script.read(4)
        val2 = script.read(4)

        val1 = int.from_bytes(val1, "little")
        val2 = int.from_bytes(val2, "little")

        trueoffset = val2 + offset
        dataoffset = dataoffset + trueoffset

        script.seek(trueoffset - endsize)
        endcode = script.read(endsize)

        if endcode in known:
            isknown = "KNOWN"
        elif endcode in ignore:
            isknown = "ignore"
        else:
            isknown = "NEW"

        if val1 == val2 == 0:
            break

        log.write(f"Entry Order {count:X}\tEntry Order Offset {currentread:X}\tEntry Number {val1:X}\tOffset {val2:X}\tTrue Offset {trueoffset:X}\tDATA.BIN Offset {dataoffset:X}\tEnd code {endcode}\t{isknown}\n")

        count = count + 1

        currentread = currentread + 0x08

extract("stage00.bin", "script00.txt", 0x94BA800)
extract("stage10.bin", "script10.txt", 0x94CC000)
extract("stage20.bin", "script20.txt", 0x94D4800)
extract("stage30.bin", "script30.txt", 0x94DE000)
extract("stage40.bin", "script40.txt", 0x94E1800)
extract("stage50.bin", "script50.txt", 0x94EB800)
extract("stage60.bin", "script60.txt", 0x94F3000)
extract("stage70.bin", "script70.txt", 0x94FC800)
extract("stage80.bin", "script80.txt", 0x9502000)
extract("stage90.bin", "script90.txt", 0x950E800)
extract("stagea0.bin", "scripta0.txt", 0x9516800)
extract("stageb0.bin", "scriptb0.txt", 0x9519000)