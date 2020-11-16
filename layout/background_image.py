from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.widget import Widget

from layout.events.go_background import GoBackgroundMockDispatcher
from utils.texture import redraw_texture, repeat_texture, image_texture
from utils.validation import ValidObject


class BackgroundImageAnimation(Widget, GoBackgroundMockDispatcher):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.mountains_texture = image_texture('layout/img/mountains-2.png')
        self.cloud_big_texture = image_texture('layout/img/cloud-big.png')
        self.cloud_middle_texture = image_texture('layout/img/cloud-middle.png')
        self.cloud_min_texture = image_texture('layout/img/cloud-min.png')

        Clock.schedule_interval(self.scroll_textures_clouds, 3/60)

        repeat_texture(self.cloud_big_texture, uvsize_x=Window.width/self.cloud_big_texture.width)
        repeat_texture(self.cloud_middle_texture, uvsize_x=Window.width/self.cloud_middle_texture.width)
        repeat_texture(self.cloud_min_texture, uvsize_x=Window.width/self.cloud_min_texture.width)

    # clouds textures --

    def scroll_textures_clouds(self, dt):
        def __set_ivpos(texture):
            return (texture.uvpos[0] + dt / 2.0) % Window.width, texture.uvpos[1]

        self.cloud_min_texture.uvpos = __set_ivpos(self.cloud_min_texture)
        self.cloud_middle_texture.uvpos = __set_ivpos(self.cloud_middle_texture)
        self.cloud_big_texture.uvpos = __set_ivpos(self.cloud_big_texture)

        redraw_texture(self, 'cloud_min_texture')
        redraw_texture(self, 'cloud_middle_texture')
        redraw_texture(self, 'cloud_big_texture')

    # get game objects --

    def get_road(self):
        return ValidObject.road(self.parent.children[1])

    def get_status_bar(self):
        return ValidObject.status_bar(self.parent.children[2])

    def get_bike(self):
        return ValidObject.bike(self.parent.children[0])  # if self.parent else StatusBar.get_bike()

    def get_rock(self):
        if len(self.children) > 1:
            return ValidObject.rock(self.children[1])

    def get_puddle(self):
        if len(self.children) > 1:
            return ValidObject.rock(self.children[2])

    def get_lamp(self):
        if len(self.children) > 1:
            return ValidObject.rock(self.children[3])

    def get_start(self):
        if len(self.children) > 1:
            return ValidObject.start(self.children[2])

    def get_finish(self):
        if len(self.children) > 1:
            return ValidObject.finish(self.children[0])
