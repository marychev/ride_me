from label.status_bar import StatusBar


class GoEventRoad:
    def __init__(self, road=None, bike=None, rock=None):
        self.road = road or StatusBar.get_road()
        self.bike = bike or StatusBar.get_bike()
        self.rock = rock or StatusBar.get_rock()
        self.finish = StatusBar.get_finish()

    def start(self, acceleration):
        print('Start GO ROAD')
        if self.bike.has_collision_rock():
            self.bike.collision_rock()
            return False
        else:
            self.bike.acceleration = acceleration
            self.bike.speed += acceleration
            self.set_distances()
            return True

    def set_distances(self):
        self.rock.set_x()
        self.road.set_distance_traveled(self.bike)
        self.finish.set_x()
