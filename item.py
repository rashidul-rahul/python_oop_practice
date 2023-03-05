import csv


class Item:
    all = []

    def __init__(self, name, amount, quantity):
        self.__name = name
        self.amount = amount
        self.quantity = quantity

        self.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def calculate_price(self):
        return self.amount * self. quantity

    @classmethod
    def instantiated_from_csv(cls):
        with open("items.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)

            for item in items:
                cls(
                        name=item["name"],
                        amount=10,
                        quantity=item["amount"]
                        )

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.amount}, {self.quantity})"
