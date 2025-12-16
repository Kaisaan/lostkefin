
def fix_ascii(text):
    """
    Replace some ascii characters with their fullwidth equivalents
    """
    return (
        text.replace("\n", "\\n")
        .replace(", ", "，")
        .replace(",", "，")
        .replace("!", "！")
        .replace("~", "〜")
        .replace("...", "…")
    )


def generate_asm(strings_filename, rows):
    """
    Generate strings.asm
    """
    with open(strings_filename, "w", encoding="utf-8") as asm_fp:
        for row in rows:
            en = row[2]
            en = fix_ascii(en)
            if en.startswith("b\"\\x"):       # Add support to just put singular byte (python byte-string styled)
                en = "0x" + en.lstrip("b\"\\x").rstrip("\"")
            else: 
                en = "\"" + en.replace('"', '\\"') + "\""

            label = row[3]
            label = "L" + label

            asm_fp.write(f"{label}: equ\t{en}\n")
