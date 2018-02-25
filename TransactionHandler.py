import Inventory
userWallet = 10.0

def IsTransactionPossible(inventoryIndex):
    global userWallet
    if userWallet < Inventory.itemPrices[inventoryIndex]:
        return False
    else:
        return True

def MakeTransaction(inventoryIndex):
    global userWallet
    userWallet = userWallet - Inventory.itemPrices[inventoryIndex]
    return userWallet

def GetUserWallet():
    return userWallet

print(IsTransactionPossible(1))

