from kivy.clock import Clock
from kivy.properties import NumericProperty, ObjectProperty, StringProperty
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from bike.bike import Bike
from conf import WIDTH_GAME, SECOND_GAME
from layout.base import BaseLayout
from road.road import Road
from utils.checks import set_texture_uvpos, background_texture
from kivy.lang import Builder


Builder.load_file('layout/scene.kv')


class Scene(BoxLayout):

    # x = NumericProperty(0)
    # y = NumericProperty(0)
    # height = NumericProperty(0)
    # width = NumericProperty(WIDTH_GAME)
    #
    # texture = ObjectProperty(Image(source='layout/bg-mountains.png').texture)
    # bike = ObjectProperty(Bike())
    # road = ObjectProperty(Road())

    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #
    #     self.size_hint = None, None
    #     self.y = BaseLayout.tools_default_height() + self.road.height
    #     self.height = BaseLayout.scene_default_height() - self.road.height
    #
    #     self.add_widget(self.road)
    #     self.add_widget(self.bike)
    #
    #     background_texture(self)

    def animate(self, dt):
        self.y = BaseLayout.tools_default_height()
        uvpos_x = (self.texture.uvpos[0] + 0.0005)
        set_texture_uvpos(self, uvpos_x, self.texture.uvpos[1])
