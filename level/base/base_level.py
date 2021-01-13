# from level.base.base_start_level import BaseStartLevel
# from level.base.base_rock_level import BaseRockLevel
# from level.base.base_puddle_level import BasePuddleLevel
# from objects.lamp.lamp import Lamp
# from level.base.base_finish_level import BaseFinishLevel


class LevelGameObjects(
    # BaseStartLevel, BaseFinishLevel,
    # Lamp,
    # #BaseRockLevel, BasePuddleLevel
):
    pass


# class BaseLevel(LevelGameObjects):
class BaseLevel:

    def __init__(self, road, bike, map_json, **kwargs):
        super().__init__(**kwargs)
        self.road = road
        self.bike = bike
        self.map = map_json

        self.add_game_objects()

    def exist_to_map(self, name):
        return name.title() in list(set(el.get('name') for el in self.map))

    def map_objects(self, name):
        return [m for m in self.map if m['name'] == name.title() and int(self.road.distance_traveled) <= int(m['pos'][0])]

    def can_remove_widget(self, widget):
        visible_zone = [w for w in self.road.children if w.__class__.__name__ == 'VisibleZone'][0]
        return not visible_zone.collide_point(widget.x, visible_zone.y)

    def _remove_widget(self, widget):
        if self.can_remove_widget(widget):
            self.road.remove_widget(widget)

    def remove_widgets(self, road_objects):
        if len(road_objects) > 0 and self.road.distance_traveled > 0:
            [self._remove_widget(w) for w in road_objects]

    def add_game_objects(self):
        # self.add_start()
        # self.exist_to_map('rock') and self.add_rocks()
        # self.exist_to_map('puddle') and self.add_puddles()
        # self.exist_to_map('lamp') and self.add_lamps()
        # self.exist_to_map('lamp') and Lamp().add_game_objects()
        # self.add_finish()
        print('ADD OBJECTS')
