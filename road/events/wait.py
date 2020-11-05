from .go import GoEventRoad
from utils.state import State


class WaitEventRoad(GoEventRoad):
    def do(self, dt):
        can = self.bike.speed <= 0 and self.bike.power < self.bike.max_power
        if can:
            self.bike.speed = 0
            self.bike.power += dt*10
            self.road.set_state(State.ON_WAIT_MOVE)
        else:
            self.road.set_state(State.ON_WAIT_STOP)
        return can

