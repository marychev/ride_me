from .go import GoEventRoad
from utils.state import State


class LandingEventRoad(GoEventRoad):
    def do(self, dt):
        is_in_sky = self.bike.is_in_sky()

        if is_in_sky:
            self._do(dt)
            self.road.set_state(State.ON_LANDING_MOVE)
        else:
            self.bike.y = self.road.y
            self.bike.power = self.bike.max_power
            self.road.set_state(State.ON_LANDING_STOP)
        return is_in_sky

    def _do(self, dt):
        self.bike.y -= self.set_bike_y(dt) * self.road.gravity
        self.bike.set_power(dt)

    def set_bike_y(self, dt):
        return dt * self.bike.power
