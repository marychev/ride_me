from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import NumericProperty, ObjectProperty, ListProperty, OptionProperty
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from label.status_bar import StatusBar
from layout.background_image import BackgroundImageAnimation
from road.events import GoEventRoad, RelaxEventRoad, StopEventRoad, JumpEventRoad, WaitEventRoad
from utils.checks import set_texture_uvpos
from conf import SECOND_GAME
from utils.validation import ValidObject
from utils.state import State

Builder.load_file("road/road.kv")


class Road(Widget):

    texture = ObjectProperty(Image(source='road/img/road-01.png').texture)
    total_way = NumericProperty(3000)
    distance_traveled = NumericProperty(0)
    gravity = NumericProperty(2)
    state = OptionProperty(State.NONE, options=State.list_states())
    last_states = ListProperty()

    def __init__(self, **kwargs):
        super(Road, self).__init__(**kwargs)
        BackgroundImageAnimation.repeat_wrap(self.texture, Window.width / self.texture.width)
        self.on_landing_start()

        self.register_event_type(State.EVENT_ON_WAIT)
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
    # -- on wait --
    def on_wait(self, dt):
        event = WaitEventRoad(**self.game_objects())
        status_bar = self.get_status_bar()
        bike = self.get_bike()

        if event.start(dt):
            status_bar.show_status('On Wait: ' + self.state, bike, self)
            return True
        else:
            self.on_wait_stop()
            status_bar.show_status('Stop On Wait: ' + self.state, bike, self)
            return False

    def on_wait_start(self):
        print('wait', self.state)
        if self.state in (State.NONE, State.ON_RELAX_STOP, State.ON_STOP_STOP, State.ON_JUMP_LANDING_STOP):
            Clock.schedule_interval(self.on_wait, SECOND_GAME)

            self.set_state(State.NONE)
            self.get_bike().anim_wait()
        else:
            print('\nXXX xx x .  wait  . x xx XXX\n', self.state)

    def on_wait_stop(self):
        print('-- wait stop')
        if self.state in (State.ON_GO_START, State.ON_JUMP_LANDING):
            Clock.unschedule(self.on_wait)
        else:
            print('\nXXX xx x .  wait stop . x xx XXX\n', self.state)

    # -- on landing --

    def on_landing(self, dt):
        event = JumpEventRoad(**self.game_objects())
        status_bar = self.get_status_bar()
        bike = self.get_bike()

        if event.landing(dt):
            status_bar.show_status('On Landing: ' + self.state, bike, self)
            return True
        else:
            self.on_landing_stop()
            status_bar.show_status('Stop On Landing: ' + self.state, bike, self)
            return False

    def on_landing_start(self):
        bike = self.get_bike()

        if self.state in State.available_states_landing():
            Clock.schedule_interval(self.on_landing, SECOND_GAME)

            self.set_state(State.ON_JUMP_LANDING)
            bike and bike.anim_landing()
        else:
            self.on_landing_stop()
            print('\nXXX xx x .  landing  . x xx XXX\n', self.state)

    def on_landing_stop(self):
        if self.state == State.ON_JUMP_LANDING:
            Clock.unschedule(self.on_landing)
            self.on_relax_start()
            self.set_state(State.ON_JUMP_LANDING_STOP)
            # move >> self.get_bike().anim_relax()
        elif self.get_bike().speed <= 0:
            self.on_wait_start()
            # move >> self.get_bike().anim_wait()

    # -- on jump up --

    def on_jump(self, dt):
        event = JumpEventRoad(**self.game_objects())
        status_bar = self.get_status_bar()
        bike = self.get_bike()

        if event.do(dt):
            status_bar.show_status('On Jump: ' + self.state, bike, self)
            return True
        else:
            self.on_jump_stop()
            self.on_landing_start()
            status_bar.show_status('Stop On Jump: ' + self.state, bike, self)
            return False

    def on_jump_start(self):
        if self.state in State.available_states_jump():
            Clock.schedule_interval(self.on_jump, SECOND_GAME)

            self.set_state(State.ON_JUMP_START)
            self.get_bike().anim_jump_up()
        else:
            # if self.get_bike().speed <= 0:
            #     self.on_wait_start()
            #     self.get_bike().anim_wait()
            print('\nXXX xx x .  jump  . x xx XXX\n')

    def on_jump_stop(self):
        if self.state == State.ON_JUMP_UP_MOVE:
            # self.get_bike().anim_relax()
            Clock.unschedule(self.on_jump)

    # -- on go --

    def on_go(self, dt):
        event = GoEventRoad(**self.game_objects())
        status_bar = self.get_status_bar()
        bike = self.get_bike()

        if event.do(dt):
            status_bar.show_status('On Go: ' + self.state, bike, self)
            return True
        elif self.has_finished():
            status_bar.show_status_finished()
            self.unschedule_events()
            return False
        else:
            self.on_go_stop()
            status_bar.show_status('STOP On Go: ' + self.state, bike, self)
            return False

    def on_go_start(self):
        if self.state in State.available_states_go():
            Clock.schedule_interval(self.on_go, SECOND_GAME)

            self.set_state(State.ON_GO_START)
            self.get_bike().anim_go()
        else:
            if self.get_bike().speed <= 0:
                self.on_wait_start()
                # self.get_bike().anim_wait()
            print('\nXXX xx x .  go  . x xx XXX\n', self.state)

    def on_go_stop(self):
        if self.state in (State.ON_GO_MOVE, State.ON_GO_START):
            # self.get_bike().anim_relax()
            Clock.unschedule(self.on_go)
            self.set_state(State.ON_GO_STOP)

    # -- on relax --

    def on_relax(self, acceleration):
        print('On Relax', self.state, self.last_states)
        event = RelaxEventRoad(**self.game_objects())
        bike = self.get_bike()
        status_bar = self.get_status_bar()

        if event.do(acceleration):
            status_bar.show_status('On Relax: ' + self.state, bike, self)
            return True
        elif self.has_finished():
            status_bar.show_status_finished()
            self.unschedule_events()
            return False
        else:
            self.on_relax_stop()
            status_bar.show_status('Stop On Relax: ' + self.state, bike, self)
            return False

    def on_relax_start(self):
        print(self.state, '<<<<<<<<<<,')
        if self.state in State.available_states_relax():
            Clock.schedule_interval(self.on_relax, SECOND_GAME)
            self.set_state(State.ON_RELAX_START)
            self.get_bike().anim_relax()
        else:
            print('\nXXX xx x .  relax start  . x xx XXX\n', self.state)

    def on_relax_stop(self):
        print('III', self.state)
        if self.state == State.ON_RELAX_MOVE:
            Clock.unschedule(self.on_relax)
            self.get_bike().anim_wait()
        else:
            self.on_wait_start()
            self.get_bike().anim_wait()
            print('\nXXX xx x .  relax stop  . x xx XXX\n', self.state)

    # -- on stop --

    def on_stop(self, acceleration):
        event = StopEventRoad(**self.game_objects())
        status_bar = self.get_status_bar()
        bike = self.get_bike()

        if event.start(acceleration):
            status_bar.show_status('On Stop: ' + self.state, bike, self)
            return True
        elif self.has_finished():
            status_bar.show_status_finished()
            return False
        else:
            status_bar.show_status('Stop On Stop: ' + self.state, bike, self)
            self.on_stop_stop()
            return False

    def on_stop_start(self):
        if self.state in State.available_states_stop():
            Clock.schedule_interval(self.on_stop, SECOND_GAME)
            self.set_state(State.ON_STOP_START)
            self.get_bike().anim_stop()

    def on_stop_stop(self):
        if self.state in (State.ON_STOP_START, State.ON_STOP_MOVE):
            Clock.unschedule(self.on_stop)
            self.on_wait_start()

    def unschedule_events(self):
        bg_animation = StatusBar.get_background_image_animation()
        self.on_jump_stop()
        self.on_go_stop()
        self.on_relax_stop()
        bg_animation.go_mountains_stop()
        bg_animation.relax_mountains_stop()
        self.on_wait_start()

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

    # get game objects

    def game_objects(self):
        return {
            'status_bar': self.get_status_bar(),
            'road': self,
            'bike': self.get_bike(),
            'rock': self.get_rock(),
            'finish': self.get_finish()}

    def get_status_bar(self):
        return ValidObject.status_bar(self.parent.children[2])

    def get_tools(self):
        return ValidObject.tools(self.parent.parent.children[0])

    def get_bike(self):
        return self.parent and ValidObject.bike(self.parent.children[0])  # if self.parent else StatusBar.get_bike()

    def get_rock(self):
        try:
            if len(self.children) > 1:
                return ValidObject.rock(self.children[1])
        except IndexError as e:
            print('[EXCEPT] the `Rock` item does not exist on the `Road`!')

    def get_finish(self):
        return ValidObject.finish(self.children[0])
