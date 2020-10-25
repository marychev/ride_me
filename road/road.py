from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import NumericProperty, ObjectProperty
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from label.status_bar import StatusBar
from layout.background_image import BackgroundImageAnimation
from road.events import GoEventRoad, RelaxEventRoad, StopEventRoad
from road.finish import Finish
from utils.checks import set_texture_uvpos

Builder.load_file("road/road.kv")


class Road(Widget):
    texture = ObjectProperty(Image(source='road/img/road-01.png').texture)
    total_way = NumericProperty(800)
    distance_traveled = NumericProperty(0)

    finish = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(Road, self).__init__(**kwargs)
        BackgroundImageAnimation.repeat_wrap(self.texture, Window.width / self.texture.width)

    @classmethod
    def set_finish_x(cls):
        if not isinstance(cls.finish, Finish):
            cls.finish = StatusBar.get_finish()
        cls.finish.set_x()

    def go(self, acceleration):
        print('GO ROAD!')
        status_bar = StatusBar.get_status_bar()

        if self.has_finished():
            status_bar.show_status_finished()
            self.unschedule_events()
        else:
            bike = StatusBar.get_bike()
            event = GoEventRoad(self, bike, StatusBar.get_rock())

            if event.start(acceleration):
                status_bar.show_status('Go bike ===>', bike, self)

    def relax(self, acceleration):
        print('RELAX ROAD!')
        status_bar = StatusBar.get_status_bar()

        if self.has_finished():
            status_bar.show_status_finished()
            self.unschedule_events()
        else:
            bike = StatusBar.get_bike()
            event = RelaxEventRoad(self, bike, StatusBar.get_rock())

            if event.start(acceleration):
                status_bar.show_status('... Relax ...', bike, self)
            else:
                # event stops or can't start
                return False

    def stop(self, acceleration):
        status_bar = StatusBar.get_status_bar()

        if self.has_finished():
            status_bar.show_status_finished()
        else:
            bike = StatusBar.get_bike()
            event = StopEventRoad(self, bike, StatusBar.get_rock())

            if event.start(acceleration):
                status_bar.show_status('S T O P', bike, self)

    def set_distance_traveled(self, bike):
        self.distance_traveled = self.texture.uvpos[0] + bike.speed
        set_texture_uvpos(self, self.distance_traveled, self.texture.uvpos[1])

    def has_finished(self):
        return self.distance_traveled >= self.total_way

    def unschedule_events(self):
        bg_animation = StatusBar.get_background_image_animation()
        Clock.unschedule(self.go)
        Clock.unschedule(self.relax)
        Clock.unschedule(bg_animation.go_mountains)
        Clock.unschedule(bg_animation.relax_mountains)

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
