import csv

FILE_READ = "Entrega"

def time_to_seconds(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    return hours * 3600 + minutes * 60 + seconds

with open(f"datarizer/{FILE_READ}.csv", 'r') as f:
    reader = csv.reader(f)
    rows = list(reader)  # Convert reader to a list for easier indexing

    # Iterate over the lines
    for i in range(len(rows) - 1):
        row = rows[i]
        next_row = rows[i + 1]
        if row[0] == next_row[0]:
            # From next_row hour subtract row hour
            time_diff = time_to_seconds(next_row[1]) - time_to_seconds(row[1])
            with open(f"datarizer/{FILE_READ}_Interval.csv", 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([row[0], time_diff])
