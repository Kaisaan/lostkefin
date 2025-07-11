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

# Handle imports for both module and script execution
try:
    # When imported as a module
    from .update_kscript import update_kscript
except ImportError:
    # When run as a script
    from update_kscript import update_kscript


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


def from_sheets(dir: str = "decompiled"):
    secret_file = os.path.join("lostkefin_secret.json")
    if not os.path.exists(secret_file):
        sys.exit(
            "lostkefin_secret.json not found. Make sure it's in the lostkefin folder."
        )

    credentials = service_account.Credentials.from_service_account_file(
        secret_file, scopes=scopes
    )
    service = build("sheets", "v4", credentials=credentials)

    if not os.path.exists(dir):
        sys.exit(f"Directory {dir} does not exist")

    rows = get_rows(service, "TL")
    if rows[0][0] != "ID" or rows[0][1] != "JP Text" or rows[0][2] != "EN Text":
        sys.exit(
            "Header is either missing ID/JP/EN column, or they're not in the right place"
        )

    for stage in [
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
        # Filter down to rows where the ID column exists and has stageXX in it
        filtered_rows = [row for row in rows[1:] if row and stage in row[0]]

        print(f"Updating .kscript file for {stage}")
        update_kscript(os.path.join(dir, f"{stage}.kscript"), filtered_rows)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: from_sheets.py <directory of .kscript files>")
        sys.exit(1)
    from_sheets(sys.argv[1])
