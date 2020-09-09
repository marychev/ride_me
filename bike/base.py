from kivy.clock import Clock
from kivy.event import EventDispatcher
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, StringProperty
from kivy.vector import Vector

from layout.base import BaseLayout
from conf import SECOND_GAME
from utils.checks import show_outline
from utils.logs import Log

EVENT_NAME = 'on_wait'


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

    on_wait = ObjectProperty(None)
    on_landing = ObjectProperty(None)
    on_move = ObjectProperty(None)
    on_relax = ObjectProperty(None)
    on_stop = ObjectProperty(None)
    # events_list = ReferenceListProperty(on_landing, on_wait, on_move, on_relax, on_stop)

    current_event = StringProperty(EVENT_NAME)
    pre_event = StringProperty('undefined')

    @staticmethod
    def unschedule(event_list):
        [Clock.unschedule(event) for event in event_list]

    def can_wait(self):
        Log.try_to_set(EVENT_NAME, self)
        # it is on the land
        can = self.road_pos.y >= self.y
        Log.can_or_not(EVENT_NAME, can, self)
        return can

    def set_wait(self, dt):
        if self.can_wait():
            self.pre_event = self.current_event
            BaseBikeEvent.unschedule([self.on_move, self.on_relax, self.on_stop, self.on_landing])

    def wait(self):
        Log.start(EVENT_NAME, self)

        if self.can_wait():
            BaseBikeEvent.unschedule([self.on_move, self.on_relax, self.on_stop, self.on_landing])
            self.current_event = EVENT_NAME
            self.speed = 0
            self.acceleration = 0
            self.on_landing = Clock.schedule_interval(self.set_wait, SECOND_GAME)
            print('\n\tWaiting for some actions!!!\n\t------------------------------')

    def add_speed(self, value):
        self.speed += value
        if self.speed > self.max_speed:
            self.speed = self.max_speed

    def _set_pos(self):
        self.pos = Vector(self.x, self.y)
        self.canvas.before.clear()
        show_outline(self)

