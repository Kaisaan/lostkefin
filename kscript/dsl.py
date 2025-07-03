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