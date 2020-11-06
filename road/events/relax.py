from kivy.clock import Clock
from utils.state import State
from conf import SECOND_GAME
from .go import GoDispatcher
from utils.state import State


class RelaxEventRoad(GoDispatcher):

    def do(self, dt):
        if self.rock and self.bike.collide_widget(self.rock):
            self.bike.collision_rock()
            self.road.set_state(State.ON_RELAX_STOP)
            return False
        elif self.road.has_finished():
            self.bike.speed = 0
            self.bike.power = 0
            self.bike.acceleration = 0
            self.road.set_state(State.FINISH)
            return False
        elif self.bike.speed - dt <= 0:
            self.bike.speed = 0
            self.rock and self.rock.set_x()
            self.finish.set_x()
            self.road.set_state(State.ON_WAIT_START)
            return False
        else:
            self.bike.speed -= dt/2
            self.bike.power += dt
            self.set_distances()
            self.road.set_state(State.ON_RELAX_MOVE)
            return True
