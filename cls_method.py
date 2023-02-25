import csv


class Item:
    name = ""
    all = []

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
        Item.all.append(self)

    @classmethod
    def instantiate_from_csv(cls):
        with open("items.csv", "r") as f:
            data = csv.DictReader(f)
            items = list(data)

        for item in items:
            cls(
                    name=item["name"],
                    amount=int(item["amount"]),
                    )

    def __repr__(self):
        return f"Item('{self.name}', {self.amount})"


Item.instantiate_from_csv()

print(Item.all)
