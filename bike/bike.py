from kivy.animation import Animation
from kivy.lang import Builder
from kivy.properties import NumericProperty, StringProperty
from kivy.uix.image import Image
Builder.load_file("bike/bike.kv")


class Bike(Image):
    source = StringProperty('bike/bike-1.png')
    gravity = NumericProperty(0.2)
    acceleration = NumericProperty(0)
    speed = NumericProperty(0)
    max_speed = NumericProperty(60)

    # animation

    def anim_go(self):
        anim = Animation(angle=4, duration=.2)
        anim.start(self)

    def anim_relax(self):
        anim = Animation(angle=0, duration=.2)
        anim.start(self)

    def anim_stop(self):
        anim = Animation(angle=-2, duration=.1)
        anim.start(self)

    # events

    # info

    def show_status(self, title='BIKE'):
        return '''
------------------------------------------- [{}]
_acceleration:             {}
Speed:                          {}
Pos:                              {}
'''.format(
            title,
            self.acceleration,
            self.speed,
            self.pos,
        )
