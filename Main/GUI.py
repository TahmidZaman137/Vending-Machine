# ===================================================================================
#
# This is the main script which makes use of the Kivy module to design and construct
# the GUI. By running this script, the GUI of the vending machine app is executed.
#
# ===================================================================================

# Kivy imports
from kivy.config import Config
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.app import runTouchApp
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image

# Vending machine imports
import TransactionHandler
import Inventory

# Utility imports
from functools import partial

Config.set('input', 'mouse', 'mouse, multitouch_on_demand')

# BaseGUI definition


class BaseGUI(GridLayout):

    def __init__(self, **kwargs):  # defines initial properties of the GUI.
        super(BaseGUI, self).__init__(**kwargs)  # this has to be here, trust me...
        self.cols = 5
        self.size_hint_x = 1
        self.size_hint_y = 2
        self.spacing = 20

        for x in range(0, len(Inventory.drinks)):
            # for loop dynamically creates widgets for the GUI according to inventory data.
            self.add_widget(Label(text=Inventory.drinks[x].name))
            self.add_widget(Image(source=Inventory.drinks[x].image))
            Inventory.drinks[x].label = Label(text=Inventory.as_currency(Inventory.drinks[x].price))
            self.add_widget(Inventory.drinks[x].label)
            btn1 = Button(text="Buy")  # result of Button function assigned to btn1.
            btn1.bind(on_press=partial(TransactionHandler.IsTransactionPossible, x))
            # IsTransactionPossible is being delegated with a given parameter to the on_press event of btn1.
            self.add_widget(btn1)
            self.add_widget(Label(text=Inventory.drinks[x].description))

        walletLabel = Label(text="Wallet:\n" + Inventory.as_currency(TransactionHandler.userWallet))
        TransactionHandler.walletLabelReference = walletLabel

        brokeLabel = Label(text="", markup=True)
        TransactionHandler.brokeLabelReference = brokeLabel

        self.add_widget(walletLabel)
        self.add_widget(brokeLabel)
        btn2 = Button(text="Change currency")
        btn2.bind(on_press=partial(Inventory.currency_change))
        self.add_widget(btn2)

        # creates vertical scroll bar widget
        root = ScrollView(size_hint=(1, 1), size=(Window.width, Window.height))
        root.add_widget(self)
        runTouchApp(root)


class MyApp(App):

    def build(self):
        return BaseGUI()  # Build according to the BaseGUI.


def DisplayGUI():
    if __name__ == '__main__':
        MyApp().run()


DisplayGUI()
