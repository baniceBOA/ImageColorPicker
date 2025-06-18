from components import ColorCard, ColorCodes, ImageColor, ImageColorSelection
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.core.window import Window

from kivy.lang import Builder
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), 'mobile.kv'))

class MobileImageColorPicker(MDBoxLayout,ImageColorSelection):
    pass
