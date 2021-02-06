from kivy.lang import Builder
from kivy.properties import NumericProperty, StringProperty
from kivy.uix.image import Image
from bike.animation import AnimationBike
from utils.dir import abstract_path
from utils.validation import ValidObject

Builder.load_file(abstract_path('bike/bike.kv'))


class Bike(Image, AnimationBike):
    source = StringProperty(abstract_path('bike/img/bike-1.png'))
    acceleration = NumericProperty(0.00)
    power = NumericProperty(150.00)
    max_power = NumericProperty(200.00)
    speed = NumericProperty(0.00)
    max_speed = NumericProperty(20.00)

    start_dt = NumericProperty(0.00)
    finish_dt = NumericProperty(0.00)

    collected_currency = NumericProperty(0)
    currency = NumericProperty(0)

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
        if self.parent:
            for el in self.parent.children[:]:
                if el.__class__.__name__ == 'Road': return ValidObject.road(el)
