# TL CSV Format

Given a [.kscript file](https://github.com/Kaisaan/lostkefin/blob/main/kscript.md), we pull out only the opcodes that contain JP text and place them into a CSV so that they can easily be worked on in Google sheets. In order to do so, each opcode gets a unique ID.

## ID Format

Each row has an ID column with the format: `<filename>||<opcode number>||<sub-opcode number>`

- **filename**: The .kscript file containing the text (e.g., `stage00.kscript`)
- **opcode number**: Index of the opcode in the original .bin file (starts at 0)
- **sub-opcode number**: Used for choice opcodes to distinguish between question text and options

## Sub-opcode Numbers

For regular text opcodes (TextBubble, VNText, etc.), the sub-opcode is always `0`.

For choice opcodes (Choice, FourChoice, etc.), the sub-opcode indicates:
- `0`: The question text itself
- `1`: First choice option
- `2`: Second choice option
- `3`: Third choice option
- etc.

## Example

```
ID                        | JP Text            | EN Text
stage00.kscript||1266||0  | 何を聞きますか？    | What do you want to ask?
stage00.kscript||1266||1  | ケフィンのこと       | About Kefin
stage00.kscript||1266||2  | スタンのこと        | About Stan
stage00.kscript||1266||3  | 錬金術のこと        | About alchemy
```

This represents a single choice opcode 1266 with one question and three response options.

## How english text is inserted into .kscript files

The `update_kscript.py` script processes CSV rows and updates .kscript files:

1. **Parse CSV rows**: Extracts the ID, JP text, and EN text from each row
2. **Build changes map**: Groups changes by opcode number, handling choice sub-opcodes specially
3. **Process .kscript file**: Reads the original .kscript file line by line, applying changes where needed
4. **Text formatting**: Replaces punctuation and formatting (commas -> full-width commas, exclamation marks, newlines)
5. **Write updated file**: Outputs the modified .kscript with English text replacing Japanese text

For choice opcodes, the script updates both the question text (sub-opcode 0) and all response options (sub-opcodes 1+) as a single operation.