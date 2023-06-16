import matplotlib.pyplot as plt
import numpy as np
import csv

DATA_FILE = 'datarizer/Persona_Interval.csv'
INTERVAL = 10

data = np.array([])



with open(DATA_FILE, 'r') as f:
    reader = csv.reader(f)
    rows = list(reader)

    # Iterate over the lines
    for i in range(1, len(rows)):
        data = np.append(data, int(rows[i][1]))

# std of the data
print(np.std(data))

data_unique = np.unique(data)

# Get min and max values
minVal, maxVal = min(data_unique), max(data_unique)

# Get the range between min and max
rangeVal = maxVal - minVal

# Get interval size
intervalSize = rangeVal / INTERVAL

# Get the intervals
intervals = np.arange(minVal, maxVal, intervalSize)

print(intervals)

# Get the frequency of each interval
frequency = np.zeros(INTERVAL)

for i in range(len(data_unique)):
    for j in range(len(intervals)):
        if data_unique[i] >= intervals[j] and data_unique[i] < intervals[j] + intervalSize:
            frequency[j] += 1
            break

# Plot the histogram
plt.bar(intervals, frequency, width=intervalSize, edgecolor='black')
plt.xticks(intervals)
plt.xlabel('Interval')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()