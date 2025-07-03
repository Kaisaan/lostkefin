import csv
import sys
from parser import line_to_op


def from_csv(csv_file, kscript_file, out_file):
    """
    Given a CSV file, modify a kscript file by replacing text from the EN colum
    """
    csv_fp = open(csv_file, "r")
    reader = csv.reader(csv_fp)
    next(reader)

    changes = {}
    for row in reader:
        id = row[0]
        jp = row[1]
        en = row[2]

        if not id:
            continue

        filename, line, subline = id.split("||")
        line = int(line)
        subline = int(subline)
        if not en:
            continue
        if subline == 0:
            changes[line] = (jp, en, {})
        else:
            changes[line][2][subline] = (jp, en)

    kscript_fp = open(kscript_file, "r")
    kscript_lines = kscript_fp.readlines()
    out_fp = open(out_file, "w")
    for i, line in enumerate(kscript_lines):
        parsed_line = line.lstrip().rstrip("\n")
        if "LABEL_" in parsed_line or "JMP_" in parsed_line:
            out_fp.write(line)
            continue
        op = line_to_op(parsed_line)
        op_type = op.__class__.__name__

        if i not in changes:
            out_fp.write(line)
            continue

        change = changes.get(i)

        jp, en, responses = change
        # sort responses by key
        if responses:
            responses = sorted(responses.items(), key=lambda x: x[0])
            responses = [x[1][1] for x in responses]

        if op_type in [
            "Choice",
            "FourChoice",
            "FourChoiceType2",
            "FourChoiceType3",
            "BubbleChoice",
            "BubbleChoice2",
        ]:
            op.question_text = (
                en.replace("\n", "\\n")
                .replace(", ", "，")
                .replace(",", "，")
                .replace("! ", "！")
                .replace("!", "！")
            )

            op.responses = responses

        elif op_type in [
            "TextBubble",
            "TextBubbleNoTail",
            "VNText",
            "CutsceneText",
        ]:
            op.text = (
                en.replace("\n", "\\n")
                .replace(", ", "，")
                .replace(",", "，")
                .replace("! ", "！")
                .replace("!", "！")
            )

        out_fp.write(f"  {str(op)}\n")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python from_csv.py <csv_file> <kscript_file> <out_file>")
        sys.exit(1)
    from_csv(sys.argv[1], sys.argv[2], sys.argv[3])
