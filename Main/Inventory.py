# ===================================================================================
#
# This script contains all code pertaining to the items sold by the vending machine.
#
# ===================================================================================

import GUI
import TransactionHandler


class Item:
    def __init__(self, name, price, description):
        path_to_images = r"C:\Users\tahmi\OneDrive\Documents\Git\Vending-Machine\Images\\"
        self.name = name
        self.image = path_to_images + self.name + ".jpg"
        self.price = price
        self.description = description
        self.label = None


coke_desc = "Coca-Cola is the most popular soft drink in history, as well as the best-known brand in the world."
pepsi_desc = "Pay each penny to save Israel."
fanta_desc = "Bright, bubbly and instantly refreshing, Fanta is made with 100% natural flavors and is caffeine free."
drpep_desc = "The unique taste of 'Dr Pepper' - 'What's the worst that could happen?"
redbull_desc = "Red bull energy drink is a functional beverage providing wings whenever you need them."
monster_desc = "Tear into a can of Monster Energy,\n the meanest energy drink on the planet."

coke = Item("Coke", 0.99, coke_desc)
pepsi = Item("Pepsi", 8.0, pepsi_desc)
fanta = Item("Fanta", 5.0, fanta_desc)
drpepper = Item("Dr Pepper", 0.50, drpep_desc)
redbull = Item("Redbull", 0.30, redbull_desc)
monster = Item("Monster", 0.10, monster_desc)

drinks = [coke, pepsi, fanta, drpepper, redbull, monster]

currencies = ["£", "$", "Y"]

currentCurrencyIndex = 0


def as_currency(amount):
    global currentCurrencyIndex
    if amount >= 0:
        currency_format = currencies[currentCurrencyIndex] + '{:,.2f}'
        if currentCurrencyIndex == 1:
            newAmount = amount*1.41
            return currency_format.format(newAmount)
        if currentCurrencyIndex == 2:
            newAmount = amount*148.96
            return currency_format.format(newAmount)
        return currency_format.format(amount)
    elif amount < 0:
        currency_format = "-" + currencies[currentCurrencyIndex] + '{:,.2f}'
        if currentCurrencyIndex == 1:
            newAmount = amount * 1.41
            return currency_format.format(newAmount)
        if currentCurrencyIndex == 2:
            newAmount = amount*148.96
            return currency_format.format(newAmount)
        return currency_format.format(amount)


def currency_change(buttonInstance):
    global currentCurrencyIndex
    currentCurrencyIndex += 1
    if currentCurrencyIndex >= 3:
        currentCurrencyIndex = 0

    for x in range(0, len(drinks)):
        drinks[x].label.text = as_currency(drinks[x].price)
    TransactionHandler.walletLabelReference.text = as_currency(TransactionHandler.userWallet)




