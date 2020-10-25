class GoEventRoad:
    def __init__(self, road, bike, rock):
        self.road = road
        self.bike = bike
        self.rock = rock

    def start(self, acceleration):
        print('Start GO ROAD')
        self.bike.acceleration = acceleration
        self.bike.speed += acceleration

        self.rock.set_x()

        self.road.set_distance_traveled(self.bike)
        self.road.set_finish_x()
        return True
