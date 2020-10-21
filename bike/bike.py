from kivy.properties import NumericProperty, StringProperty
from kivy.uix.image import Image
# from kivy.vector import Vector
from conf import SECOND_GAME
# from bike.bike_events import BikeEvents
from kivy.clock import Clock

# START_POS_Y = BaseLayout.tools_default_height() + 30  # border
from kivy.lang import Builder
from kivy.animation import Animation
Builder.load_file("bike/bike.kv")


class Bike(Image):
    source = StringProperty('bike/bike.png')
    gravity = NumericProperty(0.2)
    acceleration = NumericProperty(0)
    speed = NumericProperty(0)
    max_speed = NumericProperty(60)

    # animation

    def anim_go(self):
        anim = Animation(angle=2, duration=.2)
        anim.start(self)

    def anim_relax(self):
        anim = Animation(angle=0, duration=.2)
        anim.start(self)

    def anim_stop(self):
        anim = Animation(angle=-2, duration=.1)
        anim.start(self)

    # events

    def move(self, dt):
        if self.speed > 0:
            extra_speed = dt * self.speed
            self.pos = (self.x + extra_speed, self.y)
            self.speed -= (self.gravity * dt) * 11

    def on_go(self):
        self.speed += 10

    def on_stop(self):
        self.speed -= 15

    # info

    def show_status(self, title='BIKE'):
        return '''
{}
-----------------------------------------------
Speed:              {}
Acceleration:   {}
Pos:                  {}
State (pre/now**):    {} / {}, {}
'''.format(
            title,
            self.speed, self.acceleration, self.pos,
            self.pre_event, self.current_event, self.available_events,
        )
