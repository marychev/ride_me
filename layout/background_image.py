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

        self.repeat_wrap(self.cloud_big_texture)
        self.repeat_wrap(self.cloud_middle_texture)
        self.repeat_wrap(self.cloud_min_texture)

    @staticmethod
    def repeat_wrap(texture, uvsize_y=-1):
        texture.wrap = 'repeat'
        texture.uvsize = (Window.width/texture.width, uvsize_y)

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
        def set_ivpos(texture):
            return texture.uvpos[0] + dt/10, texture.uvpos[1]
        self.mountains_texture.uvpos = set_ivpos(self.mountains_texture)

        self.repeat_wrap(self.mountains_texture)
        self.redraw_textures('mountains_texture')

    def relax_mountains(self, dt):
        road = get_game_screen().ids.road
        if road.acceleration <= 0:
            return False

        def set_ivpos(texture):
            # return texture.uvpos[0] + (road.acceleration/2) / 1000, texture.uvpos[1]
            return texture.uvpos[0] + dt/10, texture.uvpos[1]
        self.mountains_texture.uvpos = set_ivpos(self.mountains_texture)

        self.redraw_textures('mountains_texture')




