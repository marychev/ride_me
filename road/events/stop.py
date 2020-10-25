from conf import SECOND_GAME


class StopEventRoad:
    def __init__(self, road, bike, rock):
        self.road = road
        self.bike = bike
        self.rock = rock

    def start(self, acceleration):
        self.bike.acceleration = acceleration
        stop_way = (acceleration + SECOND_GAME) * 2

        if self.bike.speed - stop_way <= 0:
            self.bike.speed = 0

            self.rock.set_x()

            self.road.set_finish_x()
            return False
        else:
            self.bike.speed -= stop_way

            self.rock.set_x()

            self.road.set_distance_traveled(self.bike)
            self.road.set_finish_x()
            return True
