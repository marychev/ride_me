from conf import SECOND_GAME
from .go import GoEventRoad
from utils.state import State


class StopEventRoad(GoEventRoad):

    def start(self, acceleration):
        if self.bike.collide_widget(self.rock):
            self.bike.collision_rock()
            self.road.set_state(State.ON_STOP_STOP)
            return False
        else:

            self.bike.acceleration = acceleration
            stop_way = (acceleration + SECOND_GAME) * 2

            if self.bike.speed - stop_way <= 0:
                self.bike.speed = 0

                self.rock.set_x()
                self.finish.set_x()
                self.road.set_state(State.ON_STOP_STOP)
                return False
            else:
                self.bike.speed -= stop_way
                self.set_distances()
                self.road.set_state(State.ON_STOP_MOVE)
                return True
