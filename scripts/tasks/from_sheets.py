# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "google-api-python-client",
#     "google-auth",
# ]
# ///

"""
Pull latest translations from Google Sheets and updates kscript files.
"""

import os
import shutil
import sys
from google.oauth2 import service_account
from googleapiclient.discovery import build
from io import StringIO
from .parser import line_to_op

scopes = [
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/spreadsheets",
]
secret_file = os.path.join("lostkefin_secret.json")
if not os.path.exists(secret_file):
    sys.exit("lostkefin_secret.json not found. Make sure it's in the lostkefin folder.")

spreadsheet_id = "1kcEely3uIDJAifqj9kn16Bky8mBBoed03CgAwd4B0W8"

credentials = service_account.Credentials.from_service_account_file(
    secret_file, scopes=scopes
)
service = build("sheets", "v4", credentials=credentials)


def get_sheet_titles():
    sheet_metadata = service.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()
    sheets = sheet_metadata.get("sheets", "")
    for sheet in sheets:
        title = sheet.get("properties", {}).get("title", "Sheet1")
        yield title


def get_rows(sheet):
    range_name = f"{sheet}!A:Z"
    result = (
        service.spreadsheets()
        .values()
        .get(spreadsheetId=spreadsheet_id, range=range_name)
        .execute()
    )

    return result.get("values", [])


def update_kscript(kscript_file, rows):
    """
    Given a kscript file, modify a kscript file by replacing text from the EN colum
    """

    out = StringIO()

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
        subline = int(subline)
        if not en:
            continue
        if subline == 0:
            changes[line] = (jp, en, {})
        else:
            changes[line][2][subline] = (jp, en)

    # Read
    with open(kscript_file, "r", encoding="utf-8") as kscript_fp:
        kscript_lines = kscript_fp.readlines()

    # Then overwrite
    with open(kscript_file, "w", encoding="utf-8") as out_fp:
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


def from_sheets(dir: str = "decompiled"):
    if not os.path.exists(dir):
        sys.exit(f"Directory {dir} does not exist")

    for title in get_sheet_titles():
        if title not in [
            "stage00",
            "stage10",
            "stage20",
            "stage30",
            "stage40",
            "stage50",
            "stage60",
            "stage70",
            "stage80",
            "stage90",
            "stagea0",
            "stageb0",
        ]:
            continue
        print(f"Pulling sheet for {title}")
        rows = get_rows(title)
        if rows[0][0] != "ID" or rows[0][1] != "JP Text" or rows[0][2] != "EN Text":
            sys.exit(
                "Header is either missing ID/JP/EN column, or they're not in the right place"
            )

        print(f"Updating .kscript file for {title}")
        update_kscript(os.path.join(dir, f"{title}.kscript"), rows[1:])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: from_sheets.py <directory of .kscript files>")
        sys.exit(1)
    from_sheets(sys.argv[1])
