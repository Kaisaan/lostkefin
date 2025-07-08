import csv
import os
import sys


# Handle imports for both module and script execution
try:
    # When imported as a module
    from .update_kscript import update_kscript
except ImportError:
    # When run as a script
    from update_kscript import update_kscript


def from_csv(csv_dir: str, kscript_dir: str):
    if not os.path.exists(csv_dir):
        sys.exit(f"Directory {csv_dir} does not exist")
    if not os.path.exists(kscript_dir):
        sys.exit(f"Directory {kscript_dir} does not exist")

    for filename in os.listdir(csv_dir):
        if filename not in [
            "stage00.csv",
            "stage10.csv",
            "stage20.csv",
            "stage30.csv",
            "stage40.csv",
            "stage50.csv",
            "stage60.csv",
            "stage70.csv",
            "stage80.csv",
            "stage90.csv",
            "stagea0.csv",
            "stageb0.csv",
        ]:
            continue
        print(f"Processing {filename}")

        with open(os.path.join(csv_dir, filename), "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            rows = list(reader)
            kscript_filename = filename.replace(".csv", ".kscript")
            update_kscript(os.path.join(kscript_dir, kscript_filename), rows[1:])


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(
            "Usage: from_csv.py <directory of .csv files> <directory of .kscript files>"
        )
        sys.exit(1)
    from_csv(sys.argv[1], sys.argv[2])
