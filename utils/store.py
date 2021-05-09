from typing import Optional
from kivy.cache import Cache
from kivy.logger import Logger

from bike.bikes import get_by_title as get_bike_by_title
from bike.model import BikeModel
from level.model import MapModel

CACHE_NAME = 'installed'


class Store:
    installed_table = CACHE_NAME
    bike_table = 'bike'
    map_table = 'map'

    def register_all_table(self):
        Cache.register(self.bike_table)
        Cache.register(self.map_table)
        Cache.register(self.installed_table, limit=10000)

    def add_cache_bike(self, bike_title: Optional[str], model: BikeModel = None) -> BikeModel:
        model = get_bike_by_title(bike_title) if model is None else model

        if not model:
            raise Exception("Bike was not registered to Cache since it does not exist to JSON data")

        self.set_cache_bike(model)
        Logger.info(f"Cache: The {bike_title} bike was added to Cache!")
        return model

    def reset_cache_bike(self) -> BikeModel:
        model = BikeModel.create_empty()
        self.set_cache_bike(model)

        Logger.info("Cache: Bike was reset for Cache!")
        return model

    def add_cache_map(self, title: Optional[str], model: MapModel = None) -> MapModel:
        from level.maps import get_by_title as get_map_by_title

        model = get_map_by_title(title) if model is None else model

        if not model:
            raise Exception("Map was not registered to Cache since it does not exist to JSON data")

        self.set_cache_map(model)
        Logger.info(f"Cache: The {title} map was installed to Cache!")
        return model

    def reset_cache_map(self) -> MapModel:
        model = MapModel.create_empty()
        self.set_cache_map(model)

        Logger.info("Cache: Map was reset for Cache!")
        return model

    def set_cache_bike(self, model: BikeModel):
        Cache.append(self.bike_table, 'title', model.title)
        Cache.append(self.bike_table, 'power', model.power)
        Cache.append(self.bike_table, 'speed', model.speed)
        Cache.append(self.bike_table, 'acceleration', model.acceleration)
        Cache.append(self.bike_table, 'agility', model.agility)

    def remove_cache_bike(self) -> None:
        Cache.remove(self.bike_table, 'title')
        Cache.remove(self.bike_table, 'power')
        Cache.remove(self.bike_table, 'speed')
        Cache.remove(self.bike_table, 'acceleration')
        Cache.remove(self.bike_table, 'agility')

    def set_cache_map(self, model: MapModel):
        Cache.append(self.map_table, 'title', model.title)
        Cache.append(self.map_table, 'level', model.level)
        Cache.append(self.map_table, 'map', model.map)
        Cache.append(self.map_table, 'total_way', model.total_way)

    def remove_cache_map(self):
        Cache.remove(self.map_table, 'title')
        Cache.remove(self.map_table, 'level')
        Cache.remove(self.map_table, 'map')
        Cache.remove(self.map_table, 'total_way')

    def set_rm(self, value: int):
        Cache.append(self.bike_table, 'rm', value)

    def remove_cache_rm(self):
        Cache.remove(self.bike_table, 'rm')

    # def get_installed_cache(self, sid: str) -> Optional[str, int, float]:
    def get_installed_cache(self, sid):
        return Cache.get(self.installed_table, sid)
