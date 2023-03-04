from item import Item


class Phone(Item):
    def __init__(self, name, amount, quantity, broken_phone):
        super().__init__(
                name, amount, quantity
                )
        self.broken_phone = broken_phone
