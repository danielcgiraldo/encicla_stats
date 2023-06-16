# Read csv

import csv
import os

SELECTOR = "Entrega"

with open("datarizer/fixed.csv", 'r') as f:
    reader = csv.reader(f)

    # Iterate over the lines
    for row in reader:
        if row[2] == SELECTOR:
            # Add the line to the file
            with open(f"datarizer/{SELECTOR}.csv", 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(row)

            