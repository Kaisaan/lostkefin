"""
parser.py

Interprets Lost Kefin's .bin script files and converts them to DSL format,
and vice versa.
"""

import re
import sys
import json


def format_value(value):
    """
    Format a value for DSL output, adding quotes if it contains spaces or special chars
    """
    if isinstance(value, str):
        if "\t" in value:
            raise ValueError(f"Tab in value: {value}")
        return value
    if isinstance(value, list):
        return json.dumps(value, ensure_ascii=False)
    return str(value)


def instruction_to_dsl(instruction):
    """
    Convert a single instruction dict to DSL format
    """
    if not isinstance(instruction, dict) or "name" not in instruction:
        raise ValueError("Instruction must be a dict with a 'name' key")

    parts = [instruction["name"]]

    # Add all other keys as key:value pairs
    for key, value in instruction.items():
        if key != "name":  # Skip the name since it's already added
            formatted_value = format_value(value)
            parts.append(f"{key}:{formatted_value}")

    return "\t".join(parts)


def line_to_op(line: str):
    """
    Given a single line of a .kscript file, return the corresponding Operation
    Line is tab-delimited and looks like
    opcode	arg:value	arg2:value
    """
    line = line.strip()
    # parse until first space
    split = line.split("\t")
    operation = split[0]
    op = globals()[operation]

    kwargs = {}
    for term in split[1:]:
        if ":" not in term:
            print("Error")
            sys.exit(line)
        key, value = term.split(":", 1)
        if key == "arg":
            value = bytes.fromhex(value)
        else:
            try:
                value = int(value)
            except ValueError:
                if value.startswith("["):
                    value = json.loads(value)
        kwargs[key] = value

    try:
        return op(**kwargs)
    except TypeError:
        if "arg" not in kwargs:
            kwargs["arg"] = b""
        return op(**kwargs)


def read_debug_string(io):
    """
    Decode a debug string from the script
    Just normal null terminated strings
    """
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
    return debug_str


def read_string(io, length):
    """
    Decode a string from the script
    1. Replace sleep control codes with <sleep XX>
    2. Decode the string from shift-jis
    3. Escape newlines
    """
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

    decoded = out.decode("shift-jis")
    decoded = decoded.replace("\n", "\\n")
    return decoded


def encode_string(s):
    """
    1. Unescape newlines
    2. Re-encode to shift-jis
    3. Insert sleep control codes
    4. Add length to the front and flip the top bit
    """
    s = s.replace("\\n", "\n")

    encoded = s.encode("shift-jis")

    # Replace <sleep XX> with \xFF\xFD\xXX where XX is an int
    while b"<sleep " in encoded:
        encoded = re.sub(
            rb"<sleep (\d+)>",
            lambda m: b"\xff\xfd" + int(m.group(1)).to_bytes(1, "little"),
            encoded,
        )

    length = len(encoded)
    # Flip top bit
    length = length | 0x8000
    encoded = length.to_bytes(2, "little") + encoded
    return encoded


def choice_from_io(io, choices=2):
    """
    Aside from their args, all choice operations can be decoded the same way
    """
    s_len = int.from_bytes(io.read(1), "little")

    question_text = read_string(io, s_len)

    responses = []
    indices = []
    for _ in range(choices):
        s_len = int.from_bytes(io.read(1), "little")

        response = read_string(io, s_len)

        index = int.from_bytes(io.read(4), "little")
        responses.append(response)
        indices.append(index)
        if index == 0:
            break

    return question_text, responses, indices


def choice_to_bytes(choice):
    """
    All choice operations encode the same way
    """
    out = (
        choice.opcode.to_bytes(1, "little")
        + choice.arg
        + encode_string(choice.question_text)
    )

    for response, index in zip(choice.responses, choice.indices):
        out += encode_string(response)
        out += index.to_bytes(4, "little")

    out += b"\xff"
    return out


