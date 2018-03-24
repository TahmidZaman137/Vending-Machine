# ===================================================================================
#
# This script contains all code regarding the currency transactions made by the app.
#
# ===================================================================================

import Inventory
import AudioManager
walletLabelReference = None
brokeLabelReference = None

userWallet = 10.0


def MakeTransaction(inventoryIndex):
    global userWallet, walletLabelReference
    userWallet = userWallet - Inventory.drinks[inventoryIndex].price
    walletLabelReference.text = Inventory.as_currency(userWallet)
    return userWallet


def IsTransactionPossible(inventoryIndex, buttonInstance):
    # Added second parameter to satisfy the conditions of btn1.bind
    global userWallet, brokeLabelReference
    if userWallet >= Inventory.drinks[inventoryIndex].price:
        MakeTransaction(inventoryIndex)
        AudioManager.successNoise.play()
        brokeLabelReference.text = ""
    else:
        brokeLabelReference.text = "[color=ed1010][size=50]You broke AF[/color][/size]"
        AudioManager.failureNoise.play()



