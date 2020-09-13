from kivy.properties import NumericProperty, StringProperty, ReferenceListProperty
from kivy.uix.image import Image
from kivy.vector import Vector

from layout.base import BaseLayout
from bike.bike_events import BikeEvents
from utils.checks import show_outline


START_POS_X = 80
START_POS_Y = 128 + 100


class Bike(BikeEvents, Image):
    source = StringProperty('bike/bike.png')

    x = NumericProperty(START_POS_X)
    y = NumericProperty(START_POS_Y)
    pos = ReferenceListProperty(x, y)

    height = NumericProperty(60)
    width = NumericProperty(80)
    max_speed = NumericProperty(40)

    road_pos = Vector(80, BaseLayout.tools_default_height())

    def __init__(self, **kwargs):
        super(Bike, self).__init__(**kwargs)

        self.size_hint = None, None

        self.define_available_events()
        if 'on_landing' in self.available_events:
            self.on_landing()

        show_outline(self)

    def define_available_events(self):
        self.available_events = []
        if self.can_landing():
            self.available_events.append('on_landing')
        if self.can_wait():
            self.available_events.append('on_wait')
        if self.can_move():
            self.available_events.append('on_motion')
        if self.can_relax():
            self.available_events.append('on_relax')
        print(self.available_events)

    def show_status(self, title='...'):
        return '''{}
----------------------------------------------------------------------
Speed / Accel / Gravity:    {} / {} / {}
Pos / x,y:                  {} / {}, {}
State pre/now/available:    {} / {} / {}
Loop Event:                 {}
Road:                       {}
----------------------------------------------------------------------
        '''.format(
            title,
            self.speed, self.acceleration, self.gravity,
            self.pos, self.x, self.y,
            self.pre_event, self.current_event, self.available_events,
            self.loop_event,
            self.road_pos
        )
