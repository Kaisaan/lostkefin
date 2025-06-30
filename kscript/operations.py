def read_string(io, length):
    # See scriptFormat.md for string format
    flag = int.from_bytes(io.read(1), "little")
    if not flag & 0x80:
        print(hex(io.tell()))
        raise ValueError(f"Unknown byte {flag} is not 0x80 in read_string")

    s = io.read(length)

    out = s[:]
    for i in range(len(s) - 2):
        if s[i] == 0xFF and s[i + 1] == 0xFD:
            duration = s[i + 2]
            sleep_str = f"<sleep {duration}>"
            out = out.replace(s[i : i + 3], sleep_str.encode("shift-jis"))

    return out.decode("shift-jis")


class ScreenEffect:
    opcode = 0x2

    def __init__(self, effect_type: int):
        self.effect_type = effect_type

    @classmethod
    def from_io(cls, io):
        effect_type = int.from_bytes(io.read(1), "little")
        return cls(effect_type)


class ScreenEffect2:
    opcode = 0x3

    def __init__(self, effect_type: int):
        self.effect_type = effect_type

    @classmethod
    def from_io(cls, io):
        effect_type = int.from_bytes(io.read(1), "little")
        return cls(effect_type)


class Unkn_4:
    opcode = 0x4

    def __init__(self):
        pass

    @classmethod
    def from_io(cls, _io):
        return cls()


class CutsceneText:
    opcode = 0xA

    def __init__(self, arg_bytes, text):
        self.arg_bytes = arg_bytes
        self.text = text

    @classmethod
    def from_io(cls, io):
        arg_bytes = io.read(4)
        s_len = int.from_bytes(io.read(1), "little")

        text = read_string(io, s_len)
        return cls(arg_bytes, text)


class Unkn_5:
    opcode = 0x5

    def __init__(self):
        pass

    @classmethod
    def from_io(cls, io):
        return cls()


class Unkn_6:
    opcode = 0x6

    def __init__(self):
        pass

    @classmethod
    def from_io(cls, io):
        return cls()


class Unkn_7:
    opcode = 0x7

    def __init__(self, arg: int):
        self.arg = arg

    @classmethod
    def from_io(cls, io):
        arg = int.from_bytes(io.read(1), "little")
        return cls(arg)


class Debug:
    opcode = 0x9

    def __init__(self, debug_str: str):
        self.debug_str = debug_str

    @classmethod
    def from_io(cls, io):
        debug_str = b""
        while True:
            byte = io.read(1)
            if byte == b"\x00":
                break
            debug_str += byte
        try:
            debug_str = debug_str.decode("ascii")
        except UnicodeDecodeError:
            raise ValueError(f"Debug string: {debug_str} is not ASCII")
        return cls(debug_str)


class Unkn_B:
    opcode = 0xB

    def __init__(self):
        pass

    @classmethod
    def from_io(cls, io):
        return cls()


class Unkn_C:
    opcode = 0xC

    def __init__(self):
        pass

    @classmethod
    def from_io(cls, io):
        return cls()


class Unkn_E:
    opcode = 0xE

    def __init__(self, arg: int):
        self.arg = arg

    @classmethod
    def from_io(cls, io):
        arg = int.from_bytes(io.read(1), "little")
        return cls(arg)


class Unkn_10:
    opcode = 0x10

    def __init__(self):
        pass

    @classmethod
    def from_io(cls, io):
        return cls()


class Unkn_11:
    opcode = 0x11

    def __init__(self):
        pass

    @classmethod
    def from_io(cls, io):
        return cls()


class Unkn_12:
    opcode = 0x12

    def __init__(self):
        pass

    @classmethod
    def from_io(cls, io):
        return cls()


class Unkn_14:
    opcode = 0x14

    def __init__(self, arg: int):
        pass

    @classmethod
    def from_io(cls, io):
        arg = int.from_bytes(io.read(1), "little")
        return cls(arg)


class Unkn_15:
    opcode = 0x15

    def __init__(self, arg_bytes: bytes):
        self.arg_bytes = arg_bytes

    @classmethod
    def from_io(cls, io):
        arg_bytes = io.read(2)
        return cls(arg_bytes)


