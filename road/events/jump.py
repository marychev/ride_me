from .go import GoEventRoad
from utils.state import State


class JumpEventRoad(GoEventRoad):

    def __init__(self, road, bike, rock, finish):
        super(JumpEventRoad, self).__init__(road, bike, rock, finish)

    def up(self, dt):
        can_up = self.bike.power > 0 and (State.ON_JUMP_LANDING != self.road.state)
        if can_up:
            self._do_up(dt)
            self.road.set_state(State.ON_JUMP_UP_MOVE)
        else:
            self.road.set_state(State.ON_JUMP_UP_STOP)
        return can_up

    def landing(self, dt):
        is_in_sky = self.bike.is_in_sky()

        if is_in_sky:
            self._do_down(dt)
            self.road.set_state(State.ON_JUMP_LANDING)
        else:
            self.bike.y = self.road.y
            self.bike.power = self.bike.max_power
            self.road.set_state(State.ON_JUMP_LANDING_STOP)
        return is_in_sky

    def _do_up(self, dt):
        self.bike.y += self.set_bike_y(dt)
        self.bike.set_power(-dt)

    def _do_down(self, dt):
        self.bike.y -= self.set_bike_y(dt) * self.road.gravity
        self.bike.set_power(dt)

    def set_bike_y(self, dt):
        return dt * self.bike.power