class Operation:
    """
    Generic operation. For most opcodes where we just want to read their argument data
    and keep track of it, this is enough.
    """

    opcode: int
    size: int

    def __init__(self, arg: bytes):
        self.arg = arg

    def to_object(self):
        object = {"name": self.__class__.__name__, "arg": self.arg.hex()}
        if len(self.arg) == 0:
            del object["arg"]
        return object

    def to_bytes(self):
        return self.opcode.to_bytes(1, "little") + self.arg

    def __str__(self):
        object = self.to_object()
        return instruction_to_dsl(object)

    @classmethod
    def from_io(cls, io):
        arg = io.read(cls.size)
        return cls(arg)


class ScreenEffect(Operation):
    opcode = 0x2

    def __init__(self, effect_type: int):
        self.effect_type = effect_type

    def to_object(self):
        object = {"name": self.__class__.__name__, "effect_type": self.effect_type}
        return object

    def to_bytes(self):
        return self.opcode.to_bytes(1, "little") + self.effect_type.to_bytes(
            1, "little"
        )

    @classmethod
    def from_io(cls, io):
        effect_type = int.from_bytes(io.read(1), "little")
        return cls(effect_type)


class ScreenEffect2(Operation):
    opcode = 0x3

    def __init__(self, effect_type: int):
        self.effect_type = effect_type

    def to_object(self):
        object = {"name": self.__class__.__name__, "effect_type": self.effect_type}
        return object

    def to_bytes(self):
        return self.opcode.to_bytes(1, "little") + self.effect_type.to_bytes(
            1, "little"
        )

    @classmethod
    def from_io(cls, io):
        effect_type = int.from_bytes(io.read(1), "little")
        return cls(effect_type)


class Unkn_4(Operation):
    opcode = 0x4
    size = 0


class CutsceneText(Operation):
    opcode = 0xA

    def __init__(self, arg, text):
        self.arg = arg
        self.text = text

    def to_object(self):
        object = {
            "name": self.__class__.__name__,
            "arg": self.arg.hex(),
            "text": self.text,
        }
        return object

    def to_bytes(self):
        return self.opcode.to_bytes(1, "little") + self.arg + encode_string(self.text)

    @classmethod
    def from_io(cls, io):
        arg = io.read(4)
        s_len = int.from_bytes(io.read(1), "little")

        text = read_string(io, s_len)
        return cls(arg, text)


class Unkn_5(Operation):
    opcode = 0x5
    size = 0


class Unkn_6(Operation):
    opcode = 0x6
    size = 0


class Unkn_7(Operation):
    opcode = 0x7
    size = 1


class Debug(Operation):
    opcode = 0x8

    def __init__(self, debug_str: str):
        self.debug_str = debug_str

    def to_object(self):
        object = {"name": self.__class__.__name__, "debug_str": self.debug_str}
        return object

    def to_bytes(self):
        return (
            self.opcode.to_bytes(1, "little") + self.debug_str.encode("ascii") + b"\x00"
        )

    @classmethod
    def from_io(cls, io):
        debug_str = read_debug_string(io)
        return cls(debug_str)


class Debug2(Operation):
    opcode = 0x9

    def __init__(self, debug_str: str):
        self.debug_str = debug_str

    def to_object(self):
        object = {"name": self.__class__.__name__, "debug_str": self.debug_str}
        return object

    def to_bytes(self):
        return (
            self.opcode.to_bytes(1, "little") + self.debug_str.encode("ascii") + b"\x00"
        )

    @classmethod
    def from_io(cls, io):
        debug_str = read_debug_string(io)
        return cls(debug_str)


class Unkn_B(Operation):
    opcode = 0xB
    size = 0


class Unkn_C(Operation):
    opcode = 0xC
    size = 0


class Unkn_E(Operation):
    opcode = 0xE
    size = 1


class Unkn_10(Operation):
    opcode = 0x10
    size = 0


class Unkn_11(Operation):
    opcode = 0x11
    size = 0


class Unkn_12(Operation):
    opcode = 0x12
    size = 0


class Unkn_13(Operation):
    opcode = 0x13
    size = 3


class Unkn_14(Operation):
    opcode = 0x14
    size = 1


class Unkn_15(Operation):
    opcode = 0x15
    size = 2


class Unkn_16(Operation):
    opcode = 0x16
    size = 3


