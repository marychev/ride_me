from .go import GoEventRoad
from utils.state import State


class JumpEventRoad(GoEventRoad):

    def do(self, dt):
        can_up = self.bike.power > 0
        if can_up:
            self._do(dt)
            self.road.set_state(State.ON_JUMP_MOVE)
        else:
            self.road.set_state(State.ON_JUMP_STOP)
        return can_up

    def _do(self, dt):
        self.bike.y += self.set_bike_y(dt)
        self.bike.set_power(-dt)

    def set_bike_y(self, dt):
        return dt * self.bike.power
