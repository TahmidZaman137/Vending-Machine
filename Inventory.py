itemNames = ["Coke", "Pepsi", "Fanta", "Dr Pepper", "Redbull", "Monster"]
itemImages = ["coke.jpg", "pepsi.jpg", "fanta.jpg", "dr-pepper.jpg", "redbull.jpeg", "monster.jpg"]
itemPrices = [0.99, 8.0, 5.0, 0.50, 0.49, 0.01]

def as_currency(amount):
    if amount >= 0:
        return '£{:,.2f}'.format(amount)
    else:
        return '-£{:,.2f}'.format(-amount)
