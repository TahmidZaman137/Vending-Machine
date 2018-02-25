from Inventory import itemPrices
userWallet = 10.0

def IsTransactionPossible(inventoryIndex):
    global userWallet
    if userWallet < itemPrices[inventoryIndex]:
        return False
    else:
        return True

def MakeTransaction(inventoryIndex):
    global userWallet
    userWallet = userWallet - itemPrices[inventoryIndex]
    return userWallet

def GetUserWallet():
    return userWallet

print(IsTransactionPossible(1))