class Unkn_16:
    opcode = 0x16

    def __init__(self, arg_bytes: bytes):
        self.arg_bytes = arg_bytes

    @classmethod
    def from_io(cls, io):
        arg_bytes = io.read(3)
        return cls(arg_bytes)


class PromptBubble:
    opcode = 0x17

    def __init__(self, arg_bytes: bytes):
        self.arg_bytes = arg_bytes

    @classmethod
    def from_io(cls, io):
        arg_bytes = io.read(2)
        return cls(arg_bytes)


class Unkn_18:
    opcode = 0x18

    def __init__(self, arg_bytes: bytes):
        self.arg_bytes = arg_bytes

    @classmethod
    def from_io(cls, io):
        arg_bytes = io.read(3)
        return cls(arg_bytes)


class Unkn_1C:
    opcode = 0x1C

    def __init__(self, arg_bytes: bytes):
        self.arg_bytes = arg_bytes

    @classmethod
    def from_io(cls, io):
        arg_bytes = io.read(4)
        return cls(arg_bytes)


class Unkn_1D:
    opcode = 0x1D

    def __init__(self, arg_bytes: bytes):
        self.arg_bytes = arg_bytes

    @classmethod
    def from_io(cls, io):
        arg_bytes = io.read(3)
        return cls(arg_bytes)


class Unkn_1E:
    opcode = 0x1E

    def __init__(self, arg_bytes: bytes):
        self.arg_bytes = arg_bytes

    @classmethod
    def from_io(cls, io):
        arg_bytes = io.read(9)
        return cls(arg_bytes)


class Unkn_20:
    opcode = 0x20

    def __init__(self, arg_bytes: bytes):
        self.arg_bytes = arg_bytes

    @classmethod
    def from_io(cls, io):
        arg_bytes = io.read(3)
        return cls(arg_bytes)


class BubbleChoice:
    opcode = 0x27

    def __init__(self, arg_bytes, question_text, responses: list, indices: list):
        self.arg_bytes = arg_bytes
        self.question_text = question_text
        self.responses = responses
        self.indices = indices

    @classmethod
    def from_io(cls, io):
        arg_bytes = io.read(4)
        s_len = int.from_bytes(io.read(1), "little")

        question_text = read_string(io, s_len)

        responses = []
        indices = []
        while True:
            s_len = int.from_bytes(io.read(1), "little")

            if s_len == 255:
                break
            response = read_string(io, s_len)
            index = int.from_bytes(io.read(4), "little")
            responses.append(response)
            indices.append(index)
            if index == 0:
                break
        return cls(arg_bytes, question_text, responses, indices)


class Choice:
    opcode = 0x28

    def __init__(self, arg_bytes, question_text, responses: list, indices: list):
        self.arg_bytes = arg_bytes
        self.question_text = question_text
        self.responses = responses
        self.indices = indices

    @classmethod
    def from_io(cls, io):
        arg_bytes = io.read(2)
        s_len = int.from_bytes(io.read(1), "little")

        question_text = read_string(io, s_len)

        responses = []
        indices = []
        while True:
            s_len = int.from_bytes(io.read(1), "little")

            if s_len == 255:
                break
            response = read_string(io, s_len)
            index = int.from_bytes(io.read(4), "little")
            responses.append(response)
            indices.append(index)
            if index == 0:
                break
        return cls(arg_bytes, question_text, responses, indices)


class BubbleChoice2:
    opcode = 0x29

    def __init__(self, arg_bytes, question_text, responses: list, indices: list):
        self.arg_bytes = arg_bytes
        self.question_text = question_text
        self.responses = responses
        self.indices = indices

    @classmethod
    def from_io(cls, io):
        arg_bytes = io.read(2)
        s_len = int.from_bytes(io.read(1), "little")

        question_text = read_string(io, s_len)

        responses = []
        indices = []
        while True:
            s_len = int.from_bytes(io.read(1), "little")

            if s_len == 255:
                break
            response = read_string(io, s_len)
            index = int.from_bytes(io.read(4), "little")
            responses.append(response)
            indices.append(index)
            if index == 0:
                break
        return cls(arg_bytes, question_text, responses, indices)


