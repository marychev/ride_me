from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import NumericProperty, ObjectProperty, ListProperty, OptionProperty
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from label.status_bar import StatusBar
from layout.background_image import BackgroundImageAnimation
from road.events import GoEventRoad, RelaxEventRoad, StopEventRoad, JumpEventRoad
from utils.checks import set_texture_uvpos
from conf import SECOND_GAME
from utils.validation import ValidObject
from utils.state import State

Builder.load_file("road/road.kv")


class Road(Widget):
    texture = ObjectProperty(Image(source='road/img/road-01.png').texture)
    total_way = NumericProperty(800)
    distance_traveled = NumericProperty(0)
    gravity = NumericProperty(2)
    state = OptionProperty(State.NONE, options=State.list_states())
    last_states = ListProperty()

    def __init__(self, **kwargs):
        super(Road, self).__init__(**kwargs)
        BackgroundImageAnimation.repeat_wrap(self.texture, Window.width / self.texture.width)
        Clock.schedule_interval(self.do_landing, SECOND_GAME)

        self.register_event_type(State.EVENT_ON_JUMP)
        self.register_event_type(State.EVENT_ON_GO)
        self.register_event_type(State.EVENT_ON_RELAX)
        self.register_event_type(State.EVENT_ON_STOP)

    def get_distance_traveled(self):
        return self.x + self.get_bike().speed

    def set_distance_traveled(self):
        self.distance_traveled = self.get_distance_traveled()
        set_texture_uvpos(self, self.distance_traveled + self.texture.uvpos[0], self.texture.uvpos[1])

    def has_finished(self):
        return self.distance_traveled >= self.total_way

    def set_state(self, name, count=5):
        self.state = name
        self.last_states.append(name)
        if len(self.last_states) > count:
            del self.last_states[0]
            del self.last_states[1]

    # events
    # on jump

    def do_landing(self, dt):
        event = JumpEventRoad(self, self.get_bike(), self.get_rock(), self.get_finish())
        return event.landing(dt)

    def on_jump(self, acceleration):
        bike = self.get_bike()
        event = JumpEventRoad(self, bike, self.get_rock(), self.get_finish())

        if event.up(acceleration):
            status_bar = StatusBar.get_status_bar()
            status_bar.show_status('JUMP start ===>' + self.state, bike, self)
        else:
            self.on_jump_stop()
            Clock.schedule_interval(self.do_landing, SECOND_GAME)
            print('\nXXX xx x .  jump  . x xx XXX\n')
            return False

    def on_jump_start(self):
        self.state = State.ON_JUMP_START
        Clock.schedule_interval(self.on_jump, SECOND_GAME)

    def on_jump_stop(self):
        Clock.unschedule(self.on_jump)

    # on go

    def on_go(self, acceleration):
        print('GO ROAD!', self.state, self.last_states)
        status_bar = StatusBar.get_status_bar()

        if self.has_finished():
            status_bar.show_status_finished()
            self.unschedule_events()
        else:
            bike = self.get_bike()
            event = GoEventRoad(self, bike, self.get_rock())

            if event.start(acceleration):
                status_bar.show_status('Go bike ===>', bike, self)
            else:
                status_bar.show_status('No Go ???', bike, self)
                self.unschedule_events()

    def on_go_start(self):
        self.state = State.ON_GO_START
        Clock.schedule_interval(self.on_go, SECOND_GAME)

    def on_go_stop(self):
        Clock.unschedule(self.on_go)

    # on relax

    def on_relax(self, acceleration):
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

    def on_relax_start(self):
        self.state = State.ON_RELAX_START
        Clock.schedule_interval(self.on_relax, SECOND_GAME)

    def on_relax_stop(self):
        Clock.unschedule(self.on_relax)

    # on stop

    def on_stop(self, acceleration):
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

    def on_stop_start(self):
        self.state = State.ON_STOP_START
        Clock.schedule_interval(self.on_stop, SECOND_GAME)

    def on_stop_stop(self):
        Clock.unschedule(self.on_stop)

    def unschedule_events(self):
        bg_animation = StatusBar.get_background_image_animation()
        self.on_jump_stop()
        self.on_go_stop()
        self.on_relax_stop()
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

    # game objects

    def get_tools(self):
        return ValidObject.tools(self.parent.parent.children[0])

    def get_bike(self):
        return ValidObject.bike(self.parent.children[0])

    def get_rock(self):
        return ValidObject.rock(self.children[1])

    def get_finish(self):
        return ValidObject.finish(self.children[0])
