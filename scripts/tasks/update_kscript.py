# Handle imports for both module and script execution
import sys


try:
    # When imported as a module
    from .parser import line_to_op
except ImportError:
    # When run as a script
    from parser import line_to_op


def update_kscript(kscript_file, rows):
    """
    Given a kscript file, modify a kscript file by replacing text from the EN colum
    """

    # Changes are indexed by line number in the original kscript file
    changes = {}
    for row in rows:
        if len(row) < 3:
            continue
        id = row[0]
        jp = row[1]
        en = row[2]

        if not id:
            continue

        filename, line, subline = id.split("||")
        line = int(line)
        # Choices contain multiple pieces of text per line,
        # so I also add a sub-line index as part of the ID
        subline = int(subline)
        if not en:
            en = jp

        if subline == 0:
            changes[line] = (jp, en, {})
        else:
            # Choice response
            if line not in changes:
                raise ValueError(
                    f"Found a choice response for line {line} before the choice was defined"
                )
            changes[line][2][subline] = (jp, en)

    # Read each line of the unmodified kscript file
    with open(kscript_file, "r", encoding="utf-8") as kscript_fp:
        kscript_lines = kscript_fp.readlines()

    # Then overwrite the kscript file with the modified lines
    with open(kscript_file, "w", encoding="utf-8") as out_fp:
        i = 0
        for line in kscript_lines:
            parsed_line = line.lstrip().rstrip("\n")
            if "LABEL_" in parsed_line or "JMP_" in parsed_line:
                out_fp.write(line)
                continue
            op = line_to_op(parsed_line)
            op_type = op.__class__.__name__

            if i not in changes:
                out_fp.write(line)
                i += 1
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
            i += 1
            out_fp.write(f"  {str(op)}\n")
