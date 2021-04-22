from kivy.cache import Cache
from layout.scene import CACHE_NAME
from utils.init import app_config, calc_rest_rm


class BaseLevel:

    def __init__(self, road, bike, map_json):
        self.road = road
        self.bike = bike
        self.map = map_json

    def exist_to_map(self, name):
        return name.title() in list(set(el.get('name') for el in self.map))

    def map_objects(self, name):
        return [m for m in self.map if m['name'] == name.title() and int(self.road.distance_traveled) <= int(m['pos'][0])]

    def visible_map_elem(self):
        return [me for me in self.road.level.map if self.road.visible(me['pos'])]

    def _remove_widget(self, widget):
        if widget.x < 0:
            Cache.remove(CACHE_NAME, widget.sid)
            self.road.remove_widget(widget)

    def remove_widgets(self, road_objects):
        if len(road_objects) > 0 and self.road.distance_traveled > 0:
            [self._remove_widget(w) for w in road_objects]

    @staticmethod
    def total_way(map):
        return map[-1]['pos'][0]

    @staticmethod
    def buy(map):
        rest_rm = calc_rest_rm(map['price'])
        if rest_rm > 0:
            BaseLevel.set_config(map, rest_rm)
            return True
        return False

    @staticmethod
    def set_config(item, rest_rm):
        Cache.remove('bike', 'rm')
        Cache.append('bike', 'rm', rest_rm)

        Cache.remove('map', 'title')
        Cache.remove('map', 'level')
        Cache.remove('map', 'map')
        Cache.remove('map', 'total_way')
        Cache.append('map', 'title', item['title'])
        Cache.append('map', 'level', item['level'])
        Cache.append('map', 'map', item['map'])
        Cache.append('map', 'total_way', item['total_way'])

