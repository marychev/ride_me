from .go import GoEventRoad


class JumpEventRoad(GoEventRoad):

    def __init__(self, road, bike, rock, finish):
        super(JumpEventRoad, self).__init__(road, bike, rock, finish)
        self.max_jump = 220

    def up(self, dt):
        can_up = self.bike.y < self.max_jump
        if self.bike.y < self.max_jump:
            self._do_up(dt)
        return can_up

    def landing(self, dt):
        is_in_sky = self.bike.is_in_sky()
        if is_in_sky:
            self._do_down(dt)
        else:
            self.bike.y = self.road.height
        return is_in_sky

    def _do_up(self, dt):
        self.bike.y += self.calculate_power(dt)
        self.bike.power -= self.calculate_power(dt)

    def _do_down(self, dt):
        self.bike.y -= self.calculate_power(dt)
        self.bike.power += self.calculate_power(dt)

    def calculate_power(self, dt):
        return dt * self.bike.power

