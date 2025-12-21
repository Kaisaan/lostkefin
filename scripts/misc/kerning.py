import csv
# 10px spacing by default
table = [b"\x0a"] * 0x80


with open("kerning.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        c = row[1]
        c_i = ord(c)
        if c_i > 0x80:
            continue
        width = int(row[2])

        # Account of the "squish"
        width = int(round(0.833 * width))
        width+=2

        print(repr(c))
        print(repr(c_i))
        table[c_i] = bytes([width])

with open("kerning.bin", "wb") as f:
    f.write(b"".join(table))