from kivy.clock import Clock
from kivy.event import EventDispatcher
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, StringProperty, ListProperty
from kivy.vector import Vector

from utils.checks import show_outline


class BaseBikeEvent(EventDispatcher):
    x = NumericProperty(0)
    y = NumericProperty(0)
    pos = ReferenceListProperty(x, y)

    acceleration = NumericProperty(0)
    speed = NumericProperty(0)
    max_speed = NumericProperty(0)
    gravity = NumericProperty(0)

    canvas = ObjectProperty(None)

    current_event = StringProperty('undefined')
    pre_event = StringProperty('undefined')
    available_events = ListProperty()

    def add_speed(self, value):
        self.speed += value
        if self.speed > self.max_speed:
            self.speed = self.max_speed

        if self.speed <= 0:
            self.on_wait()

        return self.speed

    def _set_pos(self):
        self.x += self.speed

        self.pos = Vector(self.x, self.y)
        self.canvas.before.clear()
        show_outline(self)

