# Read csv

import csv
import os

# Fixed file to store lines
fixed = []

with open("datarizer/data.csv", 'r') as f:
    reader = csv.reader(f)
    rows = list(reader)

    # Iterate over the lines
    for i in range(1, len(rows)):
        row = rows[i]
        if row[1][:2] in ["14", "15"]:
            if row[0] == "1/6/2023" and i + 1 < len(rows):
                next_row = rows[i + 1]
                if next_row[2] == "Entrega":
                    continue
            fixed.append(row)

# Write the fixed lines to a new file
with open("datarizer/fixed.csv", 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(fixed)