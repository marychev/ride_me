from kivy.clock import Clock
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.event import EventDispatcher
from layout.base import BaseLayout
from utils.checks import show_outline


SECOND_GAME = 1.2 / 60


class BikeEvent(EventDispatcher):
    x = NumericProperty(0)
    y = NumericProperty(0)
    pos = ReferenceListProperty(x, y)

    acceleration = NumericProperty(0)
    speed = NumericProperty(0)
    max_speed = NumericProperty(0)
    gravity = NumericProperty(0)

    canvas = ObjectProperty(None)
    on_landing = ObjectProperty(None)
    on_move = ObjectProperty(None)
    on_relax = ObjectProperty(None)
    on_stop = ObjectProperty(None)

    road_pos = Vector(80, BaseLayout.tools_default_height())

    @staticmethod
    def unschedule(event_list):
        [Clock.unschedule(event) for event in event_list]

    def set_lending(self, dt):
        print('... set_lending ...')
        BikeEvent.unschedule([self.on_move, self.on_relax, self.on_stop])

        if self.road_pos.y < self.y:
            self.y -= self.speed
            self.add_speed(self.gravity)
        else:
            self.on_landing.cancel()
            self.stop()

        self._set_pos()

    def lending(self):
        print('LANDING')
        BikeEvent.unschedule([self.on_move, self.on_relax, self.on_stop])
        self.on_landing = Clock.schedule_interval(self.set_lending, SECOND_GAME)

    def set_move(self, dt):
        print('... set move ...', self.speed)
        BikeEvent.unschedule([self.on_landing, self.on_relax, self.on_stop])

        self.x += self.speed
        self.add_speed(self.acceleration)
        self._set_pos()

    def move(self):
        print('MOVE')
        BikeEvent.unschedule([self.on_landing, self.on_relax, self.on_stop])

        self.acceleration = 0.2
        self.on_move = Clock.schedule_interval(self.set_move, SECOND_GAME)

    def set_relax(self, dt):
        print('... set relax ...')
        BikeEvent.unschedule([self.on_landing, self.on_move, self.on_stop])

        self.x += self.speed
        self.add_speed(-self.acceleration)

        if self.speed <= 0:
            Clock.unschedule(self.on_relax)
            self.stop()

        self._set_pos()

    def relax(self):
        print('RELAX')
        BikeEvent.unschedule([self.on_landing, self.on_move, self.on_stop])

        self.acceleration = 0.01
        self.on_relax = Clock.schedule_interval(self.set_relax, 1 / 60)

    def set_stop(self, dt):
        print('... set stop ...')
        BikeEvent.unschedule([self.on_landing, self.relax, self.on_move])

        self.speed = 0
        self.x += self.speed
        self.add_speed(-self.acceleration)
        self._set_pos()

    def stop(self):
        BikeEvent.unschedule([self.on_landing, self.relax, self.on_move])

        self.speed = 0
        self.acceleration = 0.05
        self.on_stop = Clock.schedule_interval(self.set_stop, SECOND_GAME)

    def add_speed(self, value):
        self.speed += value
        if self.speed > self.max_speed:
            self.speed = self.max_speed

    def _set_pos(self):
        self.pos = Vector(self.x, self.y)
        self.canvas.before.clear()
        show_outline(self)
