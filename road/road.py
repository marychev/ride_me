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
        #self.texture.uvsize = (1, -1)

    @classmethod
    def get_bike(cls):
        return get_game_screen().ids.bike

    @staticmethod
    def get_status_bar():
        return get_game_screen().ids.status_bar

    def go(self, acceleration):
        print('go road')
        bike = self.get_bike()
        bike.acceleration = acceleration

        bike.speed += acceleration
        self.set_distance_traveled(bike)
        self.get_status_bar().show_status('Go bike ===>', bike, self)

    def relax(self, acceleration):
        print('go Relax')
        bike = self.get_bike()
        bike.acceleration = acceleration

        if bike.speed - acceleration <= 0:
            bike.speed = 0
            self.get_status_bar().show_status('... Relax ...', bike, self)
            return False
        else:
            bike.speed -= acceleration
            self.set_distance_traveled(bike)
            self.get_status_bar().show_status('... Relax ...', bike, self)

    def stop(self, acceleration):
        print('on S T O P')
        bike = self.get_bike()
        bike.acceleration = acceleration
        stop_way = (acceleration + SECOND_GAME) * 2
        if bike.speed - stop_way <= 0:
            bike.speed = 0
            self.get_status_bar().show_status('S T O P', bike, self)
            return False
        else:
            bike.speed -= stop_way
            self.set_distance_traveled(bike)
            self.get_status_bar().show_status('S T O P', bike, self)

    def show_status(self, title='ROAD'):
        return '''
----------------------------------------------- [{}]
distance_traveled:          {}'''.format(
            title,
            self.distance_traveled
        )

    def set_distance_traveled(self, bike):
        self.distance_traveled = self.texture.uvpos[0] + bike.speed
        set_texture_uvpos(self, self.distance_traveled, self.texture.uvpos[1])
