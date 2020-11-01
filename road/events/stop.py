from utils.state import State
from .go import GoEventRoad


class StopEventRoad(GoEventRoad):

    def start(self, dt):
        if self.rock and self.bike.collide_widget(self.rock):
            self.bike.collision_rock()
            self.road.set_state(State.ON_STOP_STOP)
            return False
        else:
            stop_way = dt*2
            if self.bike.speed - stop_way <= 0:
                self.bike.speed = 0

                self.rock and self.rock.set_x()
                self.finish.set_x()
                self.road.set_state(State.ON_STOP_STOP)
                return False
            else:
                self.bike.speed -= stop_way
                self.set_distances()
                self.road.set_state(State.ON_STOP_MOVE)
                return True
