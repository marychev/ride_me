from kivy.event import EventDispatcher
from kivy.properties import ObjectProperty
from utils.state import State

from label.status_bar import StatusBar


class BaseDispatcher(EventDispatcher):
    status_bar = ObjectProperty(None)
    road = ObjectProperty(None)
    rock = ObjectProperty(None)
    bike = ObjectProperty(None)
    finish = ObjectProperty(None)

    def set_distances(self):
        self.rock and self.rock.set_x()
        self.road.set_distance_traveled()
        self.finish and self.finish.set_x()

    def set_game_object(self):
        # todo: only as temp solution
        self.status_bar = self.get_status_bar()
        self.road = self.get_road() or StatusBar.get_road()
        self.rock = self.get_rock() or StatusBar.get_rock()
        self.bike = self.get_bike() or StatusBar.get_bike()
        self.finish = self.get_finish() or StatusBar.get_finish()

    def road_finish(self):
        self.bike.power = 0
        self.bike.speed = 0
        self.bike.acceleration = 0

        self.road.set_state(State.FINISH)
        self.road.unschedule_events()
        self.status_bar and self.status_bar.show_status_finished()