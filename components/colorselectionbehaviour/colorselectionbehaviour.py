from kivy.properties import StringProperty, ColorProperty, ListProperty
from kivy.utils import get_hex_from_color, get_color_from_hex
from kivymd.toast import toast
from kivy.utils import platform
from kivy.event import EventDispatcher
from kivy.uix.image import Image
from plyer import filechooser
from PIL import Image as PILImage
from kivy.clock import Clock
import colorsys

if platform == 'android':
    from android.permissions import request_permissions, Permission, check_permission

class ImageColorSelection(EventDispatcher):
    source = StringProperty('')
    rgb = ColorProperty()
    rgb_color = ColorProperty([0, 1, 1, 1])
    rgb_color_label = StringProperty()
    hsv_color = ColorProperty()
    hsv_color_label = StringProperty()
    hsl_color = ColorProperty()
    hsl_color_label = StringProperty()
    hex_color_label = StringProperty()
    hex_color  = ColorProperty()
    main_colors = ListProperty()

    def on_rgb(self, instance, value):
        self.rgb_color_label = str(value)
        self.rgb_color = value[0]/255, value[1]/255, value[2]/255

        #HSV
        hsv = colorsys.rgb_to_hsv(value[0], value[1], value[2])
        self.hsv_color_label = f'{round(hsv[0], 2)}, {round(hsv[1], 2)}, {round(hsv[2], 2)}'
        self.hsv_color = hsv

        #HSL
        h, l, s = colorsys.rgb_to_hls(value[0], value[1], value[2]) 
        self.hsl_color_label = f'{round(h, 2)}, {round(l, 2)}, {round(s, 2)}'
        self.hsl_color = [h, l, s]

        #HEX
        hex = get_hex_from_color((value[0]/255, value[1]/255, value[2]/255))
        self.hex_color_label = str(hex)
        self.hex_color = get_color_from_hex(hex)

    def on_main_colors(self, instance, value):
        
        Clock.schedule_once(self.assign_colors, 1)

    def on_source(self, instance, value):
        self.main_colors = self.get_main_colors(value) 
    
    def assign_colors(self, interval):
        if self.main_colors:
            for pos, color in enumerate(self.main_colors):
                
                r,g,b = color[1][0:3]
                self.ids[f'main_color_{pos+1}'].color = [r/255, g/255, b/255, 1]

    

    def get_main_colors(self, img):
        image = PILImage.open(img)
        colors = image.getcolors(image.size[0]*image.size[1])
        colors.sort(reverse=True)
        five_colors = colors[0:5]
        return five_colors
    
    def select_image(self):
        if platform == 'android':
            # Request specific Media permission for API 33+
            perm = Permission.READ_MEDIA_IMAGES
            if not check_permission(perm):
                request_permissions([perm], self.on_permission_result)
                return # Stop and wait for user choice
        
        # If already granted or on Desktop, open picker
        filechooser.open_file(on_selection=self.selection)
    def on_permission_result(self, permissions, results):
        if all(results):
            # Permission granted! Now open the file chooser
            Clock.schedule_once(lambda dt: filechooser.open_file(on_selection=self.selection))
        else:
            toast("Permission denied by user")
    def on_permission_result(self, permissions, results):
        if all(results):
            # Permission granted! Now open the file chooser
            Clock.schedule_once(lambda dt: filechooser.open_file(on_selection=self.selection))
        else:
            toast("Permission denied by user")
    
    def selection(self, filename):
        if filename:
            self.source = filename[0]





