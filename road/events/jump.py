from .go import GoEventRoad
from label.status_bar import StatusBar
from utils.state import State


class JumpEventRoad(GoEventRoad):

    def __init__(self, road, bike, rock, finish):
        super(JumpEventRoad, self).__init__(road, bike, rock, finish)

    def up(self, dt):
        print('up')
        can_up = self.bike.power > 0 and (State.ON_JUMP_LANDING != self.road.state)
        if can_up:
            self._do_up(dt)
            self.road.set_state(State.ON_JUMP_UP_MOVE)
        else:
            self.road.set_state(State.ON_JUMP_UP_STOP)
        return can_up

    def landing(self, dt):
        print('landing', self.road.state, self.road.last_states)
        is_in_sky = self.bike.is_in_sky()
        status_bar = StatusBar.get_status_bar()
        if is_in_sky:
            self._do_down(dt)
            self.road.set_state(State.ON_JUMP_LANDING)
            status_bar.show_status('. . . . on landing', self.bike, self.road)
        else:
            self.bike.y = self.road.y
            self.bike.power = self.bike.max_power
            self.road.set_state(State.ON_JUMP_LANDING_STOP)
            status_bar.show_status('. . . STOP on landing', self.bike, self.road)
        return is_in_sky

    def _do_up(self, dt):
        self.bike.y += self.set_bike_y(dt)
        self.bike.set_power(-dt)

    def _do_down(self, dt):
        self.bike.y -= self.set_bike_y(dt) * self.road.gravity
        self.bike.set_power(dt)

    def set_bike_y(self, dt):
        return dt * self.bike.power

