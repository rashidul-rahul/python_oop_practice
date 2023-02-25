class Item:
    name = ""
    all_attr = []

    def __init__(self, name: str, amount: int):
        self.name = name
        self.amount = amount
        Item.all_attr.append(self)

    def __str__(self):
        self.name

    def __repr__(self):
        return f"Item('{self.name}', {int(self.amount)})"


item1 = Item("Glass", 2)
item2 = Item("Spoon", 5)
item3 = Item("Toy", 1)
item4 = Item("Bottle", 2)
item5 = Item("Book", 3)

print(Item.all_attr)
