#!/usr/bin/env bash
for file in out/*; do
    filename=$(basename "$file" .kscript)
    python kscript/to_csv.py "out/${filename}.kscript" "csv/${filename}.csv"
done