class Debug3(Operation):
    opcode = 0x17

    def __init__(self, debug_str: str, arg: int):
        self.debug_str = debug_str
        self.arg = arg

    def to_object(self):
        object = {
            "name": self.__class__.__name__,
            "debug_str": self.debug_str,
            "arg": self.arg.hex(),
        }
        return object

    def to_bytes(self):
        return (
            self.opcode.to_bytes(1, "little")
            + self.debug_str.encode("ascii")
            + b"\x00"
            + self.arg
        )

    @classmethod
    def from_io(cls, io):
        debug_str = read_debug_string(io)
        arg = io.read(2)
        return cls(debug_str, arg)


class Unkn_18(Operation):
    opcode = 0x18
    size = 3


class Unkn_19(Operation):
    opcode = 0x19
    size = 8


class Unkn_1A(Operation):
    opcode = 0x1A
    size = 3


class Unkn_1B(Operation):
    opcode = 0x1B
    size = 6


class Unkn_1C(Operation):
    opcode = 0x1C
    size = 4


class Unkn_1D(Operation):
    opcode = 0x1D
    size = 3


class Unkn_1E(Operation):
    opcode = 0x1E
    size = 9


class Unkn_1F(Operation):
    opcode = 0x1F
    size = 4


class Unkn_20(Operation):
    opcode = 0x20
    size = 3


class Unkn_21(Operation):
    opcode = 0x21
    size = 3


class Unkn_22(Operation):
    opcode = 0x22
    size = 4


class Unkn_23(Operation):
    opcode = 0x23
    size = 5


class FourChoice(Operation):
    opcode = 0x24

    def __init__(self, arg, question_text, responses: list, indices: list):
        self.arg = arg
        self.question_text = question_text
        self.responses = responses
        self.indices = indices

    def to_object(self):
        object = {
            "name": self.__class__.__name__,
            "arg": self.arg.hex(),
            "question_text": self.question_text,
            "responses": self.responses,
            "indices": self.indices,
        }
        return object

    def to_bytes(self):
        return choice_to_bytes(self)

    @classmethod
    def from_io(cls, io):
        arg = io.read(4)
        question_text, responses, indices = choice_from_io(io, choices=4)

        return cls(arg, question_text, responses, indices)


class FourChoiceType2(Operation):
    opcode = 0x25

    def __init__(self, arg, question_text, responses: list, indices: list):
        self.arg = arg
        self.question_text = question_text
        self.responses = responses
        self.indices = indices

    def to_object(self):
        object = {
            "name": self.__class__.__name__,
            "arg": self.arg.hex(),
            "question_text": self.question_text,
            "responses": self.responses,
            "indices": self.indices,
        }
        return object

    def to_bytes(self):
        return choice_to_bytes(self)

    @classmethod
    def from_io(cls, io):
        arg = io.read(2)
        question_text, responses, indices = choice_from_io(io, choices=4)

        return cls(arg, question_text, responses, indices)


class FourChoiceType3(Operation):
    opcode = 0x26

    def __init__(self, arg, question_text, responses: list, indices: list):
        self.arg = arg
        self.question_text = question_text
        self.responses = responses
        self.indices = indices

    def to_object(self):
        object = {
            "name": self.__class__.__name__,
            "arg": self.arg.hex(),
            "question_text": self.question_text,
            "responses": self.responses,
            "indices": self.indices,
        }
        return object

    def to_bytes(self):
        return choice_to_bytes(self)

    @classmethod
    def from_io(cls, io):
        arg = io.read(2)
        question_text, responses, indices = choice_from_io(io, choices=4)

        return cls(arg, question_text, responses, indices)


class BubbleChoice(Operation):
    opcode = 0x27

    def __init__(self, arg, question_text, responses: list, indices: list):
        self.arg = arg
        self.question_text = question_text
        self.responses = responses
        self.indices = indices

    def to_object(self):
        object = {
            "name": self.__class__.__name__,
            "arg": self.arg.hex(),
            "question_text": self.question_text,
            "responses": self.responses,
            "indices": self.indices,
        }
        return object

    def to_bytes(self):
        return choice_to_bytes(self)

    @classmethod
    def from_io(cls, io):
        arg = io.read(4)
        question_text, responses, indices = choice_from_io(io)

        return cls(arg, question_text, responses, indices)


