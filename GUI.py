# Kivy imports
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
# Vending machine imports
import TransactionHandler
import Inventory

# utility imports
from functools import partial

# BaseGUI definition
class BaseGUI(GridLayout):

    def __init__(self, **kwargs):
        super(BaseGUI, self).__init__(**kwargs) # this has to be here, trust me...
        self.cols = 3 # sets three columns. Added widgets are inserted to the columns going left to right.

        for x in range(0, 3): # creates widgets for item names, item prices, and buttons through iteration.
            self.add_widget(Label(text=Inventory.itemNames[x]))
            self.add_widget(Label(text=str(Inventory.itemPrices[x])))
            btn1 = Button(text="buy") # result of Button function assigned to btn1.
            btn1.bind(on_press = partial(TransactionHandler.IsTransactionPossible, x)) # IsTransactionPossible is being delegated with a given parameter to the on_press event of btn1.
            self.add_widget(btn1)

class MyApp(App):

    def build(self):
        return BaseGUI() # Build according to the BaseGUI.

def DisplayGUI():
    if __name__ == '__main__':
        MyApp().run()

DisplayGUI()