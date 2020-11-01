from label.status_bar import StatusBar
from utils.state import State


class GoEventRoad:
    def __init__(self, road=None, bike=None, rock=None, finish=None):
        self.road = road or StatusBar.get_road()
        self.bike = bike or StatusBar.get_bike()
        self.rock = rock or StatusBar.get_rock()
        self.finish = finish or StatusBar.get_finish()

    def start(self, dt):
        if self.rock and self.bike.collide_widget(self.rock):
            self.bike.collision_rock()
            self.road.set_state(State.ON_GO_STOP)
            return False
        else:
            self.bike.speed += dt

            self.set_distances()
            self.road.set_state(State.ON_GO_MOVE)
            return True

    def set_distances(self):
        self.rock and self.rock.set_x()
        self.road.set_distance_traveled()
        self.finish.set_x()
