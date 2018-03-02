import Inventory
walletLabelReference = None
brokeLabelReference = None

userWallet = 10.0

def MakeTransaction(inventoryIndex):
    global userWallet, walletLabelReference
    userWallet = userWallet - Inventory.itemPrices[inventoryIndex]
    walletLabelReference.text = Inventory.as_currency(userWallet)
    return userWallet

def IsTransactionPossible(inventoryIndex, buttonInstance): # Added second parameter to satisfy the conditions of btn1.bind
    global userWallet, brokeLabelReference
    if userWallet >= Inventory.itemPrices[inventoryIndex]:
        MakeTransaction(inventoryIndex)
        brokeLabelReference.text = ""
    else:
        brokeLabelReference.text = "[color=ed1010][size=50]You broke AF[/color][/size]"



