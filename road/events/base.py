from kivy.event import EventDispatcher
from kivy.properties import ObjectProperty, ListProperty
from utils.state import State


class BaseDispatcher(EventDispatcher):
    road = ObjectProperty(None)

    # todo: set x rock
    # rock = ObjectProperty(None)
    rocks = ListProperty([])

    puddle = ObjectProperty(None)
    lamp = ObjectProperty(None)
    bike = ObjectProperty(None)

    start = ObjectProperty(None)
    finish = ObjectProperty(None)

    def set_distances(self):
        # todo: set x rock
        # self.rock and self.rock.set_x()
        if len(self.rocks) > 0:
            [rock.set_x() for rock in self.rocks]

        self.puddle and self.puddle.set_x()
        self.lamp and self.lamp.set_x()
        self.road.set_distance_traveled()
        self.start and self.start.set_x()
        self.finish and self.finish.set_x()

    def set_game_object(self):
        self.road = self.get_road()
        self.bike = self.get_bike()

        # todo: init rock
        # self.rock = self.get_rock()
        self.rocks = self.get_rocks()

        self.puddle = self.get_puddle()
        self.lamp = self.get_lamp()
        self.start = self.get_start()
        self.finish = self.get_finish()

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

    def get_puddle(self):
        raise NotImplementedError

    def get_lamp(self):
        raise NotImplementedError
