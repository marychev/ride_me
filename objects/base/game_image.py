from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.uix.widget import Widget
from utils.texture import redraw_texture
from utils.get_object import GetObject
from utils.sizes import BASE_WIDTH_BTN


class GameImage(Widget):
    sid = StringProperty('')

    def __str__(self):
        return self.sid

    @classmethod
    def init_sid(cls, pos):
        return f'{cls.__name__.lower()}_{pos[0]}_{pos[1]}'

    @classmethod
    def create(cls, sid, pos, size=None):
        # print('CREATE: {} pos: {}'.format(cls, pos))
        # size = size if size else cls.TEXTURE.size
        size = size if size else (BASE_WIDTH_BTN, BASE_WIDTH_BTN)
        kwargs = {
            "sid": sid,
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
        # if road and (road.distance_traveled + Window.width) >= self.x and (self.x+self.width/1.4 > 0):
        if road and (road.distance_traveled + Window.width) >= self.x and (self.x+self.width > 0):
            self.x = self.get_x()
            redraw_texture(self)

    def level_map_objects(self, name):
        road = self.get_road()
        return road and road.level.map_objects(name)[:]

    # general elements and functions

    def get_road(self):
        _road = self.parent and GetObject.get_child(self.parent.parent, 'Road')
        return GetObject(road=_road).road

    def get_bike(self):
        return GetObject(road=self.get_road()).bike

    def get_tools(self):
        return GetObject(road=self.get_road()).tools
