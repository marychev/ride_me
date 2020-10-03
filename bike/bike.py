from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, StringProperty, ListProperty
from kivy.uix.image import Image
from kivy.vector import Vector
from conf import SECOND_GAME
from layout.base import BaseLayout
from bike.bike_events import BikeEvents
from utils.checks import show_outline
from kivy.clock import Clock


START_POS_X = 80
START_POS_Y = 128


class Bike(Image):
    source = StringProperty('bike/bike.png')

    x = NumericProperty(START_POS_X)
    y = NumericProperty(START_POS_Y)
    pos = ReferenceListProperty(x, y)

    height = NumericProperty(60)
    width = NumericProperty(80)
    canvas = ObjectProperty(None)

    gravity = NumericProperty(0.2)
    acceleration = NumericProperty(0)
    speed = NumericProperty(0)
    max_speed = NumericProperty(8)

    current_event = StringProperty('undefined')
    pre_event = StringProperty('undefined')
    available_events = ListProperty()

    # road_pos = Vector(80, BaseLayout.tools_default_height())

    def __init__(self, **kwargs):
        super(Bike, self).__init__(**kwargs)

        Clock.schedule_interval(self.move, SECOND_GAME)

        self.size_hint = None, None

        show_outline(self)

    def move(self, dt):
        if self.speed > 0:
            extra_speed = dt * self.speed
            self.pos = (self.x + extra_speed, self.y)
            self.speed -= (self.gravity * dt) * 11

    def on_go(self):
        self.speed += 10

    def on_stop(self):
        self.speed -= 15

    def define_available_events(self):
        self.available_events = []
        if self.can_landing():
            self.available_events.append('on_landing')
        if self.can_wait():
            self.available_events.append('on_wait')
        if self.can_go():
            self.available_events.append('on_go')
        if self.can_relax():
            self.available_events.append('on_relax')

    def show_status(self, title='...'):
        return '''{}
----------------------------------------------------------------------
Speed / Accel:              {} / {} 
Pos / x,y:                  {} / {}, {}
State pre/now/available:    {} / {} / {}
----------------------------------------------------------------------
        '''.format(
            title,
            self.speed, self.acceleration, self.gravity,
            self.pos, self.x, self.y,
            self.pre_event, self.current_event, self.available_events,
        )
