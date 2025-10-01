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
import sys
from google.oauth2 import service_account
from googleapiclient.discovery import build

scopes = [
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/spreadsheets",
]

spreadsheet_id = "1kcEely3uIDJAifqj9kn16Bky8mBBoed03CgAwd4B0W8"


def get_sheet_titles(service):
    sheet_metadata = service.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()
    sheets = sheet_metadata.get("sheets", "")
    for sheet in sheets:
        title = sheet.get("properties", {}).get("title", "Sheet1")
        yield title


def get_rows(service, sheet):
    range_name = f"{sheet}!A:Z"
    result = (
        service.spreadsheets()
        .values()
        .get(spreadsheetId=spreadsheet_id, range=range_name)
        .execute()
    )

    return result.get("values", [])

def fix_ascii(text):
    """
    Replace some ascii characters with their fullwidth equivalents
    """



    return (
        text.replace("\n", "\\n")
        .replace(", ", "，")
        .replace(",", "，")
        .replace("! ", "！")
        .replace("!", "！")
        .replace("~", "～")
        .replace("&", "＆")
        .replace("...", "…")
    )

def makeasm(rows):

    for row in rows:
        en = row[2]
        en = fix_ascii(en)
        if en.startswith("b\"\\x"):       # Add support to just put singular byte (python byte-string styled)
            en = "0x" + en.lstrip("b\"\\x").rstrip("\"")
        else: 
            en = "\"" + en + "\""
        #return (text)
        label = row[3]
        label = "L" + label
        #print(f"{en}, {label}")

        #stringsFile.write(f".dw @{label}+Offset :: .skip 8\n")
        stringsFile.write(f"{label}: equ\t{en}\n")
        #codeFile.write(f"@{label}: .str {label}\n")

def from_sheets():
    secret_file = os.path.join("lostkefin_secret.json")
    if not os.path.exists(secret_file):
        sys.exit(
            "lostkefin_secret.json not found. Make sure it's in the lostkefin folder."
        )

    credentials = service_account.Credentials.from_service_account_file(
        secret_file, scopes=scopes
    )
    service = build("sheets", "v4", credentials=credentials)

    #if not os.path.exists(output):
        #sys.exit(f"Directory {output} does not exist")
    
    

    rows = get_rows(service, "SLPM NEW")
    #if rows[0][0] == "Offset" and rows[0][1] == "JP Text" and rows[0][2] == "EN Text":
        #version = 1
    if (
        rows[0][0] == "Offset"
        and rows[0][1] == "JP Text"
        and rows[0][2] == "EN Text"
        and rows[0][3] == "Label"
        #and rows[0][4] == "Comments"
    ):
        version = 2
    else:
        sys.exit(
            "Header is either missing Offset/JP/EN/Label column, or they're not in the right place"
        )

    #filtered_rows = [row for row in rows[1:] if row in row[0]]

    #print(f"Updating .kscript file for {stage}")
    #update_kscript(os.path.join(dir, f"{stage}.kscript"), filtered_rows, version)
    #print(rows)
    makeasm(rows)





if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: sheetsasm.py <strings.asm output> <OPTIONAL code.asm output>")
        sys.exit(1)
    
    #code = sys.argv[1]
    #codeFile = open(f"{code}", "w", encoding="utf-8")
    strings = sys.argv[1]
    stringsFile = open(f"{strings}", "w", encoding="utf-8")
    from_sheets()
