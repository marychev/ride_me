from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.clock import Clock


class BackgroundImageAnimation(Widget):
    mountains_texture = ObjectProperty(Image(source='layout/mountains-1.png').texture)
    cloud_big_texture = ObjectProperty(Image(source='layout/cloud-big.png').texture)
    cloud_middle_texture = ObjectProperty(Image(source='layout/cloud-middle.png').texture)
    cloud_min_texture = ObjectProperty(Image(source='layout/cloud-min.png').texture)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.scroll_textures, 3/60)

        self.cloud_big_texture.wrap = 'repeat'
        self.cloud_big_texture.uvsize = (Window.width/self.cloud_big_texture.width, -1)
        self.cloud_middle_texture.wrap = 'repeat'
        self.cloud_middle_texture.uvsize = (Window.width/self.cloud_middle_texture.width, -1)

        self.cloud_min_texture.wrap = 'repeat'
        self.cloud_min_texture.uvsize = (Window.width/self.cloud_min_texture.width, -1)

    def scroll_textures(self, dt):
        def set_ivpos(texture):
            return (texture.uvpos[0] + dt / 2.0) % Window.width, texture.uvpos[1]

        self.cloud_min_texture.uvpos = set_ivpos(self.cloud_min_texture)
        self.cloud_middle_texture.uvpos = set_ivpos(self.cloud_middle_texture)
        self.cloud_big_texture.uvpos = set_ivpos(self.cloud_big_texture)

        # redraw the textures
        texture = self.property('cloud_min_texture')
        texture.dispatch(self)
        texture = self.property('cloud_middle_texture')
        texture.dispatch(self)
        texture = self.property('cloud_big_texture')
        texture.dispatch(self)

