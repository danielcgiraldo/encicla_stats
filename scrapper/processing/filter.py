import csv

# Using data from scrapper

DAYS = ["2023-06-01", "2023-06-02", "2023-06-06", "2023-06-07", "2023-06-08", "2023-06-09"]
TIME_INTERVAL = ["14", "15"]

def time_to_seconds(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    return hours * 3600 + minutes * 60 + seconds

# Read csv
with open("data.csv", 'r') as f:
    reader = csv.reader(f)

    rows = list(reader)

    for i in range(len(rows)):
        row = rows[i]
        if row[2] in DAYS and row[3][:2] in TIME_INTERVAL and row[0] == "Suramericana":
            j = 1
            next_row = rows[i + j]
            while next_row[0] != "Suramericana":
                j += 1
                next_row = rows[i + j]
            # From next_row hour subtract row hour
            time_diff = time_to_seconds(next_row[3]) - time_to_seconds(row[3])

            if int(row[1]) + 1 == int(next_row[1]):
                with open(f"suramericana/entrega.csv", 'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow([row[2], time_diff])
            elif int(row[1]) - 1 == int(next_row[1]):
                with open(f"suramericana/persona.csv", 'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow([row[2], time_diff])
            elif int(row[1]) + 2 == int(next_row[1]):
                with open(f"suramericana/entrega.csv", 'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow([row[2], time_diff])
                    writer.writerow([row[2], 0])
            elif int(row[1]) - 2 == int(next_row[1]):
                with open(f"suramericana/persona.csv", 'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow([row[2], time_diff])
                    writer.writerow([row[2], 0])