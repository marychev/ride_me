from kivy.animation import Animation
from kivy.lang import Builder
from kivy.properties import NumericProperty, StringProperty
from label.status_bar import StatusBar
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
from road.events import JumpEventRoad

Builder.load_file("bike/bike.kv")


class Bike(Image):
    source = StringProperty('bike/img/bike-1.png')
    gravity = NumericProperty(0.2)
    acceleration = NumericProperty(0)
    power = NumericProperty(100)
    speed = NumericProperty(0)
    max_speed = NumericProperty(60)

    def get_road(self):
        road = self.parent.children[1]
        if road.__class__.__name__ == 'Road':
            return road

    def get_rock(self):
        rock = self.get_road().children[1]
        if rock.__class__.__name__ == 'Rock':
            return rock

    def get_finish(self):
        finish = self.get_road().children[0]
        if finish.__class__.__name__ == 'Finish':
            return finish

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
    def has_collision_rock(self):
        rock = self.get_rock()
        return rock.x <= self.x + self.width

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
