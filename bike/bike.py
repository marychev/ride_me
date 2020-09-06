from kivy.clock import Clock
from kivy.properties import NumericProperty, ReferenceListProperty, StringProperty, ObjectProperty
from kivy.uix.image import Image
from kivy.vector import Vector

from layout.base import BaseLayout
from utils.checks import show_outline

TMP_JUMP = 500
START_POS_X = 80
START_POS_Y = BaseLayout.tools_default_height() + TMP_JUMP


class Bike(Image):
    source = StringProperty('bike/bike.png')

    x = NumericProperty(START_POS_X)
    y = NumericProperty(START_POS_Y)
    pos = ReferenceListProperty(x, y)

    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    height = NumericProperty(60)
    width = NumericProperty(80)
    acceleration = NumericProperty(0)
    speed = NumericProperty(0)
    max_speed = NumericProperty(11)
    gravity = NumericProperty(0.2)
    mass = NumericProperty(0)

    road_pos = Vector(80, BaseLayout.tools_default_height())

    on_move = ObjectProperty(None)
    on_relax = ObjectProperty(None)
    on_stop = ObjectProperty(None)

    SECOND_GAME = 1 / 60

    def __init__(self, **kwargs):
        super(Bike, self).__init__(**kwargs)

        self.size_hint = None, None

        show_outline(self)

    def set_lending(self, dt):
        Clock.unschedule(self.on_move)
        Clock.unschedule(self.on_relax)
        Clock.unschedule(self.on_stop)

        if self.road_pos.y < self.y:
            self.y -= self.speed
            self.add_speed(self.gravity)
        else:
            self.speed = 0

        self.pos = Vector(self.x, self.y)
        self.canvas.before.clear()
        show_outline(self)

    def lending(self):
        Clock.unschedule(self.on_move)
        Clock.unschedule(self.on_relax)
        Clock.unschedule(self.on_stop)

        if self.road_pos.y < self.y:
            duration = int((self.road_pos.y + self.y) / 10)
            for i in range(duration):
                Clock.schedule_once(self.set_lending, i / 60)

    def set_move(self, dt):
        print('... loop MOVE ...', self.speed)
        Clock.unschedule(self.on_relax)
        Clock.unschedule(self.on_stop)

        self.x += self.speed
        self.add_speed(self.acceleration)
        self.pos = Vector(self.x, self.y)

        self.canvas.before.clear()
        show_outline(self)
        print(' - * -')

    def move(self):
        print('>>>>>>>> MOVE ', self.speed)
        Clock.unschedule(self.on_relax)
        Clock.unschedule(self.on_stop)

        self.acceleration = 0.2
        self.on_move = Clock.schedule_interval(self.set_move, self.SECOND_GAME)

    def set_relax(self, dt):
        print('... RELAX ...', self.speed)
        Clock.unschedule(self.on_move)
        Clock.unschedule(self.on_stop)

        self.x += self.speed
        self.add_speed(-self.acceleration)
        self.pos = Vector(self.x, self.y)

        if self.speed <= 0:
            self.speed = 0
            Clock.unschedule(self.on_relax)
            self.stop()

        self.canvas.before.clear()
        show_outline(self)
        print(' - * -')

    def relax(self):
        Clock.unschedule(self.on_move)
        Clock.unschedule(self.on_stop)

        self.acceleration = 0.01
        self.on_relax = Clock.schedule_interval(self.set_relax, 1 / 60)

    def set_stop(self, dt):
        print('... STOP ...', self.speed)

        Clock.unschedule(self.on_relax)
        Clock.unschedule(self.on_move)

        self.x += self.speed
        self.add_speed(-self.acceleration)
        self.pos = Vector(self.x, self.y)

        if self.speed <= 0:
            Clock.unschedule(self.on_stop)

        self.canvas.before.clear()
        show_outline(self)
        print(' - * -')

    def stop(self):
        Clock.unschedule(self.on_relax)
        Clock.unschedule(self.on_move)

        self.speed = 0
        self.acceleration = 0.05
        self.on_stop = Clock.schedule_interval(self.set_stop, self.SECOND_GAME)

    def add_speed(self, value):
        self.speed += value

        if self.speed > self.max_speed:
            self.speed = self.max_speed
        elif self.speed <= 0:
            self.speed = 0
            # self.stop()

    def show_status(self, title='...'):
        return '''{}
        Speed:                  {}
        Velocity coordinates:   {}
        '''.format(
            title,
            self.speed,
            self.pos,
        )
