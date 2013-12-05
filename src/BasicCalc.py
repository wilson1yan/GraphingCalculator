'''
Created on Nov 29, 2013

@author: Wilson Yan
'''
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.clock import Clock

from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout

from sympy import simplify
from sympy.parsing.sympy_parser import parse_expr

Builder.load_file("G:\Kivy Projects\Calculator\BasicCalc.kv")

class MyButton(Button):
    pass

class RootWidget(BoxLayout):
    keys = ObjectProperty(None)
    pressed_sec = False

    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
    
    def addText(self, text):
        if text=="Clear":
            self.data = ""
        elif text=="2nd":
            self.pressed_sec = True
        elif text=="x^2":
            self.data = self.data + "^2"
        elif text=="Enter":
            val = parse_expr(self.data)
            print val
            self.data = val.__str__()
        else:
            self.data = self.data +  text;
            
class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)



class CalcApp(App):
    def build(self):        
        app = RootWidget()        
        return app
    
if __name__=='__main__':
    CalcApp().run()