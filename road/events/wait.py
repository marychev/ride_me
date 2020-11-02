from .go import GoEventRoad
from utils.state import State


class WaitEventRoad(GoEventRoad):
    def wait(self, dt):
        can = self.bike.speed <= 0
        if can:
            self.bike.speed = 0
            self.road.set_state(State.NONE)
        else:
            self.road.set_state(State.NONE)
        return can

