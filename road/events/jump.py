from .go import GoEventRoad


class JumpEventRoad(GoEventRoad):

    def __init__(self, road, bike, rock, finish):
        super(JumpEventRoad, self).__init__(road, bike, rock, finish)
        self.max_jump = 200

    def up(self, acceleration):
        if self.bike.y < self.max_jump:
            self.bike.y += acceleration * self.bike.power
            self.bike.power -= acceleration * self.bike.power
            return True

    def landing(self, acceleration):
        is_in_sky = self.bike.is_in_sky()
        if is_in_sky:
            self.bike.y -= acceleration * self.bike.power
            self.bike.power += acceleration * self.bike.power
        else:
            self.bike.y = self.road.height
        return is_in_sky
