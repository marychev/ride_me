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
    total_way = NumericProperty(1800)
    distance_traveled = NumericProperty(0)
    gravity = NumericProperty(2)
    state = OptionProperty(State.NONE, options=State.list_states())
    last_states = ListProperty()

    def __init__(self, **kwargs):
        super(Road, self).__init__(**kwargs)
        BackgroundImageAnimation.repeat_wrap(self.texture, Window.width / self.texture.width)
        self.on_landing_start()

        self.register_event_type(State.EVENT_ON_JUMP)
        self.register_event_type(State.EVENT_ON_LANDING)
        self.register_event_type(State.EVENT_ON_GO)
        self.register_event_type(State.EVENT_ON_RELAX)
        self.register_event_type(State.EVENT_ON_STOP)

    def get_distance_traveled(self):
        return self.x + self.get_bike().speed

    def set_distance_traveled(self):
        self.distance_traveled += self.get_distance_traveled()
        set_texture_uvpos(self, self.texture.uvpos[0] + self.get_bike().speed, self.texture.uvpos[1])

    def has_finished(self):
        return self.distance_traveled >= self.total_way

    def set_state(self, name, count=5):
        self.state = name
        self.last_states.append(name)
        if len(self.last_states) > count:
            del self.last_states[0]
            del self.last_states[1]

    # Events
    # -- on landing --

    def on_landing(self, acceleration):
        #print('on_landing', self.state)
        event = JumpEventRoad(self, self.get_bike(), self.get_rock(), self.get_finish())
        status_bar = StatusBar.get_status_bar()
        if event.landing(acceleration):
            status_bar.show_status('On Landing: ' + self.state, self.get_bike(), self)
            return True
        else:
            self.on_landing_stop()
            status_bar.show_status('Stop On Landing: ' + self.state, self.get_bike(), self)
            return False

    def on_landing_start(self):
        if self.state in (State.ON_JUMP_UP_MOVE, State.ON_JUMP_UP_STOP):
            Clock.schedule_interval(self.on_landing, SECOND_GAME)

            self.state = State.ON_JUMP_LANDING
            if self.get_bike():
                self.get_bike().anim_landing()
        else:
            print('\nXXX xx x .  landing  . x xx XXX\n', self.state)

    def on_landing_stop(self):
        if self.state in [State.ON_JUMP_LANDING, State.ON_JUMP_LANDING_STOP]:
            self.get_bike().anim_wait()
            print('I')
            Clock.unschedule(self.on_landing)
            print('II', self.state)

    # -- on jump up --

    def on_jump(self, acceleration):
        # print('on jump', self.state)
        bike = self.get_bike()
        status_bar = StatusBar.get_status_bar()
        event = JumpEventRoad(self, bike, self.get_rock(), self.get_finish())

        if event.up(acceleration):
            status_bar.show_status('On Jump: ' + self.state, bike, self)
        else:
            self.on_jump_stop()
            self.on_landing_start()
            status_bar.show_status('Stop On Jump: ' + self.state, bike, self)
            return False

    def on_jump_start(self):
        if self.state not in (State.ON_JUMP_LANDING, State.ON_JUMP_UP_MOVE):
            Clock.schedule_interval(self.on_jump, SECOND_GAME)
            self.state = State.ON_JUMP_START
            self.get_bike().anim_jump_up()
        else:
            print('\nXXX xx x .  jump  . x xx XXX\n')

    def on_jump_stop(self):
        if self.state == State.ON_JUMP_UP_MOVE:
            # self.get_bike().anim_relax()
            Clock.unschedule(self.on_jump)

    # -- on go --

    def on_go(self, acceleration):
        # print('GO ROAD!', self.state, self.last_states)
        status_bar = StatusBar.get_status_bar()

        if self.has_finished():
            status_bar.show_status_finished()
            self.unschedule_events()
        else:
            bike = self.get_bike()
            event = GoEventRoad(self, bike, self.get_rock())

            if event.start(acceleration):
                status_bar.show_status('On Go: ' + self.state, bike, self)
            else:
                status_bar.show_status('Stop On Go: ' + self.state, bike, self)
                self.unschedule_events()
                return False

    def on_go_start(self):
        print('\n\t--- > TRY START', self.state)
        print('----------------------------------------')
        if self.state in [State.ON_RELAX_MOVE, State.ON_RELAX_STOP, State.NONE]:
            Clock.schedule_interval(self.on_go, SECOND_GAME)

            self.state = State.ON_GO_START
            self.get_bike().anim_go()
        else:
            print('\nXXX xx x .  go  . x xx XXX\n', self.state)

    def on_go_stop(self):
        if self.state == State.ON_GO_MOVE:
            self.get_bike().anim_relax()
            Clock.unschedule(self.on_go)

    # -- on relax --

    def on_relax(self, acceleration):
        # print('On Relax', self.state, self.last_states)
        status_bar = StatusBar.get_status_bar()

        if self.has_finished():
            status_bar.show_status_finished()
            self.unschedule_events()
        else:
            bike = StatusBar.get_bike()
            event = RelaxEventRoad(self, bike, self.get_rock())

            if event.start(acceleration):
                status_bar.show_status('On Relax: ' + self.state, bike, self)
            else:
                status_bar.show_status('Stop On Relax: ' + self.state, bike, self)
                self.unschedule_events()
                return False

    def on_relax_start(self):
        print(self.state, '<<<<<<<<<<,')
        if self.state not in [State.ON_JUMP_UP_MOVE]:
            self.state = State.ON_RELAX_START
            self.get_bike().anim_relax()
            Clock.schedule_interval(self.on_relax, SECOND_GAME)
        else:
            print('\nXXX xx x .  relax start  . x xx XXX\n', self.state)

    def on_relax_stop(self):
        print('III', self.state)
        if self.state in [State.ON_RELAX_MOVE, State.ON_RELAX_STOP]:
            Clock.unschedule(self.on_relax)
            self.get_bike().anim_wait()
        else:
            print('\nXXX xx x .  relax stop  . x xx XXX\n', self.state)

    # -- on stop --

    def on_stop(self, acceleration):
        status_bar = StatusBar.get_status_bar()

        if self.has_finished():
            status_bar.show_status_finished()
        else:
            bike = self.get_bike()
            event = StopEventRoad(self, bike, self.get_rock())
            if event.start(acceleration):
                status_bar.show_status('On Stop: ' + self.state, bike, self)
            else:
                status_bar.show_status('Stop On Stop: ' + self.state, bike, self)
                self.unschedule_events()
                return False

    def on_stop_start(self):
        if self.state not in (State.ON_RELAX_STOP, State.ON_STOP_STOP):
            Clock.schedule_interval(self.on_stop, SECOND_GAME)
            self.state = State.ON_STOP_START
            self.get_bike().anim_stop()

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
        return ValidObject.bike(self.parent.children[0]) if self.parent else None

    def get_rock(self):
        try:
            return ValidObject.rock(self.children[1])
        except IndexError as e:
            # todo:
            # print('[WARNING] the `Rock` item does not exist on the `Road`!')
            pass

    def get_finish(self):
        return ValidObject.finish(self.children[0])
