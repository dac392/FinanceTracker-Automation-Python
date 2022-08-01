import csv
import gspread

from Accountant import Accountant

MONTH = input('Which month are we doing today, boss? ')
YEAR = input("Which year is this on, boss? ")

file_name = f"statements/boa_{MONTH}{YEAR}.csv"
count = 0
accountant = Accountant()

with open(file_name, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        # maybe it should be 7
        if(count > 7):
            date = row[0]
            desc = row[1]
            amount = float(row[2].replace(',', ''))
            accountant.add(date, desc, amount)
        count += 1

accountant.print_transactions()
# sa = gspread.service_account()
# sh = sa.open("Personal Finances")
