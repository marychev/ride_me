from kivy.animation import Animation
from kivy.graphics import Color, Rectangle
from kivy.lang import Builder
from kivy.properties import NumericProperty, StringProperty
from kivy.uix.image import Image
from kivy.core.window import Window
from utils.validation import ValidObject

Builder.load_file("bike/bike.kv")


class Bike(Image):
    source = StringProperty('bike/img/bike-1.png')
    gravity = NumericProperty(0.2)
    acceleration = NumericProperty(0)
    power = NumericProperty(100)
    speed = NumericProperty(0)
    max_speed = NumericProperty(60)

    def is_in_sky(self):
        road = self.get_road()
        return road.x + road.height < self.y

    # animation

    def anim_go(self):
        self.source = 'bike/img/bike-go.jpg'
        anim = Animation(angle=6, duration=.2)
        anim.start(self)

    def anim_relax(self):
        self.source = 'bike/img/bike-1.png'
        anim = Animation(angle=0, duration=.2)
        anim.start(self)

    def anim_stop(self):
        self.source = 'bike/img/bike-1.png'
        anim = Animation(angle=-3, duration=.1)
        anim.start(self)

    def anim_collision(self):
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
_power:                             {}
Speed:                          {}
Pos:                              {}
'''.format(
            title,
            self.acceleration, self.power,
            self.speed,
            self.pos,
        )

    # get parent and children

    def get_road(self):
        return ValidObject.road(self.parent.children[1])

    def get_rock(self):
        return ValidObject.rock(self.get_road().children[1])

    def get_finish(self):
        return ValidObject.finish(self.get_road().children[0])

    # initialization

    def init_pos(self):
        road = self.get_road()
        return 80, (road.y + road.height / 4) + 100

    def init_size(self):
        return int(Window.width / 16), int(Window.width / 16)
