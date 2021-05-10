from typing import List
from kivy.cache import Cache
from kivy.uix.widget import Widget
from level.model import MapModel
from utils.type import TJsonMap
from utils.init import calc_rest_rm
# todo: troubles with import
# from utils.store import CACHE_NAME


class BaseLevel:
    def __init__(self, road, bike, map_json: TJsonMap):
        self.road = road
        self.bike = bike
        self.map = map_json

    @staticmethod
    def total_way(json_map: TJsonMap):
        return json_map[-1]['pos'][0]

    @staticmethod
    def buy(map_model: MapModel) -> bool:
        rest_rm = calc_rest_rm(map_model.price)
        if rest_rm > 0:
            BaseLevel.set_config(map_model, rest_rm)
            return True
        return False

    @staticmethod
    def set_config(map_model: MapModel, rest_rm: int) -> None:
        from utils.store import Store
        store = Store()
        store.remove_cache_rm()
        store.set_rm(rest_rm)
        store.remove_cache_map()
        store.set_cache_map(map_model)

    def exist_to_map(self, name: str) -> bool:
        return name.title() in list(set(el.get('name') for el in self.map))

    def remaining_objects_on_map(self, name: str) -> TJsonMap:
        return [m for m in self.map if m['name'] == name.title()
                and int(self.road.distance_traveled) <= int(m['pos'][0])]

    def visible_map_elem(self) -> TJsonMap:
        return [me for me in self.road.level.map if self.road.visible(me['pos'])]

    def _remove_widget(self, widget: Widget) -> None:
        from utils.store import CACHE_NAME

        if widget.x < 0:
            Cache.remove(CACHE_NAME, widget.sid)
            self.road.remove_widget(widget)

    def remove_widgets(self, road_objects: List[Widget]) -> None:
        if len(road_objects) > 0 and self.road.distance_traveled > 0:
            [self._remove_widget(w) for w in road_objects]
