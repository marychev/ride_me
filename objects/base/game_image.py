from typing import Tuple, Dict, Any
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.uix.widget import Widget

from objects.model import GOModel
from utils.exception import ExceptionPosObjectMoreRoad
from utils.sizes import ROAD_BIKE_POINT_Y, BIKE_HEIGHT, ROAD_BIKE_LINE_Y
from utils.type import TPos, TPosN
from utils.get_object import GetObject
from utils.texture import redraw_texture


class GameImage(Widget):
    sid = StringProperty('')

    def __str__(self):
        return self.sid

    @classmethod
    def to_map(cls, x: TPosN, y: TPosN = ROAD_BIKE_LINE_Y) -> Dict[str, TPos]:
        pos = cls.init_pos(x, y)
        return {"name": cls.__name__, "pos": pos}

    @classmethod
    def init_pos(cls, x: TPosN, y: TPosN) -> TPos:
        max_y = ROAD_BIKE_POINT_Y + BIKE_HEIGHT
        if y >= max_y or y < ROAD_BIKE_POINT_Y:
            ExceptionPosObjectMoreRoad()
        return x, y

    @classmethod
    def init_sid(cls, pos: Tuple) -> str:
        """It must have unique returned values all time"""
        return f'{cls.__name__.lower()}_{pos[0]}_{pos[1]}'

    @classmethod
    def create(cls, sid: str, pos: TPos, size: Tuple) -> Widget:
        # print('CREATE: {} pos: {}'.format(cls, pos))
        go_model = GOModel(sid=sid, pos=pos, size=size, size_hint=(None, None))
        return cls(**go_model._asdict())

    def get_x(self) -> TPosN:
        bike = self.get_bike()
        return self.x - bike.speed if bike else self.x

    def set_x(self) -> None:
        road = self.get_road()
        if road and (road.distance_traveled + Window.width) >= self.x and (self.x+self.width > 0):
            self.x = self.get_x()
            redraw_texture(self)

    # general elements and functions

    def get_road(self) -> Widget:
        _road = self.parent and GetObject.get_child(self.parent.parent, 'Road')
        return GetObject(road=_road).road

    def get_bike(self) -> Widget:
        return GetObject(road=self.get_road()).bike

    def get_tools(self) -> Widget:
        return GetObject(road=self.get_road()).tools
