# Handle imports for both module and script execution

try:
    # When imported as a module
    from .update_kscript import fix_ascii
except ImportError:
    # When run as a script
    from update_kscript import fix_ascii

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
