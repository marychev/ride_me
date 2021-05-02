from typing import Union, Optional
from kivy.cache import Cache
from kivy.lang import Builder
# from kivy.logger import Logger
from kivy.properties import NumericProperty, StringProperty
from kivy.uix.widget import Widget

from bike.animation import AnimationBike
from bike.bikes import get_by_title as get_by_bike_title
from bike.model import BikeModel
from utils.dir import abstract_path
from utils.get_object import GetObject
from utils.init import app_config, calc_rest_rm
from utils.validation import ValidObject
from utils.exception import WarnBikeIsNotConfig

Builder.load_file(abstract_path('bike/bike.kv'))


class Bike(AnimationBike):
    source = StringProperty(abstract_path('bike/img/default.png'))
    acceleration = NumericProperty(0.0)
    power = NumericProperty(0)
    max_power = NumericProperty(0)
    speed = NumericProperty(0)
    max_speed = NumericProperty(0)
    agility = NumericProperty(0)

    start_dt = NumericProperty(0)
    finish_dt = NumericProperty(0)

    collected_currency = NumericProperty(0)
    currency = NumericProperty(0)

    def __init__(self, **kwargs):
        super(Bike, self).__init__(**kwargs)
        self.init_app_config()

    def init_params(self, bike_model: BikeModel) -> None:
        self.source = bike_model.source
        self.max_power = bike_model.power
        self.max_speed = bike_model.speed
        self.acceleration = bike_model.acceleration
        self.agility = bike_model.agility

        self.init_source_animation(bike_model)

    def init_app_config(self) -> None:
        bike_title = app_config('bike', 'title')

        if bike_title:
            bike_model = get_by_bike_title(bike_title)
            self.init_params(bike_model)
        else:
            WarnBikeIsNotConfig(bike_title, self)

    @staticmethod
    def buy(bike_model: BikeModel) -> bool:
        res_rm = calc_rest_rm(bike_model.price)
        if res_rm > 0:
            Bike.set_config(bike_model, res_rm)
            return True
        return False

    @staticmethod
    def set_config(bike_model, rest_rm) -> None:
        Cache.remove('bike', 'rm')
        Cache.append('bike', 'rm', rest_rm)

        Cache.remove('bike', 'title')
        Cache.remove('bike', 'power')
        Cache.remove('bike', 'speed')
        Cache.remove('bike', 'acceleration')
        Cache.remove('bike', 'agility')

        Cache.append('bike', 'title', bike_model.title)
        Cache.append('bike', 'power', bike_model.power)
        Cache.append('bike', 'speed', bike_model.speed)
        Cache.append('bike', 'acceleration', bike_model.acceleration)
        Cache.append('bike', 'agility', bike_model.agility)

    def set_power(self, value: Union[int, float]) -> None:
        self.power = self._max_val(value, self.max_power)

    def set_speed(self, value: Union[int, float]) -> None:
        self.speed = self._max_val(value, self.max_speed)

    def _max_val(self, val: Union[int, float], max_val: Union[int, float]) -> Union[int, float]:
        if val <= 0:
            return 0
        elif val > max_val:
            return max_val
        else:
            return val

    def is_in_sky(self) -> bool:
        road = self.get_road()
        if road:
            return road.line_points[-1] < self.y

    # Collisions

    def get_collisions(self, class_name: str) -> Optional[Widget]:
        children = [ro for ro in self.get_road().children[:] if ro.__class__.__name__ == class_name]
        for w in children:
            if w and self.collide_widget(w):  return w

    def on_collision_rock(self):
        rock = self.get_collisions('Rock')
        return rock and rock.on_collision(self)

    def on_collision_currency(self):
        currency = self.get_collisions('Currency')
        return currency and currency.on_collision(self)

    def on_collision_puddle(self) -> Optional[Widget]:
        puddle = self.get_collisions('Puddle')
        return puddle and puddle.on_collision(self)

    # Game objects

    def get_road(self) -> Optional[Widget]:
        return self.parent and ValidObject.road(GetObject.get_child(self.parent, 'Road'))
