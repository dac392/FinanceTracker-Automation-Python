import csv
import gspread
import time
from Accountant import Accountant

BOA_OFFSET = 7


def get_transactions(MONTH, YEAR):
    file_name = f"statements/boa_{MONTH}{YEAR}.csv"
    count = 0
    accountant = Accountant()
    sum = 0
    with open(file_name, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if(count > BOA_OFFSET):
                date = row[0]
                desc = row[1]
                amount = round(float(row[2].replace(',', '')), 2)
                accountant.add(date, desc, amount)
                sum += amount
            count += 1
    # accountant.print_transactions()
    print(f"You made: ${round(sum, 2)} on {MONTH}{YEAR}")
    return accountant


def worksheet_setup(worksheet, income, expenses, profit):
    worksheet.update("A1", "Total")
    worksheet.format("A1", {
        "textFormat": {
            "fontSize": 12,
            "bold": True
        }
    })

    worksheet.update("A2", "Income")
    worksheet.update("B2", f"{income}")

    worksheet.update("A3", "Expenses")
    worksheet.update("B3", f"{expenses}")

    worksheet.update("A4", "Profit")
    worksheet.update("B4", f"{profit}")

    worksheet.format("B2:B4", {
        "numberFormat": {
            "type": "CURRENCY"
        },
        "horizontalAlignment": "Right"
    })
    worksheet.insert_row(["Date", "Description", "Category", "Amount"], 6)
    worksheet.format("A6:D6", {
        "textFormat": {
            "fontSize": 12,
            "bold": True
        }
    })


if __name__ == "__main__":
    MONTH = input('Which month are we doing today, boss? ')
    YEAR = input("Which year is this on, boss? ")
    bank_stmt = get_transactions(MONTH, YEAR)
    totals = bank_stmt.get_totals()
    sa = gspread.service_account()
    spreadsheet = sa.open("Personal Finances")
    worksheet = spreadsheet.add_worksheet(
        title=f"{MONTH}{YEAR}", rows="100", cols="20")

    worksheet_setup(worksheet, totals["income"],
                    totals["expenses"], totals["profit"])
    for transaction in bank_stmt.transactions:
        worksheet.insert_row(transaction.items_as_list(), 8)
        time.sleep(2)
