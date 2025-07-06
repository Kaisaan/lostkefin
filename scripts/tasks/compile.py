import sys


# Handle imports for both module and script execution
try:
    # When imported as a module
    from .parser import line_to_op, ConditionalRelativeJump
except ImportError:
    # When run as a script
    from parser import line_to_op, ConditionalRelativeJump


def kscript_to_bin(kscript_file: str, bin_file: str):
    """
    Convert a .kscript file to a .bin file
    """
    f = open(kscript_file, "r", encoding="utf-8")
    out_f = open(bin_file, "wb")

    out_f.seek(0x2000)
    ptrs = []
    relative_jump_locations = []
    relative_jump_targets = {}
    for line in f:
        if "LABEL_" in line:
            line = line.strip()
            line = line.split("_")[1].split(":")[0]

            index = int(line, 16)
            ptr = out_f.tell() - 0x2000
            ptrs.append((index, ptr))
            continue
        if "JMP_" in line:
            # These are handled last so we just keep track of the locations
            line = line.strip()
            line = line.split("_")[1].split(":")[0]
            index = int(line, 16)
            relative_jump_targets[index] = out_f.tell()
            continue

        op = line_to_op(line)
        if isinstance(op, ConditionalRelativeJump):
            relative_jump_locations.append(out_f.tell())

        out_f.write(op.to_bytes())
    out_f.seek(0)
    for index, ptr in ptrs:
        out_f.write(index.to_bytes(4, "little"))
        out_f.write(ptr.to_bytes(4, "little"))

    for idx, location in enumerate(relative_jump_locations):
        # Seek to the ptr location
        out_f.seek(location + 1)

        # print(relative_jump_targets)
        # Calculate how far forward the jump is
        distance = relative_jump_targets[idx] - out_f.tell()

        # Write it
        out_f.write(distance.to_bytes(2, "little"))

    out_f.close()
    f.close()


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python compile.py stage00.kscript stage00.bin")
        sys.exit(1)
    kscript_to_bin(sys.argv[1], sys.argv[2])
