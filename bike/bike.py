from kivy.lang import Builder
from kivy.properties import NumericProperty, StringProperty
from kivy.uix.image import Image
from bike.animation import AnimationBike
from utils.dir import abstract_path
from utils.validation import ValidObject
from utils.get_object import GetObject, app_config
from kivy.logger import Logger

Builder.load_file(abstract_path('bike/bike.kv'))


class Bike(Image, AnimationBike):
    source = StringProperty(abstract_path('bike/img/default.png'))
    acceleration = NumericProperty(0)
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

    def init_app_config(self):
        if app_config('bike', 'name') and app_config('bike', 'name') != 'None':
            self.max_power = app_config('bike', 'power')
            self.max_speed = app_config('bike', 'speed')
            self.acceleration = app_config('bike', 'acceleration')
            self.agility = app_config('bike', 'agility')

    def set_power(self, value):
        self.power = self._max_val(value, self.max_power)

    def set_speed(self, value):
        self.speed = self._max_val(value, self.max_speed)

    def _max_val(self, val, max_val):
        if val <= 0:
            return 0
        elif val > max_val:
            return max_val
        else:
            return val

    def is_in_sky(self):
        road = self.get_road()
        if road: return road.line_points[-1] < self.y

    # Collisions

    def get_collisions(self, class_name):
        children = [ro for ro in self.get_road().children[:] if ro.__class__.__name__ == class_name]
        for w in children:
            if w and self.collide_widget(w): return w

    def on_collision_rock(self):
        rock = self.get_collisions('Rock')
        return rock and rock.on_collision(self)

    def on_collision_currency(self):
        currency = self.get_collisions('Currency')
        return currency and currency.on_collision(self)

    def on_collision_puddle(self):
        puddle = self.get_collisions('Puddle')
        return puddle and puddle.on_collision(self)

    # Game objects

    def get_road(self):
        return self.parent and ValidObject.road(GetObject.get_child(self.parent, 'Road'))
