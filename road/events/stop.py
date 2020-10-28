from conf import SECOND_GAME
from .go import GoEventRoad


class StopEventRoad(GoEventRoad):

    def start(self, acceleration):
        if self.bike.has_collision_rock():
            self.bike.collision_rock()
            return False
        else:

            self.bike.acceleration = acceleration
            stop_way = (acceleration + SECOND_GAME) * 2

            if self.bike.speed - stop_way <= 0:
                self.bike.speed = 0

                self.rock.set_x()
                self.finish.set_x()
                return False
            else:
                self.bike.speed -= stop_way
                self.set_distances()
                return True
