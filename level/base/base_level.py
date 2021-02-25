from kivy.cache import Cache
from layout.scene import CACHE_NAME
from kivy.app import App
from utils.init import app_config


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
        app = App.get_running_app()
        res_rm = int(app_config('bike', 'rm')) - int(map['price'])
        if res_rm > 0:
            app.config.set('map', 'name', map['title'])
            app.config.set('map', 'level', map['level'])
            app.config.set('map', 'map', map['map'])
            app.config.set('map', 'total_way', map['total_way'])
            app.config.set('bike', 'rm', res_rm)
            return True
        return False
