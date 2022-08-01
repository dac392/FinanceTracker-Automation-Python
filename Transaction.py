from Data import desc_list


class Transaction:
    def __init__(self, date, description, amount, category):
        self.date = date
        self.description = description
        self.amount = amount
        self.category = category
        self.cleanup()

    def cleanup(self):
        if("Zelle" in self.description):
            person = self.description.split("; ")[1]
            self.description = f"Zelle: {person}"
        else:
            keys = desc_list.keys()
            for key in keys:
                if key in self.description:
                    self.description = desc_list[key]
                    break


if __name__ == "__main__":
    some = Transaction(
        None, "Zelle Transfer Conf# 2SY6MBAFK; Jose Henriquez", None, None)
    # some.cleanup()