class Choice(Operation):
    opcode = 0x28

    def __init__(self, arg, question_text, responses: list, indices: list):
        self.arg = arg
        self.question_text = question_text
        self.responses = responses
        self.indices = indices

    def to_object(self):
        object = {
            "name": self.__class__.__name__,
            "arg": self.arg.hex(),
            "question_text": self.question_text,
            "responses": self.responses,
            "indices": self.indices,
        }
        return object

    def to_bytes(self):
        return choice_to_bytes(self)

    @classmethod
    def from_io(cls, io):
        arg = io.read(2)
        question_text, responses, indices = choice_from_io(io)

        return cls(arg, question_text, responses, indices)


class BubbleChoice2(Operation):
    opcode = 0x29

    def __init__(self, arg, question_text, responses: list, indices: list):
        self.arg = arg
        self.question_text = question_text
        self.responses = responses
        self.indices = indices

    def to_object(self):
        object = {
            "name": self.__class__.__name__,
            "arg": self.arg.hex(),
            "question_text": self.question_text,
            "responses": self.responses,
            "indices": self.indices,
        }
        return object

    def to_bytes(self):
        return choice_to_bytes(self)

    @classmethod
    def from_io(cls, io):
        arg = io.read(2)
        question_text, responses, indices = choice_from_io(io)

        return cls(arg, question_text, responses, indices)


class RotateCamera(Operation):
    opcode = 0x2A
    size = 3


class Unkn_2B(Operation):
    opcode = 0x2B
    size = 1


class Unkn_2C(Operation):
    opcode = 0x2C
    size = 1


class Unkn_2D(Operation):
    opcode = 0x2D
    size = 9


class Debug4(Operation):
    opcode = 0x2E

    def __init__(self, debug_str: str):
        self.debug_str = debug_str

    def to_object(self):
        object = {"name": self.__class__.__name__, "debug_str": self.debug_str}
        return object

    def to_bytes(self):
        return (
            self.opcode.to_bytes(1, "little") + self.debug_str.encode("ascii") + b"\x00"
        )

    @classmethod
    def from_io(cls, io):
        debug_str = read_debug_string(io)
        return cls(debug_str)


class Unkn_2F(Operation):
    opcode = 0x2F
    size = 2


class Unkn_30(Operation):
    opcode = 0x30
    size = 1


class Unkn_31(Operation):
    opcode = 0x31
    size = 1


class PlayEndingCutscene(Operation):
    opcode = 0x33
    size = 1


class Unkn_34(Operation):
    opcode = 0x34
    size = 0


class TextBubbleNoTail(Operation):
    opcode = 0x35

    def __init__(self, arg, text):
        self.arg = arg
        self.text = text

    def to_object(self):
        object = {
            "name": self.__class__.__name__,
            "arg": self.arg.hex(),
            "text": self.text,
        }
        return object

    def to_bytes(self):
        return self.opcode.to_bytes(1, "little") + self.arg + encode_string(self.text)

    @classmethod
    def from_io(cls, io):
        arg = io.read(4)
        s_len = int.from_bytes(io.read(1), "little")
        text = read_string(io, s_len)
        return cls(arg, text)


class Unkn_36(Operation):
    opcode = 0x36
    size = 10


class CameraPan(Operation):
    opcode = 0x37
    size = 10


class Unkn_38(Operation):
    opcode = 0x38
    size = 6


class MoveCharacter(Operation):
    opcode = 0x39
    size = 6


class VNText(Operation):
    opcode = 0x3B

    def __init__(self, arg, text):
        self.arg = arg
        self.text = text

    def to_object(self):
        object = {
            "name": self.__class__.__name__,
            "arg": self.arg.hex(),
            "text": self.text,
        }
        return object

    def to_bytes(self):
        return self.opcode.to_bytes(1, "little") + self.arg + encode_string(self.text)

    @classmethod
    def from_io(cls, io):
        arg = io.read(2)
        s_len = int.from_bytes(io.read(1), "little")
        text = read_string(io, s_len)
        return cls(arg, text)


