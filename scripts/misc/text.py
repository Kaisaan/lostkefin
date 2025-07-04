import os
from base64 import b64encode
import csv
import re
import sys

script = open("stage00.bin", "rb")

log = csv.writer(open("stage00.csv", "w", encoding="utf-8"))

fileInfo = os.stat("stage00.bin")

scriptSize = fileInfo.st_size

count = 0x0

index = 0x0
pointer = 0x0

textOffset = 0x0

entrySize = 0x4

scriptOffset = 0x2000

text = ""

pointers = []

while count < 0x400:

    index = script.read(entrySize)
    pointer = script.read(entrySize)

    index = int.from_bytes(index, "little")
    pointer = int.from_bytes(pointer, "little")

    if index == pointer == 0:
        break

    pointers.append([index, pointer])

    count = count + 1

def remove_sleep(b: bytes):
    """
    Find inline sleep opcodes and replace with a string
    """
    out = b[:]
    # Iterate over textBytes with a 3-byte sliding window
    for i in range(len(b) - 2):
        if b[i] == 0xff and b[i + 1] == 0xfd:
            duration = b[i + 2]
            sleep_str = f"<sleep {duration}>"
            out =out.replace(b[i:i + 3], sleep_str.encode("shift-jis"))
    return out

def insert_sleep(b: bytes):
    """

    """

    for sleep_str in re.findall(r"<sleep (\d+)>", b):
        duration = int(sleep_str.group(1))
        b = b.replace(sleep_str.encode("shift-jis"), b"")
    return b

log.writerow(["textPointer", "index", "text", "pre_text", "post_text"])

for i in range(count):
    index = pointers[i][0]
    textPointer = pointers[i][1]
    try:
        nextPointer = pointers[i + 1][1]
        readSize = nextPointer - textPointer
    except IndexError:
        readSize = None
    nextPointer = i + 1

    script.seek(textPointer + scriptOffset)
    textBytes = script.read(readSize)
    # Iterate over textBytes with a 3-byte sliding window
    for i in range(len(textBytes) - 2):
        # Try to find the print opcode by pattern matching
        if textBytes[i] == 0x00 and textBytes[i + 2] == 0x80:
            length = textBytes[i + 1]

            raw_text = textBytes[i + 3:i + 3 + length]
            if len(raw_text) < length:
                # This looked like a text string, but it wasn't. So skip
                continue

            # Replace sleep opcodes with a string
            raw_text = remove_sleep(raw_text)
            text = raw_text.decode(encoding="shift-jis")

            pre_text = b64encode(textBytes[:i]).decode("utf-8")
            post_text = b64encode(textBytes[i + 3 + length:]).decode("utf-8")

            log.writerow([textPointer+scriptOffset, index, text, pre_text, post_text])

            break

