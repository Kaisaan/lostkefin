def read_string(io, length):
    # Replace b'\xff\xfdXX' with b"<sleep XX>" where XX is a number
    
    unknown = io.read(1)
    if unknown != b'\x80':
        raise ValueError(f"Unknown byte {unknown} is not 0x80 in read_string")

    s = io.read(length)

    out = s[:]
    for i in range(len(s) - 2):
        if s[i] == 0xff and s[i + 1] == 0xfd:
            duration = s[i + 2]
            sleep_str = f"<sleep {duration}>"
            out = out.replace(s[i:i + 3], sleep_str.encode("shift-jis"))

    return out.decode("shift-jis")

class Unkn_4():
    opcode = 0x4
    def __init__(self):
        pass

    @classmethod
    def from_io(cls, _io):
        return cls()

class CutsceneText():
    opcode = 0xa
    def __init__(self, arg_bytes, text):
        self.arg_bytes = arg_bytes
        self.text = text

    @classmethod
    def from_io(cls, io):
        arg_bytes = io.read(4)
        s_len = int.from_bytes(io.read(1), 'little')
        
        text = read_string(io, s_len)
        return cls(arg_bytes, text)

class Unkn_7():
    opcode = 0x7
    def __init__(self, arg: int):
        self.arg = arg

    @classmethod
    def from_io(cls, io):
        arg = int.from_bytes(io.read(1), 'little')
        return cls(arg)

class Unkn_49():
    opcode = 0x49
    def __init__(self, arg_bytes: bytes):
        self.arg_bytes = arg_bytes
        
    @classmethod
    def from_io(cls, io):
        arg_bytes = io.read(2)
        return cls(arg_bytes)

class Unkn_5():
    opcode = 0x5
    def __init__(self):
        pass
    @classmethod
    def from_io(cls, io):
        return cls()

class Unkn_6():
    opcode = 0x6
    def __init__(self):
        pass
    @classmethod
    def from_io(cls, io):
        return cls()

class Unkn_C():
    opcode = 0xc
    def __init__(self):
        pass
    @classmethod
    def from_io(cls, io):
        return cls()

class Unkn_E():
    opcode = 0xe
    def __init__(self, arg: int):
        self.arg = arg
    @classmethod
    def from_io(cls, io):
        arg = int.from_bytes(io.read(1), 'little')
        return cls(arg)

class Unkn_10():
    opcode = 0x10
    def __init__(self):
        pass
    @classmethod
    def from_io(cls, io):
        return cls()

class Unkn_11():
    opcode = 0x11
    def __init__(self):
        pass
    @classmethod
    def from_io(cls, io):
        return cls()

class Unkn_12():
    opcode = 0x12
    def __init__(self):
        pass
    @classmethod
    def from_io(cls, io):
        return cls()

class Unkn_15():
    opcode = 0x15
    def __init__(self, arg_bytes: bytes):
        self.arg_bytes = arg_bytes
    @classmethod
    def from_io(cls, io):
        arg_bytes = io.read(2)
        return cls(arg_bytes)

class Unkn_18():
    opcode = 0x18
    def __init__(self, arg_bytes: bytes):
        self.arg_bytes = arg_bytes
    @classmethod
    def from_io(cls, io):
        arg_bytes = io.read(3)
        return cls(arg_bytes)

class Unkn_1D():
    opcode = 0x1d
    def __init__(self, arg_bytes: bytes):
        self.arg_bytes = arg_bytes
    @classmethod
    def from_io(cls, io):
        arg_bytes = io.read(3)
        return cls(arg_bytes)

class Unkn_1E():
    opcode = 0x1e
    def __init__(self, arg_bytes: bytes):
        self.arg_bytes = arg_bytes
    @classmethod
    def from_io(cls, io):
        arg_bytes = io.read(9)
        return cls(arg_bytes)

class Unkn_20():
    opcode = 0x20
    def __init__(self, arg_bytes: bytes):
        self.arg_bytes = arg_bytes
    @classmethod
    def from_io(cls, io):
        arg_bytes = io.read(3)
        return cls(arg_bytes)

class Choice():
    opcode = 0x28
    def __init__(self, arg_bytes, question_text, responses: list, indices:list):
        self.arg_bytes = arg_bytes
        self.question_text = question_text
        self.responses = responses
        self.indices = indices
    @classmethod
    def from_io(cls, io):
        arg_bytes = io.read(2)
        s_len = int.from_bytes(io.read(1), 'little')

        question_text = read_string(io, s_len)

        responses = []
        indices = []
        while True:
            s_len = int.from_bytes(io.read(1), 'little')

            if s_len == 255:
                break
            response = read_string(io, s_len)
            index = int.from_bytes(io.read(4), 'little')
            responses.append(response)
            indices.append(index)
            if index == 0:
                break
        return cls(arg_bytes, question_text, responses, indices)