class ConditionalRelativeJump(Operation):
    opcode = 0x3C

    def __init__(self, target: int, type: int):
        # Target is how many bytes forward to jump
        self.target = target
        self.type = type

    def to_object(self):
        object = {
            "name": self.__class__.__name__,
            "target": self.target,
            "type": self.type,
        }
        return object

    def to_bytes(self):
        return (
            self.opcode.to_bytes(1, "little")
            + self.target.to_bytes(2, "little")
            + self.type.to_bytes(2, "little")
        )

    @classmethod
    def from_io(cls, io):
        target = int.from_bytes(io.read(2), "little")
        type = int.from_bytes(io.read(2), "little")
        if type != 0x46:
            raise ValueError(f"Unknown conditional jump type {type}")

        return cls(target, type)


class Unkn_3E(Operation):
    opcode = 0x3E
    size = 1


class Unkn_3F(Operation):
    opcode = 0x3F
    size = 1


class Unkn_40(Operation):
    opcode = 0x40
    size = 1


class Unkn_41(Operation):
    opcode = 0x41
    size = 1


class Unkn_42(Operation):
    opcode = 0x42
    size = 2


class ScreenWipe(Operation):
    opcode = 0x43
    size = 2


class UnconditionalJump(Operation):
    opcode = 0x44

    def __init__(self, target_index: int):
        self.target_index = target_index

    def to_object(self):
        object = {"name": self.__class__.__name__, "target_index": self.target_index}
        return object

    def to_bytes(self):
        return self.opcode.to_bytes(1, "little") + self.target_index.to_bytes(
            4, "little"
        )

    @classmethod
    def from_io(cls, io):
        target_index = int.from_bytes(io.read(4), "little")
        return cls(target_index)


class Unkn_45(Operation):
    opcode = 0x45
    size = 1


class Unkn_47(Operation):
    opcode = 0x47
    size = 1


class Unkn_48(Operation):
    opcode = 0x48
    size = 1


class Unkn_49(Operation):
    opcode = 0x49
    size = 2


class Unkn_4A(Operation):
    opcode = 0x4A
    size = 3


class Unkn_4B(Operation):
    opcode = 0x4B
    size = 3


class Unkn_4C(Operation):
    opcode = 0x4C
    size = 1


class Unkn_4D(Operation):
    opcode = 0x4D
    size = 1


class Unkn_4E(Operation):
    opcode = 0x4E
    size = 0


class Unkn_4F(Operation):
    opcode = 0x4F
    size = 2


class ShowCharacters(Operation):
    opcode = 0x50
    size = 6


class StartVNSection(Operation):
    opcode = 0x51
    size = 0


class TextBubble(Operation):
    opcode = 0x52

    def __init__(self, arg, text):
        self.arg = arg
        self.text = text

    def to_object(self):
        object = {
            "name": self.__class__.__name__,
            "arg": self.arg.hex(),
            "text": self.text,
        }
        return object

    def to_bytes(self):
        return self.opcode.to_bytes(1, "little") + self.arg + encode_string(self.text)

    @classmethod
    def from_io(cls, io):
        arg = io.read(2)
        s_len = int.from_bytes(io.read(1), "little")
        text = read_string(io, s_len)
        return cls(arg, text)


class Unkn_53(Operation):
    opcode = 0x53
    size = 2


class Debug5(Operation):
    opcode = 0x54

    def __init__(self, debug_str: str):
        self.debug_str = debug_str

    def to_object(self):
        object = {"name": self.__class__.__name__, "debug_str": self.debug_str}
        return object

    def to_bytes(self):
        return (
            self.opcode.to_bytes(1, "little") + self.debug_str.encode("ascii") + b"\x00"
        )

    @classmethod
    def from_io(cls, io):
        debug_str = read_debug_string(io)
        return cls(debug_str)


class Unkn_55(Operation):
    opcode = 0x55
    size = 0


class Unkn_56(Operation):
    opcode = 0x56
    size = 1


class Unkn_57(Operation):
    opcode = 0x57
    size = 2


class Unkn_58(Operation):
    opcode = 0x58
    size = 2


class Unkn_59(Operation):
    opcode = 0x59
    size = 2


class EndVNSection(Operation):
    opcode = 0x5A
    size = 0


class Unkn_5B(Operation):
    opcode = 0x5B
    size = 3


