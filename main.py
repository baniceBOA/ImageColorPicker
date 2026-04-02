from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty, ColorProperty, ListProperty
from PIL import Image
from screens import MobileImageColorPicker, ComputerImageColorPicker
from kivy.utils import platform 

import colorsys

class MainApp(MDApp):

    def build(self):
        if platform == 'android':
            return MobileImageColorPicker()
        else:
            return ComputerImageColorPicker()
    def on_start(self):
        #self.root.main_colors = self.get_main_colors(self.root.source)
        if platform == 'android':
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
        pass 

    def get_main_colors(self, img):
        image = Image.open(img)
        colors = image.getcolors(image.size[0]*image.size[1])
        colors.sort(reverse=True)
        five_colors = colors[0:5]
        return five_colors
    

if __name__ == '__main__':
    MainApp().run()
