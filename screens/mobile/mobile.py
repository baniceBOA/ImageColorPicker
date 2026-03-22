from components import ColorCard, ColorCodes, ImageColor, ImageColorSelection
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window

from kivy.lang import Builder
from kivy.utils import platform
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), 'mobile.kv'))

class MobileImageColorPicker(MDScreen,ImageColorSelection):
    pass
