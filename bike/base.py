from kivy.clock import Clock
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, StringProperty
from kivy.vector import Vector
from kivy.event import EventDispatcher
from utils.checks import show_outline
from layout.base import BaseLayout


class BaseBikeEvent(EventDispatcher):
    x = NumericProperty(0)
    y = NumericProperty(0)
    pos = ReferenceListProperty(x, y)

    acceleration = NumericProperty(0)
    speed = NumericProperty(0)
    max_speed = NumericProperty(0)
    gravity = NumericProperty(0)

    canvas = ObjectProperty(None)

    road_pos = Vector(80, BaseLayout.tools_default_height())

    on_landing = ObjectProperty(None)
    on_move = ObjectProperty(None)
    on_relax = ObjectProperty(None)
    on_stop = ObjectProperty(None)

    current_event = StringProperty('')

    @staticmethod
    def unschedule(event_list):
        [Clock.unschedule(event) for event in event_list]

    def add_speed(self, value):
        self.speed += value
        if self.speed > self.max_speed:
            self.speed = self.max_speed

    def _set_pos(self):
        self.pos = Vector(self.x, self.y)
        self.canvas.before.clear()
        show_outline(self)

