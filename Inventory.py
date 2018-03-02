itemNames = ["Coke", "Pepsi", "Fanta"]
itemPrices = [0.99, 8.0, 5.0]

def as_currency(amount):
    if amount >= 0:
        return '£{:,.2f}'.format(amount)
    else:
        return '-£{:,.2f}'.format(-amount)
