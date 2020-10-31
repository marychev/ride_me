from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from label.status_bar import StatusBar
from utils.texture import redraw_texture


class BackgroundImageAnimation(Widget):
    mountains_texture = ObjectProperty(Image(source='layout/mountains-1.png').texture)
    cloud_big_texture = ObjectProperty(Image(source='layout/cloud-big.png').texture)
    cloud_middle_texture = ObjectProperty(Image(source='layout/cloud-middle.png').texture)
    cloud_min_texture = ObjectProperty(Image(source='layout/cloud-min.png').texture)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.scroll_textures_clouds, 3/60)

        self.repeat_wrap(self.cloud_big_texture, uvsize_x=Window.width/self.cloud_big_texture.width)
        self.repeat_wrap(self.cloud_middle_texture, uvsize_x=Window.width/self.cloud_middle_texture.width)
        self.repeat_wrap(self.cloud_min_texture, uvsize_x=Window.width/self.cloud_min_texture.width)

    @staticmethod
    def repeat_wrap(texture, uvsize_x=1, uvsize_y=-1):
        texture.wrap = 'repeat'
        texture.uvsize = (uvsize_x, uvsize_y)

    # clouds textures

    def scroll_textures_clouds(self, dt):
        def set_ivpos(texture):
            return (texture.uvpos[0] + dt / 2.0) % Window.width, texture.uvpos[1]
        self.cloud_min_texture.uvpos = set_ivpos(self.cloud_min_texture)
        self.cloud_middle_texture.uvpos = set_ivpos(self.cloud_middle_texture)
        self.cloud_big_texture.uvpos = set_ivpos(self.cloud_big_texture)

        redraw_texture(self, 'cloud_min_texture')
        redraw_texture(self, 'cloud_middle_texture')
        redraw_texture(self, 'cloud_big_texture')

    # mountains textures

    def go_mountains(self, dt):
        if StatusBar.get_road().has_finished():
            return False
        else:
            def set_ivpos(texture):
                return texture.uvpos[0] + dt/10, texture.uvpos[1]
            self.mountains_texture.uvpos = set_ivpos(self.mountains_texture)

            self.repeat_wrap(self.mountains_texture)
            redraw_texture(self, 'mountains_texture')

    def relax_mountains(self, dt):
        if StatusBar.get_road().has_finished():
            pass
        else:
            bike = StatusBar.get_bike()
            if bike.speed <= 0:
                return False

            def set_ivpos(texture):
                return texture.uvpos[0] + dt/10, texture.uvpos[1]
            self.mountains_texture.uvpos = set_ivpos(self.mountains_texture)

            self.repeat_wrap(self.mountains_texture)
            redraw_texture(self, 'mountains_texture')
