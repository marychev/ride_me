from level.base.base_start_level import BaseStartLevel
from level.base.base_rock_level import BaseRockLevel
from level.base.base_puddle_level import BasePuddleLevel
from level.base.base_lamp_level import BaseLampLevel
from level.base.base_finish_level import BaseFinishLevel


class LevelGameObjects(BaseStartLevel, BaseFinishLevel, BaseRockLevel, BasePuddleLevel, BaseLampLevel):
    pass


class BaseLevel(LevelGameObjects):

    def __init__(self, road, bike, map_json):
        self.road = road
        self.bike = bike
        self.map = map_json

        self.add_game_objects()

    def init_objects(self, name):
        return [m for m in self.map
                if int(self.road.distance_traveled) <= int(m['pos'][0]) and m['name'] == name.title()]

    def map_objects(self, name):
        return [m for m in self.map if m['name'] == name.title()]

    def add_game_objects(self):
        self.add_start()
        self.add_rock()
        self.add_puddle()
        self.add_lamp()
        self.add_finish()
