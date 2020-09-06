from kivy.core.window import Window
from kivy.properties import NumericProperty, ObjectProperty
from layout.base import BaseLayout
from bike.bike import Bike


class Scene(BaseLayout):
    x = NumericProperty(0)
    y = NumericProperty(Window.height / 4)
    height = NumericProperty(BaseLayout.scene_default_height())
    width = NumericProperty(Window.width)
    bike = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bike = Bike()
        self.add_widget(self.bike)

        self.bike.lending()



