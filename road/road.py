from kivy.core.window import Window
from kivy.properties import NumericProperty, ObjectProperty
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from conf import SECOND_GAME
from utils.checks import set_texture_uvpos
from label.status_bar import StatusBar
from layout.background_image import BackgroundImageAnimation
from kivy.clock import Clock
from kivy.lang import Builder

Builder.load_file("road/road.kv")


class Road(Widget):
    texture = ObjectProperty(Image(source='road/img/road-2.png').texture)
    total_way = NumericProperty(800)
    distance_traveled = NumericProperty(0)

    def __init__(self, **kwargs):
        super(Road, self).__init__(**kwargs)
        BackgroundImageAnimation.repeat_wrap(self.texture, Window.width / self.texture.width)

    @classmethod
    def set_finish_x(cls):
        road = StatusBar.get_road()
        bike = StatusBar.get_bike()
        finish = StatusBar.get_finish()
        finish.x = (road.total_way - road.distance_traveled) + bike.x + bike.width

    def go(self, acceleration):
        status_bar = StatusBar.get_status_bar()

        if self.has_finished():
            status_bar.show_status('', None, self)
        else:
            bike = StatusBar.get_bike()
            bike.acceleration = acceleration
            bike.speed += acceleration
            self.set_distance_traveled(bike)

            self.set_finish_x()
            status_bar.show_status('Go bike ===>', bike, self)

    def relax(self, acceleration):
        status_bar = StatusBar.get_status_bar()

        if self.has_finished():
            status_bar.show_status('', None, self)
        else:
            bike = StatusBar.get_bike()
            bike.acceleration = acceleration

            if bike.speed - acceleration <= 0:
                bike.speed = 0

                self.set_finish_x()
                status_bar.show_status('... Relax ...', bike, self)
                return False
            else:
                bike.speed -= acceleration
                self.set_distance_traveled(bike)

                self.set_finish_x()
                status_bar.show_status('... Relax ...', bike, self)

    def stop(self, acceleration):
        status_bar = StatusBar.get_status_bar()

        if self.has_finished():
            status_bar.show_status('', None, self)
        else:
            bike = StatusBar.get_bike()
            bike.acceleration = acceleration
            stop_way = (acceleration + SECOND_GAME) * 2

            if bike.speed - stop_way <= 0:
                bike.speed = 0

                self.set_finish_x()
                status_bar.show_status('S T O P', bike, self)
                return False
            else:
                bike.speed -= stop_way
                self.set_distance_traveled(bike)

                self.set_finish_x()
                status_bar.show_status('S T O P', bike, self)

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

    def show_status(self, title='ROAD'):
        return '''
----------------------------------------------- [{}]
total_way:                    {}
distance_traveled:    {}
*left_go:                          {}'''.format(
            title,
            self.total_way,
            self.distance_traveled,
            self.total_way - self.distance_traveled,
        )
