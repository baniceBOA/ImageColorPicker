from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.core.clipboard import Clipboard
from kivy.properties import ColorProperty, StringProperty
from kivy.lang import Builder
import os
Builder.load_file(os.path.join(os.path.dirname(__file__), 'colorcodes.kv'))

class ColorCodes(MDRelativeLayout):
    color = ColorProperty()
    color_label = StringProperty()
    declaration_lbl = StringProperty()

    def copy(self):
        Clipboard.copy(self.color_label)

