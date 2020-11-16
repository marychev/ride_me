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
    acceleration = NumericProperty(0)
    power = NumericProperty(50)
    max_power = NumericProperty(250.00)
    speed = NumericProperty(0)
    max_speed = NumericProperty(60)

    def set_power(self, dt):
        if float(self.power + dt) < float(self.max_power):
            power = self.power
            power = power - (dt*100) if int(dt) < 0 else power + (dt*100)
            self.power = float('{:3.2f}'.format(power))
        else:
            self.power = float(self.max_power)

    def is_in_sky(self):
        road = self.get_road()
        return road.line_points[-1] < self.y

    # events

    def collision_rock(self):
        self.speed = 0
        self.acceleration = 0

        with self.canvas:
            Color(rgba=(1, 0, 0, .2))
            Rectangle(pos=self.pos, size=self.size)

        self.anim_collision()

    # game objects

    def get_road(self):
        return ValidObject.road(self.parent.children[1])

    def get_rock(self):
        return ValidObject.rock(self.get_road().children[1])

    def get_puddle(self):
        return ValidObject.rock(self.get_road().children[2])

    def get_lamp(self):
        return ValidObject.rock(self.get_road().children[3])

    def get_finish(self):
        return ValidObject.finish(self.get_road().children[0])
