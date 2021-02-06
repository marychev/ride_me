from kivy.clock import Clock
from conf import SECOND_GAME
from road.events.base import BaseDispatcher
from utils.state import State
from utils.get_object import GetObject


class GoDispatcher(BaseDispatcher):

    def __init__(self, **kwargs):
        self.register_event_type(State.EVENT_ON_GO)
        super(GoDispatcher, self).__init__(**kwargs)

    @classmethod
    def ban_events(cls):
        return (
            State.ON_JUMP_START, State.ON_JUMP_MOVE, State.ON_JUMP_STOP,
            State.ON_LANDING_START, State.ON_LANDING_MOVE, State.ON_LANDING_STOP,
            State.ON_STOP_MOVE,
            State.ON_WAIT_START,
        )

    @classmethod
    def start_states_list(cls):
        return (
            State.ON_WAIT_MOVE,
            State.ON_WAIT_STOP,
            State.ON_RELAX_START, State.ON_RELAX_MOVE, State.ON_RELAX_STOP,
        )

    @classmethod
    def stop_states_list(cls):
        return State.ON_GO_START, State.ON_GO_MOVE, State.ON_GO_STOP

    def go_start(self):
        print('go_start')
        curtain = GetObject(self.road).curtain

        # todo: It was fixed for tests. It was checked by logs
        if State.ON_WAIT_MOVE in self.road.last_states:
            if hasattr(self.road.on_wait, 'cancel'):
                self.road.on_wait.cancel()

        if curtain.text == '' and not self.bike.is_in_sky() and self.road.state in GoDispatcher.start_states_list():
            Clock.schedule_interval(self.on_go, SECOND_GAME)
            self.road.set_state(State.ON_GO_START)
            self.bike.anim_go()

    def go_stop(self):
        print('go_stop')
        if self.road.state in GoDispatcher.stop_states_list():
            # todo: fix actions: go->relax->go
            Clock.unschedule(self.on_go)
            # if hasattr(self.on_go, 'cancel'):
            #     self.on_go.cancel()

            self.road.set_state(State.ON_GO_STOP)

            background = self.road.get_background()
            background and background.go_mountains_stop()

    def on_go(self, dt):
        print('on_go', 'state:{}'.format(self.road.state))
        if self.bike.on_collision_rock():
            self.go_stop()
            return False

        if self.road.has_finished():
            self.go_stop()
            self.road_finish()
            return False

        elif self.bike.is_in_sky():
            return False

        elif self.road.state in self.ban_events():
            self.go_stop()
            return False

        else:
            self.bike.on_collision_puddle()
            self.bike.on_collision_currency()

            val = dt * (self.bike.power + self.bike.acceleration)
            self.bike.acceleration = self.bike.power / 100
            self.bike.set_power(self.bike.power - val)
            if self.bike.speed < self.bike.max_speed:
                self.bike.set_speed(self.bike.speed + val)

            self.set_distances()
            self.road.set_state(State.ON_GO_MOVE)
            return True
