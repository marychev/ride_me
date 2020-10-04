from kivy.clock import Clock
from kivy.properties import NumericProperty, ObjectProperty, StringProperty
from kivy.uix.image import Image

from bike.bike import Bike
from conf import WIDTH_GAME, SECOND_GAME
from layout.base import BaseLayout
from road.road import Road
from utils.checks import set_texture_uvpos, background_texture


# TODO: y = +100 ? as road_y
class Scene(BaseLayout):
    id = StringProperty('scene')
    x = NumericProperty(0)
    y = NumericProperty(BaseLayout.tools_default_height() + 100)
    #
    height = NumericProperty(BaseLayout.scene_default_height())
    width = NumericProperty(WIDTH_GAME)

    texture = ObjectProperty(Image(source='layout/bg-mountains.png').texture)

    bike = ObjectProperty(None)
    road = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.animate, SECOND_GAME)
        self.size_hint = None, None

        self.bike = Bike()
        self.road = Road()

        self.add_widget(self.road)
        self.add_widget(self.bike)

        background_texture(self)

    def animate(self, dt):
        # todo: 100
        self.y = BaseLayout.tools_default_height() + 100
        uvpos_x = (self.texture.uvpos[0] + 0.0005)
        set_texture_uvpos(self, uvpos_x, self.texture.uvpos[1])
