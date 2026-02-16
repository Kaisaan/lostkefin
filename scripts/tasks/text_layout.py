"""Text layout utilities for centering and line-breaking game text."""

import csv
import re
from pathlib import Path

SCREEN_WIDTH = 640


def load_widths(csv_path=None):
    """Load character widths from kerning CSV."""
    if csv_path is None:
        csv_path = Path(__file__).parent.parent / "misc" / "kerning.csv"
    widths = {}
    with open(csv_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            widths[row['char']] = int(row['width'])
    widths[' '] = 4
    return widths


def calculate_width(text, widths):
    """Calculate pixel width of a string.

    Each character gets its base width plus 2px spacing,
    except brackets [] which are microspacing chars (no extra spacing).
    Unknown characters are skipped.
    """
    total = 0
    for char in text:
        if char in widths:
            if char in "[]":
                total += widths[char]
            else:
                total += widths[char] + 2
    return total


def strip_formatting(text):
    """Strip formatting tags that have zero visual width.

    Removes color tags (#wh, #gr, etc.), sleep commands, special markers,
    and font tags. Used for width calculation only — the original text
    with tags intact is preserved in output.
    """
    text = re.sub(r'#(wh|gr|bl|pi|yl|re|bk|gl|cy)', '', text)
    text = re.sub(r'<sleep \d+>', '', text)
    text = text.replace("\u25bc", "")
    text = text.replace("<F>", "")
    text = text.replace("</F>", "")
    return text


def center_pad(text, widths, left_offset):
    """Generate spacing prefix to center text on screen.

    Builds padding from spaces (6px), ] (2px), and [ (1px) to reach
    the exact pixel offset needed for centering.
    """
    text_width = calculate_width(strip_formatting(text), widths)
    target_padding = (SCREEN_WIDTH - 2 * left_offset - text_width) / 2

    if target_padding <= 0:
        return ""

    padding = ''
    remaining = target_padding

    while remaining >= 6:
        padding += ' '
        remaining -= 6
    while remaining >= 2:
        padding += ']'
        remaining -= 2
    while remaining >= 1:
        padding += '['
        remaining -= 1

    return padding


def center_lines(text, widths, left_offset):
    r"""Center each line of text by prepending spacing.

    Text uses \\n as line separator (escaped newlines for kscript format).
    """
    lines = text.split("\\n")
    centered = []
    for line in lines:
        pad = center_pad(line, widths, left_offset)
        centered.append(pad + line)
    return "\\n".join(centered)


def _get_words_with_widths(text, widths):
    """Split text into words and calculate their pixel widths.

    Angle-bracket tags like <sleep 30> are treated as zero-width tokens
    that won't be broken across lines. Color tags within words are
    stripped for width calculation but preserved in output.
    """
    words = re.findall(r'<[^>]+>|[^<\s]+', text)
    result = []
    for word in words:
        if word.startswith('<') and word.endswith('>'):
            result.append((word, 0))
        else:
            stripped = strip_formatting(word)
            result.append((word, calculate_width(stripped, widths)))
    return result


def _greedy_break(words, max_width, max_lines, space_width=6):
    """Break words into lines using a greedy algorithm.

    Places as many words on each line as possible before moving to the next.
    """
    if not words:
        return []

    lines = []
    current_line = []
    current_width = 0

    for word, width in words:
        if not current_line:
            current_line.append(word)
            current_width = width
        else:
            new_width = current_width + space_width + width
            if new_width <= max_width:
                current_line.append(word)
                current_width = new_width
            else:
                lines.append(current_line)
                if len(lines) >= max_lines:
                    return lines
                current_line = [word]
                current_width = width

    if current_line:
        lines.append(current_line)

    return lines[:max_lines]


def break_lines(text, widths, max_width, max_lines=10):
    r"""Break text into lines using greedy algorithm.

    Strips existing \\n line breaks and re-wraps from scratch.
    Returns text with \\n as line separator.
    """
    text = text.replace("\\n", " ")
    text = ' '.join(text.split())
    if not text:
        return text

    words = _get_words_with_widths(text, widths)
    lines = _greedy_break(words, max_width, max_lines)

    return "\\n".join(' '.join(line) for line in lines)
