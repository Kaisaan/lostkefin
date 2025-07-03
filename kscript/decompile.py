import sys
from parser import opcodes, ConditionalRelativeJump


def bin_to_kscript(bin_file: str, kscript_file: str):
    """
    Convert a .bin file to a .kscript file
    """
    script_indices = []
    script_pointers = []

    fp = open(bin_file, "rb")
    out_fp = open(kscript_file, "w", encoding="utf-8")

    # Parse through absolute pointer table first
    while True:
        if fp.tell() >= 0x2000:
            break
        index = int.from_bytes(fp.read(0x4), "little")
        pointer = int.from_bytes(fp.read(0x4), "little")
        script_indices.append(index)
        script_pointers.append(pointer)
        if index == 0:
            break

    fp.seek(0x2000)
    # fp.seek(0x880b)

    relative_pointers = []
    while True:
        current_pointer = fp.tell()

        if (current_pointer - 0x2000) in script_pointers:
            i = script_pointers.index(current_pointer - 0x2000)
            index = script_indices[i]
            out_fp.write(f"LABEL_{index:06x}:\n")
        if current_pointer in relative_pointers:
            if (current_pointer - 0x2000) in script_pointers:
                sys.exit(
                    "Instruction is both a jump target and a script pointer. Everdred needs to handle this apparently"
                )
            idx = relative_pointers.index(current_pointer)
            out_fp.write(f"JMP_{idx:06x}\n")

        op_byte = fp.read(1)

        if op_byte == b"":
            break
        opcode = int.from_bytes(op_byte, "little")

        if opcode not in opcodes:
            raise ValueError(f"Unknown opcode {hex(opcode)}")
        op = opcodes[opcode].from_io(fp)

        if isinstance(op, ConditionalRelativeJump):
            jump_target = fp.tell() - 0x4 + op.target
            # Rewrite target to be an index
            op.target = len(relative_pointers)
            relative_pointers.append(jump_target)
        out_fp.write(f"  {str(op)}\n")

    out_fp.close()
    fp.close()


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python decompile.py stage00.bin stage00.kscript")
        sys.exit(1)
    bin_to_kscript(sys.argv[1], sys.argv[2])
