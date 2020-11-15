from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from utils.validation import ValidObject
from utils.dir import abstract_path
from utils.texture import redraw_texture, repeat_texture

Builder.load_file(abstract_path('road/start/start.kv'))


class Start(Widget):
    texture = ObjectProperty(Image(source=abstract_path('road/finish/img/finish.jpg')).texture)

    def __init__(self, **kwargs):
        super(Start, self).__init__(**kwargs)
        repeat_texture(self.texture, 8, 8)

    def set_x(self):
        if (self.x + self.get_bike().width) > 0:
            self.x = self.get_x()
            redraw_texture(self)

    def get_x(self):
        bike = self.get_bike()
        return self.x - bike.speed

    # game objects

    def get_road(self):
        return ValidObject.road(self.parent.parent.children[1])

    def get_bike(self):
        return ValidObject.bike(self.parent.parent.children[0])

    def get_tools(self):
        return ValidObject.tools(self.parent.parent.parent.children[0])
