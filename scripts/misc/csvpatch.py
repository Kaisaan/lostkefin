import sys
import csv

csvName = sys.argv[1]
patchName = sys.argv[2]

csvFile = open(f"{csvName}", "r", newline="", encoding="utf-8")

patchFile = open(f"{patchName}", "w", encoding="utf-8")

reader = csv.reader(csvFile)
next(reader)

for row in reader:
    offset = row[0]
    text = row[2]
    text = text.replace("\n", "\\n")
    #text = text.replace("\"", "\"")

    patchFile.write(f".orga 0x{offset}\n.str \"{text}\"\n\n")