class Unkn_2F:
    opcode = 0x2F

    def __init__(self, arg_bytes: bytes):
        self.arg_bytes = arg_bytes

    @classmethod
    def from_io(cls, io):
        arg_bytes = io.read(2)
        return cls(arg_bytes)


class Unkn_30:
    opcode = 0x30

    def __init__(self, arg: int):
        self.arg = arg

    @classmethod
    def from_io(cls, io):
        arg = int.from_bytes(io.read(1), "little")
        return cls(arg)


class Unkn_31:
    opcode = 0x31

    def __init__(self, arg: int):
        self.arg = arg

    @classmethod
    def from_io(cls, io):
        arg = int.from_bytes(io.read(1), "little")
        return cls(arg)


class TextBubbleNoTail:
    opcode = 0x35

    def __init__(self, arg_bytes, text):
        self.arg_bytes = arg_bytes
        self.text = text

    @classmethod
    def from_io(cls, io):
        arg_bytes = io.read(4)
        s_len = int.from_bytes(io.read(1), "little")
        text = read_string(io, s_len)
        return cls(arg_bytes, text)


class Unkn_36:
    opcode = 0x36

    def __init__(self, arg_bytes: bytes):
        self.arg_bytes = arg_bytes

    @classmethod
    def from_io(cls, io):
        arg_bytes = io.read(10)
        return cls(arg_bytes)


class CameraPan:
    opcode = 0x37

    def __init__(self, arg_bytes: bytes):
        self.arg_bytes = arg_bytes

    @classmethod
    def from_io(cls, io):
        arg_bytes = io.read(10)
        return cls(arg_bytes)


class MoveCharacter:
    opcode = 0x39

    def __init__(self, arg_bytes: bytes):
        self.arg_bytes = arg_bytes

    @classmethod
    def from_io(cls, io):
        arg_bytes = io.read(6)
        return cls(arg_bytes)


class QuestionResponse:
    opcode = 0x3B

    def __init__(self, arg_bytes, text):
        self.arg_bytes = arg_bytes
        self.text = text

    @classmethod
    def from_io(cls, io):
        arg_bytes = io.read(2)
        s_len = int.from_bytes(io.read(1), "little")
        text = read_string(io, s_len)
        return cls(arg_bytes, text)


class ConditionalRelativeJump:
    opcode = 0x3C

    def __init__(self, target: int, type: int):
        # Target is how many bytes
        self.target = target
        self.type = type

    @classmethod
    def from_io(cls, io):
        target = int.from_bytes(io.read(2), "little")
        type = int.from_bytes(io.read(2), "little")
        if type != 0x46:
            raise ValueError(f"Unknown conditional jump type {type}")

        return cls(target, type)


class Unkn_3F:
    opcode = 0x3F

    def __init__(self, arg: int):
        self.arg = arg

    @classmethod
    def from_io(cls, io):
        arg = int.from_bytes(io.read(1), "little")
        return cls(arg)


class Unkn_40:
    opcode = 0x40

    def __init__(self, arg: int):
        self.arg = arg

    @classmethod
    def from_io(cls, io):
        arg = int.from_bytes(io.read(1), "little")
        return cls(arg)


class Unkn_42:
    opcode = 0x42

    def __init__(self, arg_bytes: bytes):
        self.arg_bytes = arg_bytes

    @classmethod
    def from_io(cls, io):
        arg_bytes = io.read(2)
        return cls(arg_bytes)


class ScreenWipe:
    opcode = 0x43

    def __init__(self, arg_bytes: bytes):
        self.arg_bytes = arg_bytes

    @classmethod
    def from_io(cls, io):
        arg_bytes = io.read(2)
        return cls(arg_bytes)


class UnconditionalJump:
    opcode = 0x44

    def __init__(self, target_index: int):
        self.target_index = target_index

    @classmethod
    def from_io(cls, io):
        target_index = int.from_bytes(io.read(4), "little")
        return cls(target_index)


class Unkn_45:
    opcode = 0x45

    def __init__(self, arg: int):
        self.arg = arg

    @classmethod
    def from_io(cls, io):
        arg = int.from_bytes(io.read(1), "little")
        return cls(arg)


class Unkn_47:
    opcode = 0x47

    def __init__(self, arg: int):
        self.arg = arg

    @classmethod
    def from_io(cls, io):
        arg = int.from_bytes(io.read(1), "little")
        return cls(arg)


