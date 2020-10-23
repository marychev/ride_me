from kivy.core.window import Window
from kivy.properties import NumericProperty, ObjectProperty
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from conf import SECOND_GAME
from utils.checks import set_texture_uvpos
from label.status_bar import StatusBar
from layout.background_image import BackgroundImageAnimation
from kivy.clock import Clock


class Road(Widget):
    texture = ObjectProperty(Image(source='road/road-2.png').texture)
    total_way = NumericProperty(100)
    distance_traveled = NumericProperty(0)

    def __init__(self, **kwargs):
        super(Road, self).__init__(**kwargs)
        BackgroundImageAnimation.repeat_wrap(self.texture, Window.width / self.texture.width)

    def go(self, acceleration):
        print('go road')
        status_bar = StatusBar.get_status_bar()
        if self.has_finished():
            status_bar.show_status('', None, self)
        else:
            bike = StatusBar.get_bike()
            bike.acceleration = acceleration

            bike.speed += acceleration
            self.set_distance_traveled(bike)
            status_bar.show_status('Go bike ===>', bike, self)

    def relax(self, acceleration):
        print('go Relax')
        status_bar = StatusBar.get_status_bar()
        if self.has_finished():
            status_bar.show_status('', None, self)
        else:
            bike = StatusBar.get_bike()
            bike.acceleration = acceleration

            if bike.speed - acceleration <= 0:
                bike.speed = 0
                status_bar.show_status('... Relax ...', bike, self)
                return False
            else:
                bike.speed -= acceleration
                self.set_distance_traveled(bike)
                status_bar.show_status('... Relax ...', bike, self)

    def stop(self, acceleration):
        print('on S T O P')
        status_bar = StatusBar.get_status_bar()
        if self.has_finished():
            status_bar.show_status('', None, self)
        else:
            bike = StatusBar.get_bike()
            bike.acceleration = acceleration
            stop_way = (acceleration + SECOND_GAME) * 2
            if bike.speed - stop_way <= 0:
                bike.speed = 0
                status_bar.show_status('S T O P', bike, self)
                return False
            else:
                bike.speed -= stop_way
                self.set_distance_traveled(bike)
                status_bar.show_status('S T O P', bike, self)

    def show_status(self, title='ROAD'):
        return '''
----------------------------------------------- [{}]
total_way:                  {}
distance_traveled:    {}'''.format(
            title,
            self.total_way,
            self.distance_traveled
        )

    def set_distance_traveled(self, bike):
        self.distance_traveled = self.texture.uvpos[0] + bike.speed
        set_texture_uvpos(self, self.distance_traveled, self.texture.uvpos[1])

    def has_finished(self):
        if self.distance_traveled >= self.total_way:
            bg_animation = StatusBar.get_background_image_animation()
            Clock.unschedule(self.go)
            Clock.unschedule(self.relax)
            Clock.unschedule(bg_animation.go_mountains)
            Clock.unschedule(bg_animation.relax_mountains)
            return True

        return False
