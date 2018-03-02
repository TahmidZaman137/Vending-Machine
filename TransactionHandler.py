import Inventory
walletlabelReference = None
brokelabelReference = None

userWallet = 10.0

def MakeTransaction(inventoryIndex):
    global userWallet, walletlabelReference
    userWallet = userWallet - Inventory.itemPrices[inventoryIndex]
    walletlabelReference.text = Inventory.as_currency(userWallet)
    return userWallet

def IsTransactionPossible(inventoryIndex, buttonInstance): # Added second parameter to satisfy the conditions of btn1.bind
    global userWallet, brokelabelReference
    print("is checking possibility?")
    if userWallet >= Inventory.itemPrices[inventoryIndex]:
        MakeTransaction(inventoryIndex)
        brokelabelReference.text = "[color=000000][size=50]You broke AF[/color][/size]"
    else:
        brokelabelReference.text = "[color=ed1010][size=50]You broke AF[/color][/size]"



def GetUserWallet():
    return userWallet