class Unkn_48:
    opcode = 0x48

    def __init__(self, arg: int):
        self.arg = arg

    @classmethod
    def from_io(cls, io):
        arg = int.from_bytes(io.read(1), "little")
        return cls(arg)


class Unkn_49:
    opcode = 0x49

    def __init__(self, arg_bytes: bytes):
        self.arg_bytes = arg_bytes

    @classmethod
    def from_io(cls, io):
        arg_bytes = io.read(2)
        return cls(arg_bytes)


class Unkn_4C:
    opcode = 0x4C

    def __init__(self, arg: int):
        self.arg = arg

    @classmethod
    def from_io(cls, io):
        arg = int.from_bytes(io.read(1), "little")
        return cls(arg)


class Unkn_4D:
    opcode = 0x4D

    def __init__(self, arg: int):
        self.arg = arg

    @classmethod
    def from_io(cls, io):
        arg = int.from_bytes(io.read(1), "little")
        return cls(arg)


class Unkn_4E:
    opcode = 0x4E

    def __init__(self):
        pass

    @classmethod
    def from_io(cls, io):
        return cls()


class Unkn_4F:
    opcode = 0x4F

    def __init__(self, arg_bytes: bytes):
        self.arg_bytes = arg_bytes

    @classmethod
    def from_io(cls, io):
        arg_bytes = io.read(2)
        return cls(arg_bytes)


class Unkn_50:
    opcode = 0x50

    def __init__(self, arg_bytes: bytes):
        self.arg_bytes = arg_bytes

    @classmethod
    def from_io(cls, io):
        arg_bytes = io.read(6)
        return cls(arg_bytes)


class Unkn_51:
    opcode = 0x51

    def __init__(self):
        pass

    @classmethod
    def from_io(cls, io):
        return cls()


class TextBubble:
    opcode = 0x52

    def __init__(self, arg_bytes, text):
        self.arg_bytes = arg_bytes
        self.text = text

    @classmethod
    def from_io(cls, io):
        arg_bytes = io.read(2)
        s_len = int.from_bytes(io.read(1), "little")
        unknown = io.read(1)
        if unknown != b"\x80":
            raise ValueError(f"Unknown byte {unknown} is not 0x80 in Unkn_52")
        text = io.read(s_len).decode("shift-jis")
        return cls(arg_bytes, text)


class Unkn_53:
    opcode = 0x53

    def __init__(self, arg_bytes: bytes):
        self.arg_bytes = arg_bytes

    @classmethod
    def from_io(cls, io):
        arg_bytes = io.read(2)
        return cls(arg_bytes)


class Unkn_55:
    opcode = 0x55

    def __init__(self):
        pass

    @classmethod
    def from_io(cls, io):
        return cls()


class Unkn_57:
    opcode = 0x57

    def __init__(self, arg_bytes: bytes):
        self.arg_bytes = arg_bytes

    @classmethod
    def from_io(cls, io):
        arg_bytes = io.read(2)
        return cls(arg_bytes)


class Unkn_58:
    opcode = 0x58

    def __init__(self, arg_bytes: bytes):
        self.arg_bytes = arg_bytes

    @classmethod
    def from_io(cls, io):
        arg_bytes = io.read(2)
        return cls(arg_bytes)


class Unkn_59:
    opcode = 0x59

    def __init__(self, arg_bytes: bytes):
        self.arg_bytes = arg_bytes

    @classmethod
    def from_io(cls, io):
        arg_bytes = io.read(2)
        return cls(arg_bytes)


class EndVNSection:
    opcode = 0x5A

    def __init__(self):
        pass

    @classmethod
    def from_io(cls, io):
        return cls()


class Unkn_5D:
    opcode = 0x5D

    def __init__(self, arg_bytes: bytes):
        self.arg_bytes = arg_bytes

    @classmethod
    def from_io(cls, io):
        arg_bytes = io.read(3)
        return cls(arg_bytes)


class Unkn_5F:
    opcode = 0x5F

    def __init__(self, arg: int):
        pass

    @classmethod
    def from_io(cls, io):
        arg = int.from_bytes(io.read(1), "little")
        return cls(arg)


