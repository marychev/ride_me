from .go import GoEventRoad
from utils.state import State


class RelaxEventRoad(GoEventRoad):

    def start(self, acceleration):
        if self.rock and self.bike.collide_widget(self.rock):
            self.bike.collision_rock()
            self.road.set_state(State.ON_RELAX_STOP)
            return False
        else:
            self.bike.acceleration = acceleration

            if self.bike.speed - acceleration <= 0:
                self.bike.speed = 0
                self.rock and self.rock.set_x()
                self.finish.set_x()
                self.road.set_state(State.ON_RELAX_STOP)
                return False
            else:
                self.bike.speed -= acceleration
                self.set_distances()
                self.road.set_state(State.ON_RELAX_MOVE)
                return True
