from kivy.uix.image import Image
from kivy.uix.widget import Widget
from label.status_bar import StatusBar
from utils.texture import redraw_texture
from utils.validation import ValidObject


class GameImage(Widget):
    @classmethod
    def create(cls, pos, size=None):
        size = size if size else cls.TEXTURE.size
        kwargs = {
            "pos": pos,
            "size": size,
            "size_hint": (None, None)}
        return cls(**kwargs)

    @classmethod
    def to_map(cls, pos):
        return {"name": cls.__name__, "pos": pos}

    def get_x(self):
        bike = self.get_bike()
        return self.x - bike.speed if bike else self.x

    def set_x(self):
        self.x = self.get_x()
        redraw_texture(self)

    # general elements and functions

    def get_road(self):
        return ValidObject.road(self.parent.parent.children[1])

    def get_bike(self):
        if self.parent:
            return self.parent.get_bike()
        else:
            return StatusBar.get_bike()

    def get_tools(self):
        return ValidObject.tools(self.parent.parent.parent.children[0])
