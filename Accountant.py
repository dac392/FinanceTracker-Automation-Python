from Transaction import Transaction


class Accountant:
    def __init__(self):
        self.transactions = []  # Array of Trans elements

    def add(self, date, description, amount, category):
        t = Transaction(date, description, amount, category)
        self.transactions.append(t)

    def print_transactions(self):
        for tran in self.transactions:
            print(
                f"{tran.date}, {tran.description}, $ {tran.amount}, {tran.category}")
