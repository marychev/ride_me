from kivy.event import EventDispatcher
from kivy.properties import ObjectProperty, ListProperty
from utils.state import State


class BaseDispatcher(EventDispatcher):
    road = ObjectProperty(None)
    bike = ObjectProperty(None)
    start = ObjectProperty(None)
    finish = ObjectProperty(None)
    rocks = ListProperty([])
    puddles = ListProperty([])
    lamps = ListProperty([])

    def set_distances(self):
        if len(self.rocks) > 0:
            [rock.set_x() for rock in self.rocks]
        if len(self.puddles) > 0:
            [puddle.set_x() for puddle in self.puddles]
        if len(self.lamps) > 0:
            [lamp.set_x() for lamp in self.lamps]

        self.road.set_distance_traveled()
        self.start and self.start.set_x()
        self.finish and self.finish.set_x()

    def set_game_object(self):
        self.road = self.get_road()
        self.bike = self.get_bike()
        self.start = self.get_start()
        self.finish = self.get_finish()
        self.rocks = self.get_rocks()
        self.puddles = self.get_puddles()
        self.lamps = self.get_lamps()

    def road_finish(self):
        self.bike.power = 0
        self.bike.speed = 0
        self.bike.acceleration = 0

        self.road.set_state(State.FINISH)
        self.road.unschedule_events()

    def get_road(self):
        raise NotImplementedError

    def get_bike(self):
        raise NotImplementedError

    def get_start(self):
        raise NotImplementedError

    def get_finish(self):
        raise NotImplementedError

    def get_rocks(self):
        raise NotImplementedError

    def get_puddles(self):
        raise NotImplementedError

    def get_lamps(self):
        raise NotImplementedError
