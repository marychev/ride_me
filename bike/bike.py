from kivy.animation import Animation
from kivy.lang import Builder
from kivy.properties import NumericProperty, StringProperty
from label.status_bar import StatusBar
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
Builder.load_file("bike/bike.kv")


class Bike(Image):
    source = StringProperty('bike/img/bike-1.png')
    gravity = NumericProperty(0.2)
    acceleration = NumericProperty(0)
    speed = NumericProperty(0)
    max_speed = NumericProperty(60)

    # animation

    def anim_go(self):
        anim = Animation(angle=6, duration=.2)
        anim.start(self)

    def anim_relax(self):
        anim = Animation(angle=0, duration=.2)
        anim.start(self)

    def anim_stop(self):
        anim = Animation(angle=-3, duration=.1)
        anim.start(self)

    def anim_collision(self):
        anim = Animation(angle=180, duration=.2)
        anim.start(self)

    # events
    def has_collision_rock(self):
        rock = StatusBar.get_rock()
        return rock.x <= self.x + self.width

    def collision_rock(self):
        rock = StatusBar.get_rock()
        print('**** COLLISION START ', rock.x <= self.width+self.x)
        self.speed = 0
        self.acceleration = 0

        with self.canvas:
            Color(rgba=(1, 0, 0, .2))
            Rectangle(pos=self.pos, size=self.size)

        self.anim_collision()

        print('COLLISION END  <****')

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
