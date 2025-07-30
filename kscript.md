# .kscript file documentation

Lost Kefin's script files are stored in a binary format which makes them difficult to work with when it comes to inserting text. Because of this, we decompile them into a more human readable format, .kscript files.

## File Format

The .kscript format is a Domain Specific Language (DSL) that represents the script operations in a human-readable, tab-delimited format. Each line represents either a label, jump target, or operation.

### Structure

#### Labels
Labels mark script entry points and are formatted as:
```
LABEL_xxxxxx:
```
Where `xxxxxx` is a hexadecimal identifier (e.g., `LABEL_000001:`).

#### Jump Targets
Jump targets mark destinations for conditional jumps and are formatted as:
```
JMP_xxxxxx
```
Where `xxxxxx` is a hexadecimal identifier (e.g., `JMP_000000`).

#### Operations
Operations follow a tab-delimited format:
```
OperationName	key1:value1	key2:value2	...
```

The first column is always the operation name, followed by any number of key:value parameter pairs.

### Common Parameters

- `arg`: Hexadecimal byte data (e.g., `arg:5a00b400`)
- `text`: Text content, often in Japanese with special markup
- `target_index`: Target for jumps (e.g., `target_index:91`)
- `target`: Relative jump offset for conditional jumps
- `type`: Operation subtype identifier

### Text Encoding

Text in .kscript files supports several special features:

#### Sleep Commands
`<sleep XX>` where XX is the duration in frames:
```
text:プロローグが始まるよ！<sleep 25>
```

#### Color Markup
Text can include color codes like `#gr` (green) and `#wh` (white):
```
text:ここが北アフロカの出入り口、#grサンドリア港#whだよ。
```

#### Line Breaks
Literal `\n` characters represent line breaks:
```
text:さあ、みなさん、\n足元に気をつけて下船してください。
```

#### Text Terminator
Text often ends with `▼` character to mark completion.

## Conversion Process

The conversion between binary (.bin) and text (.kscript) formats is handled by:

1. **Decompilation** (`scripts/tasks/decompile.py`): Converts .bin → .kscript
   - Reads binary script data
   - Parses pointer tables to create labels
   - Converts opcodes to operation names
   - Handles jump target resolution

2. **Compilation** (`scripts/tasks/compile.py`): Converts .kscript → .bin
   - Parses DSL format back to binary operations
   - Encodes strings in Shift-JIS format
   - Rebuilds pointer tables and jump targets

## Example

```kscript
LABEL_000001:
  Unkn_10
  CutsceneText	arg:5a00b400	text:<K3>　　あんた、あの船に乗ってどこへいくんだい？<sleep 25><K0>
  ConditionalRelativeJump	target:0	type:70
  UnconditionalJump	target_index:91
JMP_000000
  UnconditionalJump	target_index:20900
  EndScript
```

This shows a typical script section with:
- A label marking the start
- Various operations including text display
- A conditional jump that creates a jump target
- An unconditional jump to another script section
- Script termination 