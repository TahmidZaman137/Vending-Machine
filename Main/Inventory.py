class Item:
    def __init__(self, name, price):
        pathToImages = r"C:\Users\tahmi\OneDrive\Documents\Git\Vending-Machine\Images\\"
        self.name = name
        self.image = pathToImages + self.name + ".jpg"
        self.price = price

coke = Item("Coke", 0.99)
pepsi = Item("Pepsi", 8.0)
fanta = Item("Fanta", 5.0)
drpepper = Item("Dr Pepper", 0.50)
redbull = Item("Redbull", 0.49)
monster = Item("Monster", 0.01)

drinks = [coke, pepsi, fanta, drpepper, redbull, monster]

def as_currency(amount):
    if amount >= 0:
        return '£{:,.2f}'.format(amount)
    else:
        return '-£{:,.2f}'.format(-amount)
