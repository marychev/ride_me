class RelaxEventRoad:
    def __init__(self, road, bike):
        self.road = road
        self.bike = bike

    def start(self, acceleration):
        self.bike.acceleration = acceleration
        if self.bike.speed - acceleration <= 0:
            self.bike.speed = 0
            self.road.set_finish_x()
            return False
        else:
            self.bike.speed -= acceleration
            self.road.set_distance_traveled(self.bike)
            self.road.set_finish_x()
            return True
