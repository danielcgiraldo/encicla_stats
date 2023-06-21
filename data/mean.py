import csv
import numpy as np

with open('data/suramericana/persona.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # skip header
    sur_data = [int(row[1]) for row in reader]

with open('data/unal/persona.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # skip header
    unal_data = [int(row[1]) for row in reader]

print(np.mean(sur_data))
print(np.mean(unal_data))