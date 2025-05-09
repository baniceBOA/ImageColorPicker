from kivymd.app import MDApp
from kivy.uix.image import Image
from PIL import Image as PilImage


class ImageColor(Image):
    
    def on_touch_down(self, touch):
        x, y = touch.pos
        if self.collide_point(x,y):
            self.get_image_color(x,y)
            
    def get_image_color(self, x,y):
        if self.source:
            image = PilImage.open(self.source)
            img = image.resize((430, 350), PilImage.ANTIALIAS)
            flip_img = img.transpose(PilImage.FLIP_TOP_BOTTOM)
            colors = flip_img.getpixel((x-self.pos[0], y-self.pos[1]))
            app = MDApp.get_running_app()
            app.root.rgb = colors


