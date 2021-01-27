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
        return road.line_points[-1] < self.y

    # collisions
    # collision rock

    def get_collision_rock(self):
        rocks = [ro for ro in self.get_road().children[:] if ro.__class__.__name__ == 'Rock']
        for rock in rocks:
            if rock and self.collide_widget(rock):
                return rock

    def on_collision_rock(self):
        rock = self.get_collision_rock()
        if rock and self.collide_widget(rock):
            self._collision()
            return True
        return False

    # collision puddle

    def get_collision_puddle(self):
        puddles = [ro for ro in self.get_road().children[:] if ro.__class__.__name__ == 'Puddle']
        for puddle in puddles:
            if puddle and self.collide_widget(puddle):
                return puddle

    def on_collision_puddle(self):
        puddle = self.get_collision_puddle()
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
            Color(rgba=(1, 0, 0, .2))
            Rectangle(pos=self.pos, size=self.size)

    # game objects

    def get_road(self):
        return ValidObject.road(self.parent.children[1])

    def get_finish(self):
        return ValidObject.finish(self.get_road().children[0])
