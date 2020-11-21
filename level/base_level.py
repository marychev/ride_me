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

    def create_start(self):
        obj = self.init_obj('start')[0]
        pos = obj['pos']
        size = (50, (self.road.height / 2) + 10)
        return Start.create(pos, size)

    def add_start(self):
        children = [ch.__class__.__name__ for ch in self.road.children]
        if 'Start' not in children and (self.bike and self.road) and self.road.distance_traveled < self.start_distance:
            start = self.create_start()
            self.road.add_widget(start)

    def remove_start(self):
        if self.road.distance_traveled > self.start_distance:
            self.road.remove_widget(self.road.start)

    # rock

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

    """
    # Прямая трасса. 
    # - добавить возможность Инициализации объекта с карты от пройденного расстояния дороги
    # - добавить собирание байком очков для увеличения хар-к, и ... 
    # - Ты можешь установить лучший рекорд на время.
    
    #Start:
    #    id: start
    #    pos: 120 + root.ids.bike.width - 50, root.ids.road.y
    #    size: 50, (root.ids.road.height / 2) + 10
    #    size_hint: None, None

    #Rock:
    #    id: rock
    #    pos: 800, root.ids.road.line_points[-1]
    #    size: self.texture_size
    #Puddle:
    #    id: puddle
    #    pos: 1000, root.ids.road.line_points[-1] - self.height/2
    #    size: self.texture_size
    #Lamp:
    #    id: lamp
    #    pos: 1500, root.ids.road.line_points[-1]
    #    size: self.texture_size

    #Finish:
    #    id: finish
    #    pos: root.ids.road.total_way, root.ids.tools.height
    #    size: 120, (root.ids.road.height / 2) + 10
    #    size_hint: None, None
    """
