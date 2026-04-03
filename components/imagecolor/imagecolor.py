from kivymd.app import MDApp
from kivymd.toast import toast
from kivy.properties import NumericProperty
from kivy.uix.image import Image
from kivy.core.window import Window
from PIL import Image as PilImage


class ImageColor(Image):
    Image_width = NumericProperty(350)
    Image_height = NumericProperty(450)

    def on_source(self, instance, value):
        if value:
            self.__size = self.get_image_size(value)
            self.Image_width, self.Image_height = min(self.__size[0], Window.size[0]*0.9), min(self.__size[1], Window.size[1]*0.6)
    
    def get_image_size(self, img):
        image = PilImage.open(img)
        return image.size

    def on_touch_down(self, touch):
        x, y = touch.pos
        if self.collide_point(x,y):
            self.get_image_color(x,y)
            
    def get_image_color(self, x,y):
        if self.source:
            try:
                image = PilImage.open(self.source)
                img = image.resize((430, 350), PilImage.LANCZOS)
                flip_img = img.transpose(PilImage.Transpose.FLIP_TOP_BOTTOM)
                colors = flip_img.getpixel((x-self.pos[0], y-self.pos[1]))
                app = MDApp.get_running_app()
                app.root.rgb = colors
            except Exception as e:
                toast(f"Error getting color: {e}")


