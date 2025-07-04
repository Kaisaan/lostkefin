import csv
import sys
import os

from .parser import line_to_op


def to_csv(kscript_file, csv_file):
    """
    Pull out just the textual operations from a kscript file and save to CSV
    """
    base_filename = os.path.basename(kscript_file)
    kscript_fp = open(kscript_file, "r", encoding="utf-8")
    csv_fp = open(csv_file, "w", newline="", encoding="utf-8")
    writer = csv.writer(csv_fp)
    writer.writerow(["ID", "JP Text", "EN Text", "Comments", "Text Type"])

    for i, line in enumerate(kscript_fp.readlines()):
        line = line.lstrip().rstrip("\n")
        if "LABEL_" in line or "JMP_" in line:
            continue

        op = line_to_op(line)
        op_type = op.__class__.__name__

        if op_type in [
            "Choice",
            "FourChoice",
            "FourChoiceType2",
            "FourChoiceType3",
            "BubbleChoice",
            "BubbleChoice2",
        ]:
            text = op.to_object()["question_text"]
            text = text.replace("\\n", "\n")
            writer.writerow([f"{base_filename}||{i}||{0}", text, "", "", op_type])
            responses = op.to_object()["responses"]
            for j, response in enumerate(responses):
                writer.writerow(
                    [f"{base_filename}||{i}||{j + 1}", response, "", "", op_type]
                )

        elif op_type in [
            "TextBubble",
            "TextBubbleNoTail",
            "VNText",
            "CutsceneText",
        ]:
            text = op.to_object()["text"]
            text = text.replace("\\n", "\n")
            writer.writerow([f"{base_filename}||{i}||{0}", text, "", "", op_type])


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python to_csv.py <kscript_file> <csv_file>")
        sys.exit(1)
    to_csv(sys.argv[1], sys.argv[2])
