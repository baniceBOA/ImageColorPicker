from kivymd.uix.card import MDCard
from kivy.properties import ColorProperty
from kivy.lang import Builder
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), 'colorcard.kv'))


class ColorCard(MDCard):
    color = ColorProperty([1,1,1,1])
    pass