class Unkn_2F():
    opcode = 0x2f
    def __init__(self, arg_bytes: bytes):
        self.arg_bytes = arg_bytes
    @classmethod
    def from_io(cls, io):
        arg_bytes = io.read(2)
        return cls(arg_bytes)

class Unkn_30():
    opcode = 0x30
    def __init__(self, arg: int):
        self.arg = arg
    @classmethod
    def from_io(cls, io):
        arg = int.from_bytes(io.read(1), 'little')
        return cls(arg)

class Unkn_31():
    opcode = 0x31
    def __init__(self, arg: int):
        self.arg = arg
    @classmethod
    def from_io(cls, io):
        arg = int.from_bytes(io.read(1), 'little')
        return cls(arg)

class Unkn_36():
    opcode = 0x36
    def __init__(self, arg_bytes: bytes):
        self.arg_bytes = arg_bytes
    @classmethod
    def from_io(cls, io):
        arg_bytes = io.read(10)
        return cls(arg_bytes)

class CameraPan():
    opcode = 0x37
    def __init__(self, arg_bytes: bytes):
        self.arg_bytes = arg_bytes
    @classmethod
    def from_io(cls, io):
        arg_bytes = io.read(10)
        return cls(arg_bytes)

class QuestionResponse():
    opcode = 0x3b
    def __init__(self, arg_bytes, text):
        self.arg_bytes = arg_bytes
        self.text = text
    @classmethod
    def from_io(cls, io):
        arg_bytes = io.read(2)
        s_len = int.from_bytes(io.read(1), 'little')
        text = read_string(io, s_len)
        return cls(arg_bytes, text) 


class ConditionalRelativeJump():
    opcode = 0x3c
    def __init__(self, target: int, type: int):
        # Target is how many bytes 
        self.target = target
        self.type = type
    @classmethod
    def from_io(cls, io):
        target = int.from_bytes(io.read(2), 'little')
        type = int.from_bytes(io.read(2), 'little')
        if type != 0x46:
            raise ValueError(f"Unknown conditional jump type {type}")

        return cls(target, type)
    

class Unkn_3F():
    opcode = 0x3f
    def __init__(self, arg: int):
        self.arg = arg
    @classmethod
    def from_io(cls, io):
        arg = int.from_bytes(io.read(1), 'little')
        return cls(arg)

class Unkn_40():
    opcode = 0x40
    def __init__(self, arg: int):
        self.arg = arg
    @classmethod
    def from_io(cls, io):
        arg = int.from_bytes(io.read(1), 'little')
        return cls(arg)

class UnconditionalJump():
    opcode = 0x44
    def __init__(self, target_index: int):
        self.target_index = target_index
    @classmethod
    def from_io(cls, io):
        target_index = int.from_bytes(io.read(4), 'little')
        return cls(target_index)

class Unkn_45():
    opcode = 0x45
    def __init__(self, arg: int):
        self.arg = arg
    @classmethod
    def from_io(cls, io):
        arg = int.from_bytes(io.read(1), 'little')
        return cls(arg)

class Unkn_47():
    opcode = 0x47
    def __init__(self, arg: int):
        self.arg = arg
    @classmethod
    def from_io(cls, io):
        arg = int.from_bytes(io.read(1), 'little')
        return cls(arg)

class Unkn_48():
    opcode = 0x48
    def __init__(self, arg: int):
        self.arg = arg
    @classmethod
    def from_io(cls, io):
        arg = int.from_bytes(io.read(1), 'little')
        return cls(arg)

class Unkn_4C():
    opcode = 0x4c
    def __init__(self, arg: int):
        self.arg = arg
    @classmethod
    def from_io(cls, io):
        arg = int.from_bytes(io.read(1), 'little')
        return cls(arg)

class Unkn_4D():
    opcode = 0x4d
    def __init__(self, arg: int):
        self.arg = arg
    @classmethod
    def from_io(cls, io):
        arg = int.from_bytes(io.read(1), 'little')
        return cls(arg)

class Unkn_4E():
    opcode = 0x4e
    def __init__(self):
        pass
    @classmethod
    def from_io(cls, io):
        return cls()

class Unkn_4F():
    opcode = 0x4f
    def __init__(self, arg_bytes: bytes):
        self.arg_bytes = arg_bytes
    @classmethod
    def from_io(cls, io):
        arg_bytes = io.read(2)
        return cls(arg_bytes)

