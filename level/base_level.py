from road.start import Start
from road.finish import Finish
from road.rock import Rock


class BaseLevel:
    def __init__(self, road, bike, map_json):
        self.road = road
        self.bike = bike
        self.map = map_json

        self.add_start()
        self.add_rock()
        self.add_finish()

    def init_objects(self, name):
        return [m for m in self.map
                if int(self.road.distance_traveled) <= int(m['pos'][0]) and m['name'] == name.title()]

    def map_objects(self, name):
        return [m for m in self.map if m['name'] == name.title()]

    # start on level

    def start(self):
        starts = Start.widgets_on_road(self.road)
        return starts[0] if len(starts) > 0 else None

    def create_start(self):
        pos = self.map_objects('start')[0]['pos']
        size = (50, (self.road.height / 2) + 10)
        return Start.create(pos, size)

    def add_start(self):
        if (self.bike and self.road) and not self.road.start:
            map_start = self.map_objects('start')[0]

            if self.road.distance_traveled < map_start['pos'][0]:
                start = self.create_start()
                self.road.start = start
                self.road.add_widget(start)

    def remove_start(self):
        map_start = self.map_objects('start')[0]
        if self.road.distance_traveled > map_start['pos'][0] and self.road.start.x < 0:
            self.road.remove_widget(self.road.start)

    # rocks

    def rocks(self):
        return Rock.widgets_on_road(self.road)

    def create_rocks(self):
        rocks = [Rock.create(pos=(o['pos'][0], self.road.line_points[-1])) for o in self.init_objects('rock')]
        return rocks

    def add_rock(self):
        if len(Rock.widgets_on_road(self.road)) == 0 and (self.bike and self.road):
            [self.road.add_widget(rock) for rock in self.create_rocks()]

    def remove_rock(self):
        rocks = Rock.widgets_on_road(self.road)
        if len(rocks) > 0:
            [self.road.remove_widget(w) for w in rocks if w.pos[0] < 0]

    # todo: in dev
    # finish

    def finish(self):
        finishes = Finish.widgets_on_road(self.road)
        return finishes[0] if len(finishes) > 0 else None

    def create_finish(self):
        pos = self.map_objects('finish')[0]['pos']
        size = (120, (self.road.height / 2) + 10)
        return Finish.create(pos, size)

    def add_finish(self):
        if (self.bike and self.road) and not self.road.finish:
            map_finish = self.map_objects('finish')[0]

            if self.road.distance_traveled < map_finish['pos'][0]:
                finish = self.create_finish()
                self.road.total_way = finish.pos[0]
                self.road.finish = finish
                self.road.add_widget(finish)
