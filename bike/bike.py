import os
from kivy.animation import Animation
from kivy.graphics import Color, Rectangle
from kivy.lang import Builder
from kivy.properties import NumericProperty, StringProperty
from kivy.uix.image import Image
from utils.validation import ValidObject
from kivy.clock import Clock
from conf import SECOND_GAME

path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'bike.kv'))
Builder.load_file(path)


class Bike(Image):
    source = StringProperty('bike/img/bike-1.png')
    acceleration = NumericProperty(0)
    power = NumericProperty(50)
    max_power = NumericProperty(150.00)
    speed = NumericProperty(0)
    max_speed = NumericProperty(60)

    def set_power(self, dt):
        if float(self.power + dt) < float(self.max_power):
            power = self.power
            power = power - (dt*100) if int(dt) < 0 else power + (dt*100)
            self.power = float('{:3.2f}'.format(power))
        else:
            self.power = float(self.max_power)

    def is_in_sky(self):
        road = self.get_road()
        return road.y < self.y

    # animation

    def anim_go(self):
        self.source = 'bike/img/bike-go.png'
        anim = Animation(angle=8, duration=.2)
        anim.start(self)

    def anim_relax(self):
        self.source = 'bike/img/bike-relax.png'
        anim = Animation(angle=0, duration=.2)
        anim.start(self)

    def anim_wait(self):
        self.source = 'bike/img/bike-wait.png'
        anim = Animation(angle=0, duration=.2)
        anim.start(self)

    def anim_stop(self):
        self.source = 'bike/img/bike-stop.png'
        anim = Animation(angle=-1, duration=.1)
        anim.start(self)

    def anim_jump_up(self):
        self.source = 'bike/img/bike-jump-up.png'
        anim = Animation(angle=8, duration=.2)
        anim.start(self)

    def anim_landing(self):
        self.source = 'bike/img/bike-landing.png'
        anim = Animation(angle=-8, duration=.2)
        anim.start(self)

    def anim_collision(self):
        self.source = 'bike/img/bike-1.png'
        anim = Animation(angle=180, duration=.2)
        anim.start(self)

    # events

    def collision_rock(self):
        self.speed = 0
        self.acceleration = 0

        with self.canvas:
            Color(rgba=(1, 0, 0, .2))
            Rectangle(pos=self.pos, size=self.size)

        self.anim_collision()

    # info

    def show_status(self, title='BIKE'):
        return '''
------------------------------------------- [{}]
_acceleration:             {}
_power:                           {} 
Speed:                          {}
Pos:                              {}
'''.format(
            title,
            self.acceleration, self.power,
            self.speed,
            self.pos,
        )

    # game objects

    def get_road(self):
        return ValidObject.road(self.parent.children[1])

    def get_rock(self):
        return ValidObject.rock(self.get_road().children[1])

    def get_finish(self):
        return ValidObject.finish(self.get_road().children[0])
