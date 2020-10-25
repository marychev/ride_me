class RelaxEventRoad:
    def __init__(self, road, bike, rock):
        self.road = road
        self.bike = bike
        self.rock = rock

    def start(self, acceleration):
        self.bike.acceleration = acceleration

        if self.bike.speed - acceleration <= 0:
            self.bike.speed = 0

            self.rock.set_x()

            self.road.set_finish_x()
            return False
        else:
            self.bike.speed -= acceleration

            self.rock.set_x()

            self.road.set_distance_traveled(self.bike)
            self.road.set_finish_x()
            return True
