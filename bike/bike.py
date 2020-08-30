from kivy.clock import Clock
from kivy.properties import NumericProperty, ReferenceListProperty, StringProperty
from kivy.uix.image import Image
from kivy.vector import Vector

from layout.base import BaseLayout
from utils.checks import show_outline


class Bike(Image):
    source = StringProperty('bike/bike.png')
    x = NumericProperty(80)
    y = NumericProperty(BaseLayout.tools_default_height())
    height = NumericProperty(60)
    width = NumericProperty(80)

    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def __init__(self, **kwargs):
        super(Bike, self).__init__(**kwargs)

        self.size_hint = None, None

        show_outline(self)

    def set_move(self):
        self._set_velocity((0.1, 0))

    def move(self):
        Clock.schedule_interval(lambda x: self.set_move(), 1 / 60)

    def set_relax(self):
        self._set_velocity()

    def relax(self):
        Clock.schedule_interval(lambda x: self.set_relax(), 1 / 60)

    def set_stop(self):
        self._set_velocity((-0.1, 0))

    def stop(self):
        Clock.schedule_interval(lambda x: self.set_stop(), 1 / 60)

    def _set_velocity(self, velocity=(0, 0)):
        self.velocity = Vector(velocity)
        self.pos = Vector(*self.velocity) + (self.x, self.y)
        self.x, self.y = self.pos[0], self.pos[1]
