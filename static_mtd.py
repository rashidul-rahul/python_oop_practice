class Item:
    name = ""
    amount = ""

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
    
    @staticmethod
    def is_integer(num):
        if isinstance(num, int):
            return True
        else:
            return False


print(Item.is_integer(5))
