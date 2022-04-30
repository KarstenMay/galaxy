from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.metrics import dp
from kivy.properties import StringProperty
import numpy as np

class WidgetsExample(GridLayout):
    my_text = StringProperty("Hello!")
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.n = 0

        
    def on_button_click(self):
        self.n = np.random.randint(1,6)
        self.my_text = str(self.n)
        
    

class BoxLayoutExample(BoxLayout):
    """    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        b1 = Button(text="A")
        b2 = Button(text="B")
        self.add_widget(b1)
        self.add_widget(b2)
    """
    pass
                       
class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass

TheLabApp().run()