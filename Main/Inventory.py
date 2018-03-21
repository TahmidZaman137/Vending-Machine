#===================================================================================
#
# This script contains all code pertaining to the items sold by the vending machine.
#
#===================================================================================

class Item:
    def __init__(self, Name, Price, Description):
        pathToImages = r"C:\Users\tahmi\OneDrive\Documents\Git\Vending-Machine\Images\\"
        self.name = Name
        self.image = pathToImages + self.name + ".jpg"
        self.price = Price
        self.description = Description

coke = Item("Coke", 0.99, "Coca-Cola is the most popular soft drink in history, as well as the best-known brand in the world.")
pepsi = Item("Pepsi", 8.0, "Pay each penny to save Israel.")
fanta = Item("Fanta", 5.0,"Bright, bubbly and instantly refreshing, Fanta is made with 100% natural flavors and is caffeine free.")
drpepper = Item("Dr Pepper", 0.50, "The unique taste of 'Dr Pepper' - 'What's the worst that could happen?")
redbull = Item("Redbull", 0.49, "Red bull energy drink is a functional beverage providing wings whenever you need them.")
monster = Item("Monster", 0.01, "Tear into a can of Monster Energy,\n the meanest energy drink on the planet.")

drinks = [coke, pepsi, fanta, drpepper, redbull, monster]

def as_currency(amount):
    if amount >= 0:
        return '£{:,.2f}'.format(amount)
    else:
        return '-£{:,.2f}'.format(-amount)

