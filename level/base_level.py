from kivy.core.window import Window
from road.start import Start
from road.rock import Rock
from utils.validation import ValidObject


class BaseLevel:
    def __init__(self, road, bike, map_json):
        self.road = road
        self.bike = bike
        self.map = map_json

        self.start_distance = Window.width/2
        self.add_start()
        self.add_rock()

    def init_obj(self, name):
        objs = []
        for m in self.map:
            if int(self.road.distance_traveled) <= int(m['pos'][0]) and m['name'] == name.title():
                objs.append(m)
        return objs

    def start(self):
        widgets = [w for w in self.road.children if w.__class__.__name__ == 'Start']
        return ValidObject.start(widgets[0]) if len(widgets) > 0 else None

    def map_start(self):
        objs = []
        for m in self.map:
            if m['name'] == 'Start':
                objs.append(m)
        return objs

    def create_start(self):
        pos = self.map_start()[0]['pos']
        size = (50, (self.road.height / 2) + 10)
        return Start.create(pos, size)

    def add_start(self):
        map_start = self.map_start()[0]
        if (self.bike and self.road) and not self.road.start:
            if not self.start() and self.road.distance_traveled < map_start['pos'][0]:
                start = self.create_start()
                self.road.add_widget(start)

    def remove_start(self):
        map_start = self.map_start()[0]
        if self.road.distance_traveled > map_start['pos'][0] and self.road.start.x < 0:
            self.road.remove_widget(self.road.start)

    # todo: in dev
    # rocks

    def rocks(self):
        widgets = [w for w in self.road.children if w.__class__.__name__ == 'Rock']
        return widgets

    def add_rock(self):
        children = [ch.__class__.__name__ for ch in self.road.children]
        if 'Rock' not in children and (self.bike and self.road): # and self.road.distance_traveled < self.start_distance:
            for rock in self.create_rock():
                self.road.add_widget(rock)

    def create_rock(self):
        objs = self.init_obj('rock')
        line_point = self.road.line_points[-1]

        rocks = []
        for o in objs:
            kwargs = {
                "pos": (o['pos'][0], line_point),
                # "size": self.texture_size
            }
            rocks.append(Rock(**kwargs))
        return rocks

    # todo: refactor
    def remove_rock(self):
        widgets = [w for w in self.road.children if w.__class__.__name__ == 'Rock']
        if self.road.distance_traveled > self.start_distance:
            for w in widgets:
                if w.pos[0] < 0:
                    self.road.remove_widget(w)

    def finish(self):
        pass

