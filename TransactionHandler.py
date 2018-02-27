import Inventory
userWallet = 10.0

def IsTransactionPossible(inventoryIndex, buttonInstance): # Added second parameter to satisfy the conditions of btn1.bind
    global userWallet
    print("is checking possibility?")
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

