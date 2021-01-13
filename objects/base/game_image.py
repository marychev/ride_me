from kivy.core.window import Window
from kivy.uix.widget import Widget
from utils.texture import redraw_texture
from utils.get_object import GetObject


class GameImage(Widget):

    @classmethod
    def create(cls, pos, size=None):
        print('CREATE: {} pos: {}'.format(cls, pos))
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
        road = self.get_road()
        if road and (self.x > 0) and road and (road.distance_traveled + Window.width) >= self.x:
            self.x = self.get_x()
            redraw_texture(self)

    def level_map_objects(self, name):
        road = self.get_road()
        return road and road.level.map_objects(name)[:]

    # general elements and functions

    def get_road(self):
        _road = self.parent and self.parent.parent.children[1]
        return GetObject(road=_road).road

    def get_bike(self):
        return GetObject(road=self.get_road()).bike

    def get_tools(self):
        return GetObject(road=self.get_road()).tools
