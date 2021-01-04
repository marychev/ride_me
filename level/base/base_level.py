from kivy.core.window import Window
from level.base.base_start_level import BaseStartLevel
from level.base.base_rock_level import BaseRockLevel
from level.base.base_puddle_level import BasePuddleLevel
from level.base.base_lamp_level import BaseLampLevel
from level.base.base_finish_level import BaseFinishLevel


class LevelGameObjects(BaseStartLevel, BaseFinishLevel,
                       BaseLampLevel, BaseRockLevel, BasePuddleLevel):
    pass


class BaseLevel(LevelGameObjects):

    def __init__(self, road, bike, map_json):
        self.road = road
        self.bike = bike
        self.map = map_json
        self.add_game_objects()

    def exist_to_map(self, name):
        return name.title() in list(set(el.get('name') for el in self.map))

    def init_objects(self, name):

        if self.exist_to_map(name):
            objs = [
                m for m in self.map_objects(name)
                if 0 < int(self.road.distance_traveled + Window.width) - int(m['pos'][0]) <= int(Window.width)]
            print('INIT OBJECTS: ', name, objs)
            print(self.road.distance_traveled)
            print(self.road.lamps)
            print(self.road.children)
            print('------'*10)
            return objs

    def new_map_objects(self, road_objects, map_objects):
        new_objects = []
        if len(road_objects) == 0:
            new_objects = map_objects
        elif len(map_objects) > 0:
            for ro in road_objects:
                new_objects = [mo for mo in map_objects if ro.pos[0] != mo['pos'][0]]
        return new_objects

    def map_objects(self, name):
        return [m for m in self.map if
                m['name'] == name.title() and int(self.road.distance_traveled) <= int(m['pos'][0])]

    def can_remove_widget(self, widget):
        return self.road.distance_traveled > widget.pos[0] or widget.pos[0] < 0

    def remove_widget(self, widget):
        if self.can_remove_widget(widget):
            self.road.remove_widget(widget)
            print('x x x remove_widget x x x', widget.pos, self.road.distance_traveled)

    def remove_widgets(self, road_objects):
        print()
        if len(road_objects) > 0:
            # [self.road.remove_widget(w) for w in road_objects if w.pos[0] < 0]
            if self.can_remove_widget(road_objects[0]):
                print(' . . road_objects BEFORE: ', road_objects)
                [self.remove_widget(w) for w in road_objects]
                print(' . . self.lamps: AFTER', self.lamps())

    def add_game_objects(self):
        self.add_start()
        self.exist_to_map('rock') and self.add_rocks()
        self.exist_to_map('puddle') and self.add_puddles()
        self.exist_to_map('lamp') and self.add_lamps()
        self.add_finish()
