import csv
MONTH = input('Which month are we doing today boss? ')

file_name = f"statements/boa_{MONTH}.csv"
count = 0
with open(file_name, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        # maybe it should be 7
        if(count > 6):
            print(row)
        count += 1