def calc_box_size(string_pos: bytes, param_2: list, param_3: list, param_4=None, param_5=None, param_6: bytes = b""):
    cursor_pos = 0
    box_width = 0
    box_height = 0
    bVar5 = False
    idx = 0
    length = len(string_pos)

    def concat11(a, b):
        return (a << 8) | b

    while idx < length and string_pos[idx] != 0:
        current_char = string_pos[idx]
        print(f"current_char: {hex(current_char)}")
        goto_ce38 = False
        if current_char == 10:  # newline
            idx += 1
            box_height += 0x18
            if box_width < cursor_pos:
                box_width = cursor_pos
            cursor_pos = 0
        elif current_char == 0x20:  # space
            if bVar5:
                cursor_pos += 0x14
            else:
                cursor_pos += (0x14 >> 1)
            idx += 1
        elif current_char == 0x81 and idx + 1 < length and string_pos[idx + 1] == 0x40:
            cursor_pos += 0x14
            idx += 2
        elif current_char == 0xff and idx + 1 < length and string_pos[idx + 1] == 0xfd:
            idx += 3
        elif (current_char == 0x23 and idx + 2 < length):
            uVar7 = concat11(string_pos[idx + 1], string_pos[idx + 2])
            if uVar7 in (0x7265, 0x626c, 0x6772, 0x7069, 0x7768, 0x626b, 0x676c, 0x6379, 0x796c):
                idx += 3
            else:
                goto_ce38 = True
        elif current_char == 0x3c and idx + 1 < length:
            bVar2 = string_pos[idx + 1]
            goto_cff8 = False
            if bVar2 == 0x2f and idx + 3 < length:
                bVar3 = string_pos[idx + 2]
                if (bVar3 in (0x46, 0x66)) and string_pos[idx + 3] == 0x3e:
                    idx += 4
                    bVar5 = True
                elif (bVar3 in (0x48, 0x68)) and string_pos[idx + 3] == 0x3e:
                    idx += 4
                elif (bVar3 in (0x42, 0x62)) and string_pos[idx + 3] == 0x3e:
                    idx += 4
                else:
                    goto_cff8 = True
            else:
                goto_cff8 = True
            if goto_cff8:
                if (bVar2 in (0x46, 0x66)) and idx + 2 < length and string_pos[idx + 2] == 0x3e:
                    idx += 3
                    bVar5 = True
                elif (bVar2 in (0x48, 0x68)) and idx + 2 < length and string_pos[idx + 2] == 0x3e:
                    idx += 3
                elif (bVar2 in (0x42, 0x62)) and idx + 2 < length and string_pos[idx + 2] == 0x3e:
                    idx += 3
                elif (bVar2 in (0x57, 0x77)):
                    iVar8 = 2
                    while idx + iVar8 < length and 0x30 <= string_pos[idx + iVar8] <= 0x39:
                        iVar8 += 1
                    if idx + iVar8 < length and string_pos[idx + iVar8] == 0x3e:
                        iVar8 += 1
                    idx += iVar8
                elif (bVar2 in (0x4b, 0x6b)) and idx + 3 < length and (0x30 <= string_pos[idx + 2] <= 0x35) and string_pos[idx + 3] == 0x3e:
                    idx += 4
                else:
                    goto_ce38 = True
        else:
            goto_ce38 = True
        if goto_ce38:
            if current_char < 0x30 or current_char > 0x39:
                if current_char < 0x81:
                    cursor_pos += (0x14 >> 1)
                else:
                    bVar4 = False
                    if param_6:
                        iVar8 = 0
                        while iVar8 + 1 < len(param_6):
                            bVar2 = param_6[iVar8]
                            if bVar2 == 0:
                                break
                            if (current_char == bVar2) and (idx + 1 < length and string_pos[idx + 1] == param_6[iVar8 + 1]):
                                bVar4 = True
                                break
                            iVar8 += 2
                    if not bVar4:
                        cursor_pos += 0x14
                idx += 2
            else:
                cursor_pos += 0x14
                idx += 1
    if cursor_pos != 0:
        box_height += 0x18
    if box_width < cursor_pos:
        box_width = cursor_pos
    param_3[0] = box_height
    param_2[0] = box_width

def main():
    # Open the binary file and seek to 0x2000
    with open('stage00.bin', 'rb') as f:

        for i in range(count):
            if i != 1: 
                continue
            index = pointers[i][0]
            textPointer = pointers[i][1]
            try:
                nextPointer = pointers[i + 1][1]
                readSize = nextPointer - textPointer
            except IndexError:
                readSize = None
            nextPointer = i + 1

            f.seek(textPointer + scriptOffset)
            print(scriptOffset)
            print(hex(f.tell()))
            textBytes = f.read(readSize)

            box_width = [0]
            box_height = [0]
            calc_box_size(textBytes, box_width, box_height, None, None, b"")
            print(f"Box width: {box_width[0]}, Box height: {box_height[0]}")

if __name__ == '__main__':
    main()