class Unkn_50():
    opcode = 0x50
    def __init__(self, arg_bytes: bytes):
        self.arg_bytes = arg_bytes
    @classmethod
    def from_io(cls, io):
        arg_bytes = io.read(6)
        return cls(arg_bytes)

class Unkn_51():
    opcode = 0x51
    def __init__(self):
        pass
    @classmethod
    def from_io(cls, io):
        return cls()

class TextBubble():
    opcode = 0x52
    def __init__(self, arg_bytes, text):
        self.arg_bytes = arg_bytes
        self.text = text
    @classmethod
    def from_io(cls, io):
        arg_bytes = io.read(2)
        s_len = int.from_bytes(io.read(1), 'little')
        unknown = io.read(1)
        if unknown != b'\x80':
            raise ValueError(f"Unknown byte {unknown} is not 0x80 in Unkn_52")
        text = io.read(s_len).decode('shift-jis')
        return cls(arg_bytes, text)

class Unkn_53():
    opcode = 0x53
    def __init__(self, arg_bytes: bytes):
        self.arg_bytes = arg_bytes
    @classmethod
    def from_io(cls, io):
        arg_bytes = io.read(2)
        return cls(arg_bytes)

class Unkn_55():
    opcode = 0x55
    def __init__(self):
        pass
    @classmethod
    def from_io(cls, io):
        return cls()

class Unkn_59():
    opcode = 0x59
    def __init__(self, arg_bytes: bytes):
        self.arg_bytes = arg_bytes
    @classmethod
    def from_io(cls, io):
        arg_bytes = io.read(2)
        return cls(arg_bytes)

class EndVNSection():
    opcode = 0x5a
    def __init__(self):
        pass
    @classmethod
    def from_io(cls, io):
        return cls()

class Unkn_60():
    opcode = 0x60
    def __init__(self, arg_bytes: bytes):
        self.arg_bytes = arg_bytes
    @classmethod
    def from_io(cls, io):
        arg_bytes = io.read(2)
        return cls(arg_bytes)

class EndScript():
    opcode = 0xff
    def __init__(self):
        pass
    @classmethod
    def from_io(cls, io):
        return cls()

opcodes = {
    0x4: Unkn_4,
    0x7: Unkn_7,
    0xa: CutsceneText,
    0xc: Unkn_C,
    0x5: Unkn_5,
    0x6: Unkn_6,
    0xe: Unkn_E,
    0x10: Unkn_10,
    0x11: Unkn_11,
    0x12: Unkn_12,
    0x15: Unkn_15,
    0x18: Unkn_18,
    0x1d: Unkn_1D,
    0x1e: Unkn_1E,
    0x20: Unkn_20,
    0x28: Choice,
    0x2f: Unkn_2F,
    0x30: Unkn_30,
    0x31: Unkn_31,
    0x36: Unkn_36,
    0x37: CameraPan,
    0x3b: QuestionResponse,
    0x3c: ConditionalRelativeJump,
    0x3f: Unkn_3F,
    0x40: Unkn_40,
    0x44: UnconditionalJump,
    0x45: Unkn_45,
    0x47: Unkn_47,
    0x48: Unkn_48,
    0x49: Unkn_49,
    0x4c: Unkn_4C,
    0x4d: Unkn_4D,
    0x4e: Unkn_4E,
    0x4f: Unkn_4F,
    0x50: Unkn_50,
    0x51: Unkn_51,
    0x52: TextBubble,
    0x53: Unkn_53,
    0x55: Unkn_55,
    0x59: Unkn_59,
    0x5a: EndVNSection,
    0x60: Unkn_60,
    0xff: EndScript,
}

def parse_script(fp, index, pointer):
    print(f"parsing script {index} at {hex(pointer)}")
    fp.seek(0x2000 + pointer)
    while True:
        opcode = int.from_bytes(fp.read(1), 'little')
        if opcode == 0xff:
            break
        if opcode not in opcodes:
            raise ValueError(f"Unknown opcode {hex(opcode)}")
        op = opcodes[opcode].from_io(fp)
        print(op)
    print("done")

scripts = []
with open("../stage00.bin", "rb") as f:
    while True:
        if f.tell() >= 0x2000:
            break
        index = int.from_bytes(f.read(0x4), 'little')
        pointer = int.from_bytes(f.read(0x4), 'little')
        scripts.append((index, pointer))
        if index == 0:
            break
    for index, pointer in scripts:
        parse_script(f, index, pointer)

