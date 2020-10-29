from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import NumericProperty, ObjectProperty
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from label.status_bar import StatusBar
from layout.background_image import BackgroundImageAnimation
from road.events import GoEventRoad, RelaxEventRoad, StopEventRoad, JumpEventRoad
from utils.checks import set_texture_uvpos
from conf import SECOND_GAME

Builder.load_file("road/road.kv")


class Road(Widget):
    texture = ObjectProperty(Image(source='road/img/road-01.png').texture)
    total_way = NumericProperty(500)
    distance_traveled = NumericProperty(0)

    def __init__(self, **kwargs):
        super(Road, self).__init__(**kwargs)
        BackgroundImageAnimation.repeat_wrap(self.texture, Window.width / self.texture.width)
        Clock.schedule_interval(self.do_landing, SECOND_GAME)

    def do_landing(self, dt):
        event = JumpEventRoad(self, self.get_bike(), self.get_rock(), self.get_finish())
        return event.landing(dt)

    def jump(self, acceleration):
        print('JUMP road!')
        status_bar = StatusBar.get_status_bar()

        bike = self.get_bike()
        event = JumpEventRoad(self, bike, self.get_rock(), self.get_finish())

        if event.up(acceleration):
            status_bar.show_status('JUMP start ===>', bike, self)
        else:
            Clock.unschedule(self.jump)

            Clock.schedule_interval(self.do_landing, SECOND_GAME)
            status_bar.show_status('LANDING', bike, self)

    def go(self, acceleration):
        print('GO ROAD!')
        status_bar = StatusBar.get_status_bar()

        if self.has_finished():
            status_bar.show_status_finished()
            self.unschedule_events()
        else:
            bike = StatusBar.get_bike()
            event = GoEventRoad(self, bike, self.get_rock())

            if event.start(acceleration):
                status_bar.show_status('Go bike ===>', bike, self)
            else:
                status_bar.show_status('No Go ???', bike, self)
                self.unschedule_events()

    def relax(self, acceleration):
        print('RELAX ROAD!')
        status_bar = StatusBar.get_status_bar()

        if self.has_finished():
            status_bar.show_status_finished()
            self.unschedule_events()
        else:
            bike = StatusBar.get_bike()
            event = RelaxEventRoad(self, bike, self.get_rock())

            if event.start(acceleration):
                status_bar.show_status('... Relax ...', bike, self)
            else:
                status_bar.show_status('No relax ???', bike, self)
                self.unschedule_events()

    def stop(self, acceleration):
        print('STOP ROAD!')
        status_bar = StatusBar.get_status_bar()

        if self.has_finished():
            status_bar.show_status_finished()
        else:
            bike = self.get_bike()
            event = StopEventRoad(self, bike, self.get_rock())

            if event.start(acceleration):
                status_bar.show_status('S T O P', bike, self)
            else:
                status_bar.show_status('No stop ???', bike, self)
                self.unschedule_events()

    def get_distance_traveled(self, bike):
        return self.texture.uvpos[0] + bike.speed

    def set_distance_traveled(self, bike):
        self.distance_traveled = self.get_distance_traveled(bike)
        set_texture_uvpos(self, self.distance_traveled, self.texture.uvpos[1])

    def has_finished(self):
        return self.distance_traveled >= self.total_way

    def unschedule_events(self):
        bg_animation = StatusBar.get_background_image_animation()
        Clock.unschedule(self.jump)
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

    # get parents and children

    def get_bike(self):
        bike = self.parent.children[0]
        if bike.__class__.__name__ == 'Bike':
            return bike

    def get_rock(self):
        rock = self.children[1]
        if rock.__class__.__name__ == 'Rock':
            return rock

    def get_finish(self):
        finish = self.children[0]
        if finish.__class__.__name__ == 'Finish':
            return finish