class Unkn_60:
    opcode = 0x60

    def __init__(self, arg_bytes: bytes):
        self.arg_bytes = arg_bytes

    @classmethod
    def from_io(cls, io):
        arg_bytes = io.read(2)
        return cls(arg_bytes)


class Unkn_62:
    opcode = 0x62

    def __init__(self, arg_bytes: bytes):
        self.arg_bytes = arg_bytes

    @classmethod
    def from_io(cls, io):
        arg_bytes = io.read(3)
        return cls(arg_bytes)


class Unkn_63:
    opcode = 0x63

    def __init__(self, arg_bytes: bytes):
        self.arg_bytes = arg_bytes

    @classmethod
    def from_io(cls, io):
        arg_bytes = io.read(3)
        return cls(arg_bytes)


class Teleport:
    opcode = 0x64

    def __init__(self, arg_bytes: bytes):
        self.arg_bytes = arg_bytes

    @classmethod
    def from_io(cls, io):
        arg_bytes = io.read(14)
        return cls(arg_bytes)


class OpenShop:
    opcode = 0x65

    def __init__(self, arg_bytes: bytes):
        self.arg_bytes = arg_bytes

    @classmethod
    def from_io(cls, io):
        arg_bytes = io.read(2)
        return cls(arg_bytes)


class EndScript:
    opcode = 0xFF

    def __init__(self):
        pass

    @classmethod
    def from_io(cls, io):
        return cls()


opcodes = {
    0x2: ScreenEffect,
    0x3: ScreenEffect2,
    0x4: Unkn_4,
    0x7: Unkn_7,
    0x9: Debug,
    0xA: CutsceneText,
    0xC: Unkn_C,
    0x5: Unkn_5,
    0x6: Unkn_6,
    0xB: Unkn_B,
    0xE: Unkn_E,
    0x10: Unkn_10,
    0x11: Unkn_11,
    0x12: Unkn_12,
    0x14: Unkn_14,
    0x15: Unkn_15,
    0x16: Unkn_16,
    0x18: Unkn_18,
    0x1C: Unkn_1C,
    0x1D: Unkn_1D,
    0x1E: Unkn_1E,
    0x20: Unkn_20,
    0x27: BubbleChoice,
    0x28: Choice,
    0x29: BubbleChoice2,
    0x2F: Unkn_2F,
    0x30: Unkn_30,
    0x31: Unkn_31,
    0x35: TextBubbleNoTail,
    0x36: Unkn_36,
    0x37: CameraPan,
    0x39: MoveCharacter,
    0x3B: QuestionResponse,
    0x3C: ConditionalRelativeJump,
    0x3F: Unkn_3F,
    0x40: Unkn_40,
    0x42: Unkn_42,
    0x43: ScreenWipe,
    0x44: UnconditionalJump,
    0x45: Unkn_45,
    0x47: Unkn_47,
    0x48: Unkn_48,
    0x49: Unkn_49,
    0x4C: Unkn_4C,
    0x4D: Unkn_4D,
    0x4E: Unkn_4E,
    0x4F: Unkn_4F,
    0x50: Unkn_50,
    0x51: Unkn_51,
    0x52: TextBubble,
    0x53: Unkn_53,
    0x55: Unkn_55,
    0x57: Unkn_57,
    0x58: Unkn_58,
    0x59: Unkn_59,
    0x5A: EndVNSection,
    0x5D: Unkn_5D,
    0x5F: Unkn_5F,
    0x60: Unkn_60,
    0x62: Unkn_62,
    0x63: Unkn_63,
    0x64: Teleport,
    0x65: OpenShop,
    0xFF: EndScript,
}


def parse_script(fp, index, pointer):
    print(f"parsing script {index} at {hex(pointer)}")
    fp.seek(0x2000 + pointer)
    while True:
        opcode = int.from_bytes(fp.read(1), "little")
        print(hex(fp.tell()))
        if opcode == 0xFF:
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
        index = int.from_bytes(f.read(0x4), "little")
        pointer = int.from_bytes(f.read(0x4), "little")
        scripts.append((index, pointer))
        if index == 0:
            break
    for index, pointer in scripts:
        parse_script(f, index, pointer)
