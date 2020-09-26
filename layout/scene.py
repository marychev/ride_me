from kivy.core.window import Window
from kivy.properties import NumericProperty, ObjectProperty
from layout.base import BaseLayout
from conf import WIDTH_GAME, HEIGHT_GAME
from bike.bike import Bike
from utils.checks import background


class Scene(BaseLayout):
    x = NumericProperty(0)
    y = NumericProperty(BaseLayout.tools_default_height())
    height = NumericProperty(BaseLayout.scene_default_height())
    width = NumericProperty(WIDTH_GAME)

    bike = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # self.bike = Bike()
        # self.add_widget(self.bike)

        self.background()

    def background(self):
        background(self, '4d6db7')
