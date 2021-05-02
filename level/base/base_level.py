from typing import List, Dict, Union

from kivy.cache import Cache
from kivy.uix.widget import Widget

from layout.scene import CACHE_NAME
from level.model import MapModel
from utils.init import app_config, calc_rest_rm


class BaseLevel:

    def __init__(self, road, bike, map_json: List[Dict[str, str]]):
        self.road = road
        self.bike = bike
        self.map = map_json

    def exist_to_map(self, name: str) -> bool:
        return name.title() in list(set(el.get('name') for el in self.map))

    def map_objects(self, name: str) -> List[Dict[str, str]]:
        return [m for m in self.map if m['name'] == name.title()
                and int(self.road.distance_traveled) <= int(m['pos'][0])]

    def visible_map_elem(self) -> List[Dict[str, str]]:
        return [me for me in self.road.level.map if self.road.visible(me['pos'])]

    def _remove_widget(self, widget: Widget):
        if widget.x < 0:
            Cache.remove(CACHE_NAME, widget.sid)
            self.road.remove_widget(widget)

    def remove_widgets(self, road_objects: List[Widget]):
        if len(road_objects) > 0 and self.road.distance_traveled > 0:
            [self._remove_widget(w) for w in road_objects]

    @staticmethod
    def total_way(json_map: List[Dict[str, str]]):
        return json_map[-1]['pos'][0]

    @staticmethod
    def buy(map_model: MapModel) -> bool:
        rest_rm = calc_rest_rm(map_model.price)
        if rest_rm > 0:
            BaseLevel.set_config(map_model, rest_rm)
            return True
        return False

    @staticmethod
    def set_config(map_model: MapModel, rest_rm: int):
        Cache.remove('bike', 'rm')
        Cache.append('bike', 'rm', rest_rm)

        Cache.remove('map', 'title')
        Cache.remove('map', 'level')
        Cache.remove('map', 'map')
        Cache.remove('map', 'total_way')
        Cache.append('map', 'title', map_model.title)
        Cache.append('map', 'level', map_model.level)
        Cache.append('map', 'map', map_model.map)
        Cache.append('map', 'total_way', map_model.total_way)
