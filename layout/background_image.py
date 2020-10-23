from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from screen.utils import get_game_screen


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
    def get_road():
        return get_game_screen().ids.road

    @staticmethod
    def get_bike():
        return get_game_screen().ids.bike

    @staticmethod
    def repeat_wrap(texture, uvsize_x=1, uvsize_y=-1):
        texture.wrap = 'repeat'
        texture.uvsize = (uvsize_x, uvsize_y)

    def redraw_textures(self, texture_name):
        texture = self.property(texture_name)
        texture.dispatch(self)

    # clouds textures

    def scroll_textures_clouds(self, dt):
        def set_ivpos(texture):
            return (texture.uvpos[0] + dt / 2.0) % Window.width, texture.uvpos[1]
        self.cloud_min_texture.uvpos = set_ivpos(self.cloud_min_texture)
        self.cloud_middle_texture.uvpos = set_ivpos(self.cloud_middle_texture)
        self.cloud_big_texture.uvpos = set_ivpos(self.cloud_big_texture)

        self.redraw_textures('cloud_min_texture')
        self.redraw_textures('cloud_middle_texture')
        self.redraw_textures('cloud_big_texture')

    # mountains textures

    def go_mountains(self, dt):
        print('go mountains')
        if self.get_road().has_finished():
            print('finish -go -r')
        else:
            def set_ivpos(texture):
                return texture.uvpos[0] + dt/10, texture.uvpos[1]
            self.mountains_texture.uvpos = set_ivpos(self.mountains_texture)

            self.repeat_wrap(self.mountains_texture)
            self.redraw_textures('mountains_texture')

    def relax_mountains(self, dt):
        print('relax mountains')
        if self.get_road().has_finished():
            print('finish -go -r')
        else:
            bike = self.get_bike()
            if bike.speed <= 0:
                return False

            def set_ivpos(texture):
                return texture.uvpos[0] + dt/10, texture.uvpos[1]
            self.mountains_texture.uvpos = set_ivpos(self.mountains_texture)

            self.repeat_wrap(self.mountains_texture)
            self.redraw_textures('mountains_texture')




