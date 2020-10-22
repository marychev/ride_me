from kivy.core.window import Window
from kivy.properties import NumericProperty, ObjectProperty
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from conf import SECOND_GAME
from utils.checks import set_texture_uvpos
from screen.utils import get_game_screen


class Road(Widget):
    texture = ObjectProperty(Image(source='road/road-2.png').texture)
    distance_traveled = NumericProperty(0)

    def __init__(self, **kwargs):
        super(Road, self).__init__(**kwargs)
        self.texture.wrap = 'repeat'
        self.texture.uvsize = (Window.width / self.texture.width, -1)

    @classmethod
    def get_bike(cls):
        return get_game_screen().ids.bike

    def get_status_bar(self):
        return self.parent.status_bar

    def go(self, dt):
        bike = self.get_bike()
        bike.acceleration += SECOND_GAME
        # self.acceleration += SECOND_GAME
        self.distance_traveled = self.texture.uvpos[0] + bike.acceleration  # self.acceleration
        set_texture_uvpos(self, self.distance_traveled, self.texture.uvpos[1])
        # todo: self.get_status_bar().show_status('Go bike ===>', self.parent.bike, self)

    def relax(self, dt):
        bike = self.get_bike()
        bike.acceleration -= SECOND_GAME + dt
        if bike.acceleration < 0:
            bike.acceleration = 0
            return False

        self.distance_traveled = self.texture.uvpos[0] + bike.acceleration   # self.acceleration
        set_texture_uvpos(self, self.distance_traveled, self.texture.uvpos[1])
        # todo: self.get_status_bar().show_status('... Relax ...', self.parent.bike, self)

    def stop(self, dt):
        bike = self.get_bike()
        bike.acceleration -= SECOND_GAME / dt
        if bike.acceleration < 0:
            bike.acceleration = 0
            return False

        self.distance_traveled = self.texture.uvpos[0] + bike.acceleration   # self.acceleration
        set_texture_uvpos(self, self.distance_traveled, self.texture.uvpos[1])
        # todo: self.get_status_bar().show_status('S T O P', self.parent.bike, self)

    def show_status(self, title='ROAD'):
        return '''
{}
-----------------------------------------------
UVPos:          {}
Pos:            {}'''.format(
            title,
            self.texture.uvpos, self.pos
        )
