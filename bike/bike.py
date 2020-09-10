from kivy.properties import NumericProperty, StringProperty, ReferenceListProperty
from kivy.uix.image import Image

from bike.bike_event import BikeEvent
from utils.checks import show_outline


START_POS_X = 80
START_POS_Y = 150


class Bike(Image, BikeEvent):
    source = StringProperty('bike/bike.png')

    x = NumericProperty(START_POS_X)
    y = NumericProperty(START_POS_Y)
    pos = ReferenceListProperty(x, y)

    height = NumericProperty(60)
    width = NumericProperty(80)
    max_speed = NumericProperty(8)
    gravity = NumericProperty(0.2)

    def __init__(self, **kwargs):
        super(Bike, self).__init__(**kwargs)

        self.size_hint = None, None

        show_outline(self)

        # TODO: FOR DEV
        # check here position Road, Land and apply useful actions and events
        # self.landing()

    def show_status(self, title='...'):
        return '''{}
Speed:          {}
Pos / x,y:      {} / {}, {}
State pre/now:  {} / {}
        '''.format(
            title,
            self.speed,
            self.pos, self.x, self.y,
            self.pre_event, self.current_event
        )
