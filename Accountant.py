from Transaction import Transaction


class Accountant:
    def __init__(self):
        self.income = 0
        self.expenses = 0
        self.profit = 0
        self.transactions = []  # Array of Trans elements

    def add(self, date, description, amount):
        t = Transaction(date, description, amount)
        self.transactions.append(t)
        self.profit += t.amount

        if(t.amount > 0):
            self.income += t.amount
        else:
            self.expenses += t.amount

    def get_totals(self):
        return {"income": round(self.income, 2), "expenses": round(self.expenses, 2), "profit": round(self.profit, 2)}

    def print_transactions(self):
        for tran in self.transactions:
            print(
                f"{tran.date}, {tran.description}, $ {tran.amount}, {tran.category}")
