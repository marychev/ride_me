class GoEventRoad:
    def __init__(self, road, bike):
        self.road = road
        self.bike = bike

    def start(self, acceleration):
        self.bike.acceleration = acceleration
        self.bike.speed += acceleration

        self.road.set_distance_traveled(self.bike)
        self.road.set_finish_x()
        return True
