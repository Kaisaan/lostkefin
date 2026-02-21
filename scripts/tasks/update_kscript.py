# Handle imports for both module and script execution

try:
    # When imported as a module
    from .parser import line_to_op
    from .text_layout import load_widths, center_lines, break_lines, SCREEN_WIDTH
except ImportError:
    # When run as a script
    from parser import line_to_op
    from text_layout import load_widths, center_lines, break_lines, SCREEN_WIDTH

from os.path import basename

center_ids = {
    "stage00.kscript": [
        24,
        27,
        29,
        31,
        33,
        35,
        37,
        39,
        42,
        44,
        1441,
        1445,
        1449,
        1450,
        1454,
        1455,
        1459,
        1460,
        1464,
        1468,
        1469,
        1473,
        1477,
        1478,
        1482,
        1483,
        1484,
        1485,
        1489,
        1550,
        1554,
        1558,
        1559,
        1563,
        1564,
        1568,
        1569,
        1573,
        1577,
        1578,
        1582,
        1586,
        1587,
        1591,
        1592,
        1593,
        1594,
        1598,
        2357,
        4149,
    ],
    "stage10.kscript": [1501],
    "stage20.kscript": [869, 1574],
    "stage30.kscript": [279, 619],
    "stage40.kscript": [41, 1854],
    "stage50.kscript": [1316, 1902],
    "stage60.kscript": [
        275,
        285,
        298,
        305,
        307,
        343,
        345,
        468,
        1194,
        1330,
        1332,
        1334,
        1367,
        1369,
        1371,
        1373,
        1956,
        2203,
    ],
    "stage70.kscript": [1404],
    "stage80.kscript": [
        314,
        414,
        416,
        418,
        969,
        972,
        1166,
        1168,
        1195,
        1197,
        1199,
        1201,
        1214,
        1240,
        1242,
        1252,
        1254,
        1260,
        1275,
        1277,
        1287,
        1799,
        1801,
        1803,
        1805,
        1807,
        1809,
        3169,
    ],
    "stage90.kscript": [
        8,
        16,
        18,
        20,
        82,
        361,
        362,
        363,
        364,
        365,
        366,
        995,
        996,
        997,
        998,
        999,
        1000,
        1411,
        1412,
        1413,
        1414,
        1415,
        1416,
        1417,
        1418,
        1419,
    ],
}


def fix_ascii(text, fullwidth_ellipsis=False):
    """
    Replace some ascii characters with their fullwidth equivalents
    """
    fixed = (
        text.replace("\n", "\\n")
        .replace("，", ",")
        .replace("！", "!")
        .replace("〜", "~")
        .replace("＆", "&")
        .replace("炎", "：")
        .replace("☆", "；")
        .replace("★", "？")
        .replace("→", "！")
        .replace("＋", "+")
    )

    if fullwidth_ellipsis:
        fixed = fixed.replace("...", "…")
    else:
        fixed = fixed.replace("…", "...")

    return fixed


def update_kscript(kscript_file, rows, version=2):
    """
    Modify a kscript file in-place by replacing text from the EN colum
    """
    filename = basename(kscript_file)
    widths = load_widths()

    # Changes are indexed by line number in the original kscript file
    changes = {}
    for row in rows:
        if len(row) < 3:
            continue
        id = row[0]
        # New columns added for v2
        if version == 2:
            jp = row[3]
            en = row[4]
        else:
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
                responses = [fix_ascii(x[1][1]) for x in responses]

            if op_type in [
                "Choice",
                "FourChoice",
                "FourChoiceType2",
                "FourChoiceType3",
                "BubbleChoice",
                "BubbleChoice2",
            ]:
                op.question_text = fix_ascii(en)

                op.responses = responses

            elif op_type in [
                "TextBubble",
                "TextBubbleNoTail",
                "VNText",
            ]:
                op.text = fix_ascii(en)

            elif op_type == "CutsceneText":
                padding = int.from_bytes(op.arg[0:2], "little")
                text = fix_ascii(en)
                if i in center_ids.get(filename, []):
                    text = center_lines(text, widths, padding)
                else:
                    max_width = SCREEN_WIDTH - 2 * padding
                    text = break_lines(text, widths, max_width)

                op.text = text

            i += 1
            out_fp.write(f"  {str(op)}\n")
