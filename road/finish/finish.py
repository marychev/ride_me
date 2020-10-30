from layout.background_image import BackgroundImageAnimation
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, NumericProperty
from kivy.lang import Builder
from utils.validation import ValidObject
from utils.texture import redraw_texture

Builder.load_file("road/finish/finish.kv")


class Finish(Widget):
    texture = ObjectProperty(Image(source='road/finish/img/finish.jpg').texture)

    def __init__(self, **kwargs):
        super(Finish, self).__init__(**kwargs)
        BackgroundImageAnimation.repeat_wrap(self.texture, 8, 8)

    def set_x(self):
        self.x = self.get_x()
        redraw_texture(self)

    def get_x(self):
        bike = self.get_bike()
        road = self.get_road()
        return (road.total_way - road.distance_traveled) + bike.x + bike.width

    # general elements and functions

    def get_road(self):
        return ValidObject.road(self.parent.parent.children[1])

    def get_bike(self):
        return ValidObject.bike(self.parent.parent.children[0])

    def get_tools(self):
        return ValidObject.tools(self.parent.parent.parent.children[0])

    # initialization

    def init_pos(self):
        return -self.width, self.get_tools().height

    def init_size(self):
        return 80, self.get_road().height

