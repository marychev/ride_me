from kivy.clock import Clock
from utils.state import State
from conf import SECOND_GAME
from .go import GoEventRoad
from utils.state import State


class RelaxEventRoad(GoEventRoad):

    def do(self, dt):
        if self.rock and self.bike.collide_widget(self.rock):
            self.bike.collision_rock()
            self.road.set_state(State.ON_RELAX_STOP)
            return False
        elif self.road.has_finished():
            self.bike.speed = 0
            self.bike.power = 0
            self.bike.acceleration = 0
            self.road.set_state(State.FINISHED)
            return False
        elif self.bike.speed - dt <= 0:
            self.bike.speed = 0
            self.rock and self.rock.set_x()
            self.finish.set_x()
            self.road.set_state(State.NONE)
            return False
        else:
            self.bike.speed -= dt/10
            self.set_distances()
            self.road.set_state(State.ON_RELAX_MOVE)
            return True
