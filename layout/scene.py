from kivy.properties import NumericProperty, ObjectProperty, StringProperty

from bike.bike import Bike
from conf import WIDTH_GAME
from layout.base import BaseLayout
from road.road import Road
from utils.checks import background


class Scene(BaseLayout):
    id = StringProperty('scene')
    x = NumericProperty(0)
    y = NumericProperty(BaseLayout.tools_default_height())
    height = NumericProperty(BaseLayout.scene_default_height())
    width = NumericProperty(WIDTH_GAME)

    bike = ObjectProperty(None)
    road = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.bike = Bike()
        self.road = Road()

        self.add_widget(self.road)
        self.add_widget(self.bike)

        # self.background()

    # def background(self):
    #     background(self, '4d6db7')

