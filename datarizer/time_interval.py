import csv

FILE_READ = "Prestamo"

def time_to_seconds(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    return hours * 3600 + minutes * 60 + seconds

with open(f"unal/fixed.csv", 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[1][:2] not in ["14", "15"] or row[0] not in ["7/6/2023", "8/6/2023", "14/6/2023"] or row[2] != FILE_READ:
            continue
        
        row_next = next(reader)
        while row_next[2] != FILE_READ:
            row_next = next(reader)
        time_diff = time_to_seconds(row_next[1]) - time_to_seconds(row[1])
        if time_diff > 500:
            print(row)
            continue
        with open(f"unal/{FILE_READ}.csv", 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([time_diff])