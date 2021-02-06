from kivy.graphics import Color, Rectangle
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
        if road:
            return road.line_points[-1] < self.y

    # Collisions

    def get_collisions(self, class_name):
        child = [ro for ro in self.get_road().children[:] if ro.__class__.__name__ == class_name]
        for w in child:
            if w and self.collide_widget(w):
                return w

    # collision rock

    def on_collision_rock(self):
        rock = self.get_collisions('Rock')
        if rock and self.collide_widget(rock):
            self._collision()
            return True
        return False

    # collision currency

    def on_collision_currency(self):
        currency = self.get_collisions('Currency')
        if currency and self.collide_widget(currency):
            self.anim_collision()
            from kivy.animation import Animation
            currency.color_label = 1, .6, 0, 1
            anim = Animation(y=currency.y+1000, duration=.2)
            anim.start(currency)
            return True
        return False

    # collision puddle

    def on_collision_puddle(self):
        puddle = self.get_collisions('Puddle')
        if puddle and self.collide_widget(puddle):
            self.anim_collision()

            if self.speed > 0 or self.power > 0:
                self.acceleration -= self.acceleration / 100
                self.set_speed(self.speed - (self.max_speed / 1000))
                self.set_power(self.power - (self.max_power / 1000))

            return True
        return False

    def _collision(self):
        self.speed = 0
        self.power = 0
        self.acceleration = 0
        self.draw_collision_rectangle()
        self.anim_collision()

    def draw_collision_rectangle(self):
        with self.canvas:
            Color(rgba=(1, 0, 0, .2), group="background")
            Rectangle(pos=self.pos, size=self.size, group="background")

    # game objects

    def get_road(self):
        if self.parent:
            for el in self.parent.children[:]:
                if el.__class__.__name__ == 'Road':
                    return ValidObject.road(el)

    def get_finish(self):
        return ValidObject.finish(self.get_road().children[0])
