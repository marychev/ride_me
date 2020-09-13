from kivy.properties import NumericProperty, StringProperty, ReferenceListProperty
from kivy.uix.image import Image

from bike.bike_events import BikeEvents
from utils.checks import show_outline


START_POS_X = 80
START_POS_Y = 130


class Bike(BikeEvents, Image):
    source = StringProperty('bike/bike.png')

    x = NumericProperty(START_POS_X)
    y = NumericProperty(START_POS_Y + 100)
    pos = ReferenceListProperty(x, y)

    height = NumericProperty(60)
    width = NumericProperty(80)
    max_speed = NumericProperty(40)
    gravity = NumericProperty(0.2)

    def __init__(self, **kwargs):
        super(Bike, self).__init__(**kwargs)

        self.size_hint = None, None

        show_outline(self)

        self.on_wait()
        self.on_landing()

        print('\t\tbike')

    def show_status(self, title='...'):
        return '''{}
Speed / Accel:  {} {}
Pos / x,y:      {} / {}, {}
State pre/now:  {} / {}
        '''.format(
            title,
            self.speed, self.acceleration,
            self.pos, self.x, self.y,
            self.pre_event, self.current_event
        )
