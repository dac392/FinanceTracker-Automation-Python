from Data import desc_list


class Transaction:
    def __init__(self, date, description, amount, category):
        self.date = date
        self.description = description
        self.amount = amount
        self.category = category
        self.cleanup()

    def cleanup(self):
        keys = desc_list.keys()
        for key in keys:
            if key in self.description:
                self.description = desc_list[key]
                # print(self.description)
                break


if __name__ == "__main__":
    some = Transaction(
        None, "VENMO DES:PAYMENT ID:XXXXX49432169 INDN:DIEGO CASTELLANOS CO ID:XXXXX81992 WEB", None, None)
    some.cleanup()
