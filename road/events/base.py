from kivy.event import EventDispatcher
from kivy.properties import ObjectProperty

from label.status_bar import StatusBar


class BaseDispatcher(EventDispatcher):
    status_bar = ObjectProperty(None)
    road = ObjectProperty(None)
    rock = ObjectProperty(None)
    bike = ObjectProperty(None)
    finish = ObjectProperty(None)

    def set_game_object(self):
        # todo: only as temp solution
        self.status_bar = self.get_status_bar()
        self.road = self.get_road() or StatusBar.get_road()
        self.rock = self.get_rock() or StatusBar.get_rock()
        self.bike = self.get_bike() or StatusBar.get_bike()
