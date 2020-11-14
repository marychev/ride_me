from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from utils.dir import abstract_path
from utils.texture import redraw_texture, repeat_texture
from utils.validation import ValidObject

Builder.load_file(abstract_path('road/finish/finish.kv'))


class Finish(Widget):
    texture = ObjectProperty(Image(source=abstract_path('road/finish/img/finish.jpg')).texture)

    def __init__(self, **kwargs):
        super(Finish, self).__init__(**kwargs)
        repeat_texture(self.texture, 8, 8)

    def set_x(self):
        self.x = self.get_x()
        redraw_texture(self)

    def get_x(self):
        bike = self.get_bike()
        road = self.get_road()
        return (road.total_way - road.distance_traveled) + bike.x + bike.width

    # game objects

    def get_road(self):
        return ValidObject.road(self.parent.parent.children[1])

    def get_bike(self):
        return ValidObject.bike(self.parent.parent.children[0])

    def get_tools(self):
        return ValidObject.tools(self.parent.parent.parent.children[0])
