from kivy.clock import Clock
from label.status_bar import StatusBar
from utils.state import State
from conf import SECOND_GAME


class GoEventRoad:
    def __init__(self, status_bar=None, road=None, bike=None, rock=None, finish=None):
        self.set_game_objects(status_bar, road, bike, rock, finish)

    def do(self, dt):
        if self.rock and self.bike.collide_widget(self.rock):
            self.bike.collision_rock()
            self.road.set_state(State.ON_GO_STOP)
            return False
        elif self.road.has_finished():
            self.status_bar.show_status_finished()
        else:
            self.bike.speed += dt

            self.set_distances()
            self.road.set_state(State.ON_GO_MOVE)
            self.status_bar.show_status('On Go: ' + self.road.state, self.bike, self.road)
            return True

    def set_distances(self):
        self.rock and self.rock.set_x()
        self.road.set_distance_traveled()
        self.finish.set_x()

    def set_game_objects(self, status_bar, road, bike, rock, finish):
        self.status_bar = status_bar
        self.road = road
        self.bike = bike
        self.rock = rock
        self.finish = finish
