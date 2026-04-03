__version__ = "1.0.2"
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty, ColorProperty, ListProperty
from PIL import Image
from utils import ImageProcessor
from screens import MobileImageColorPicker, ComputerImageColorPicker
from kivy.utils import platform 
import os

import colorsys

class MainApp(MDApp):

    def build(self):
        if platform == 'android':
            return MobileImageColorPicker()
        else:
            return ComputerImageColorPicker()
    def on_start(self):
        # Executed when the app starts 
        if platform == 'android':
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
    def on_stop(self):
        """
        Executed when the user closes the app.
        """
        if platform == 'android':
            self.clear_image_cache()
    def clear_image_cache(self):
        # Define the same path used in your selection logic
        cache_path = os.path.join(self.user_data_dir, 'image_cache')
        
        # Call the cleanup utility
        ImageProcessor.clear_cache(cache_path)

    def get_main_colors(self, img):
        image = Image.open(img)
        colors = image.getcolors(image.size[0]*image.size[1])
        colors.sort(reverse=True)
        five_colors = colors[0:5]
        return five_colors
    

if __name__ == '__main__':
    MainApp().run()
