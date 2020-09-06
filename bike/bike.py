from kivy.properties import NumericProperty, StringProperty
from kivy.uix.image import Image

from bike.bike_event import BikeEvent
from layout.base import BaseLayout
from utils.checks import show_outline


SECOND_GAME = 1 / 60
TMP_JUMP = 500
START_POS_X = 80
START_POS_Y = BaseLayout.tools_default_height() + TMP_JUMP


class Bike(Image, BikeEvent):
    source = StringProperty('bike/bike.png')

    x = NumericProperty(START_POS_X)
    y = NumericProperty(START_POS_Y)

    height = NumericProperty(60)
    width = NumericProperty(80)
    max_speed = NumericProperty(11)
    gravity = NumericProperty(0.2)

    def __init__(self, **kwargs):
        super(Bike, self).__init__(**kwargs)

        self.size_hint = None, None

        show_outline(self)

    def show_status(self, title='...'):
        return '''{}
        Speed:                  {}
        Velocity coordinates:   {}
        '''.format(
            title,
            self.speed,
            self.pos,
        )