class Unkn_5C(Operation):
    opcode = 0x5C
    size = 3


class Unkn_5D(Operation):
    opcode = 0x5D
    size = 3


class Unkn_5E(Operation):
    opcode = 0x5E
    size = 1


class Unkn_5F(Operation):
    opcode = 0x5F
    size = 1


class Unkn_60(Operation):
    opcode = 0x60
    size = 2


class Unkn_62(Operation):
    opcode = 0x62
    size = 3


class Unkn_63(Operation):
    opcode = 0x63
    size = 3


class Teleport(Operation):
    opcode = 0x64
    size = 13


class OpenShop(Operation):
    opcode = 0x65
    size = 2


class Unkn_66(Operation):
    opcode = 0x66
    size = 9


class Unkn_67(Operation):
    opcode = 0x67
    size = 0


class EndScript(Operation):
    opcode = 0xFF
    size = 0


opcodes = {
    0x2: ScreenEffect,
    0x3: ScreenEffect2,
    0x4: Unkn_4,
    0x7: Unkn_7,
    0x8: Debug,
    0x9: Debug2,
    0xA: CutsceneText,
    0xC: Unkn_C,
    0x5: Unkn_5,
    0x6: Unkn_6,
    0xB: Unkn_B,
    0xE: Unkn_E,
    0x10: Unkn_10,
    0x11: Unkn_11,
    0x12: Unkn_12,
    0x13: Unkn_13,
    0x14: Unkn_14,
    0x15: Unkn_15,
    0x16: Unkn_16,
    0x17: Debug3,
    0x18: Unkn_18,
    0x19: Unkn_19,
    0x1A: Unkn_1A,
    0x1B: Unkn_1B,
    0x1C: Unkn_1C,
    0x1D: Unkn_1D,
    0x1E: Unkn_1E,
    0x1F: Unkn_1F,
    0x20: Unkn_20,
    0x21: Unkn_21,
    0x22: Unkn_22,
    0x23: Unkn_23,
    0x24: FourChoice,
    0x25: FourChoiceType2,
    0x26: FourChoiceType3,
    0x27: BubbleChoice,
    0x28: Choice,
    0x29: BubbleChoice2,
    0x2A: RotateCamera,
    0x2B: Unkn_2B,
    0x2C: Unkn_2C,
    0x2D: Unkn_2D,
    0x2E: Debug4,
    0x2F: Unkn_2F,
    0x30: Unkn_30,
    0x31: Unkn_31,
    0x33: PlayEndingCutscene,
    0x34: Unkn_34,
    0x35: TextBubbleNoTail,
    0x36: Unkn_36,
    0x37: CameraPan,
    0x38: Unkn_38,
    0x39: MoveCharacter,
    0x3B: VNText,
    0x3C: ConditionalRelativeJump,
    0x3E: Unkn_3E,
    0x3F: Unkn_3F,
    0x40: Unkn_40,
    0x41: Unkn_41,
    0x42: Unkn_42,
    0x43: ScreenWipe,
    0x44: UnconditionalJump,
    0x45: Unkn_45,
    0x47: Unkn_47,
    0x48: Unkn_48,
    0x49: Unkn_49,
    0x4A: Unkn_4A,
    0x4B: Unkn_4B,
    0x4C: Unkn_4C,
    0x4D: Unkn_4D,
    0x4E: Unkn_4E,
    0x4F: Unkn_4F,
    0x50: ShowCharacters,
    0x51: StartVNSection,
    0x52: TextBubble,
    0x53: Unkn_53,
    0x54: Debug5,
    0x55: Unkn_55,
    0x56: Unkn_56,
    0x57: Unkn_57,
    0x58: Unkn_58,
    0x59: Unkn_59,
    0x5B: Unkn_5B,
    0x5A: EndVNSection,
    0x5C: Unkn_5C,
    0x5D: Unkn_5D,
    0x5E: Unkn_5E,
    0x5F: Unkn_5F,
    0x60: Unkn_60,
    0x62: Unkn_62,
    0x63: Unkn_63,
    0x64: Teleport,
    0x65: OpenShop,
    0x66: Unkn_66,
    0x67: Unkn_67,
    0xFF: EndScript,
}
