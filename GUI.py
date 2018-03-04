# Kivy imports
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
# Vending machine imports
import TransactionHandler
import Inventory

# utility imports
from functools import partial

walletLabel = Label(text = Inventory.as_currency(TransactionHandler.userWallet))
TransactionHandler.walletLabelReference = walletLabel

brokeLabel = Label(text="", markup = True)
TransactionHandler.brokeLabelReference = brokeLabel

# BaseGUI definition
class BaseGUI(GridLayout):

    def __init__(self, **kwargs):
        global walletLabel
        global brokeLabel
        super(BaseGUI, self).__init__(**kwargs) # this has to be here, trust me...
        self.cols = 4 # sets three columns. Added widgets are inserted to the columns going left to right.

        for x in range(0, len(Inventory.itemNames)): # creates widgets for item names, item prices, and buttons through iteration.
            self.add_widget(Label(text= Inventory.itemNames[x]))
            self.add_widget(Image(source = Inventory.itemImages[x]))
            self.add_widget(Label(text= Inventory.as_currency(Inventory.itemPrices[x])))
            btn1 = Button(text="buy") # result of Button function assigned to btn1.
            btn1.bind(on_press = partial(TransactionHandler.IsTransactionPossible, x)) # IsTransactionPossible is being delegated with a given parameter to the on_press event of btn1.
            self.add_widget(btn1)

        self.add_widget(walletLabel)
        self.add_widget(brokeLabel)

class MyApp(App):

    def build(self):
        return BaseGUI() # Build according to the BaseGUI.

def DisplayGUI():
    if __name__ == '__main__':
        MyApp().run()

DisplayGUI()