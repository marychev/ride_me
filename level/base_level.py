from kivy.core.window import Window
from road.start import Start
from road.rock import Rock


LINE_REMOVE = Window.width / 2


class BaseLevel:
    def __init__(self, road, bike, map_json):
        self.road = road
        self.bike = bike
        self.map = map_json

        self.add_start()
        self.add_rock()

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

    # todo: in dev
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

    def finish(self):
        pass

