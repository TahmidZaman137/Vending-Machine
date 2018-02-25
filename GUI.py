# Kivy imports
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
# Vending machine imports
import Inventory

# BaseGUI definition
class BaseGUI(GridLayout):

    def __init__(self, **kwargs):
        super(BaseGUI, self).__init__(**kwargs) # this has to be here, trust me...
        self.cols = 2 # sets two columns. Added widgets are inserted to the columns going left to right.
        self.add_widget(Label(text=Inventory.itemNames[0]))
        self.add_widget(Label(text=str(Inventory.itemPrices[0])))


class MyApp(App):

    def build(self):
        return BaseGUI() # Build according to the BaseGUI.

def DisplayGUI():
    if __name__ == '__main__':
        MyApp().run()

DisplayGUI()