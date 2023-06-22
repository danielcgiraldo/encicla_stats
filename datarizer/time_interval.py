import csv

FILE_READ = "Entrega"

def time_to_seconds(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    return hours * 3600 + minutes * 60 + seconds

with open(f"datarizer/preprocessing/fixed.csv", 'r') as f:
    reader = csv.reader(f)
    list_reader = list(reader)

    for i in range(len(list_reader)):
        print(i)
        row = list_reader[i]
        if row[1][:2] not in ["14", "15"] or row[0] != "16/06/2023" or row[2] != FILE_READ:
            continue
        row_next = list_reader[i + 1]
        while row_next[2] != FILE_READ:
            row_next = list_reader[i + 1]
            i += 1
        if row_next[0] != "16/06/2023":
            continue
        time_diff = time_to_seconds(row_next[1]) - time_to_seconds(row[1])
        with open(f"data/{FILE_READ}.csv", 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([time_diff])