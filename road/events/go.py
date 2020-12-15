from kivy.clock import Clock
from conf import SECOND_GAME
from road.events.base import BaseDispatcher
from utils.state import State


class GoDispatcher(BaseDispatcher):

    def __init__(self, **kwargs):
        super(GoDispatcher, self).__init__(**kwargs)
        self.register_event_type(State.EVENT_ON_GO)

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
            State.ON_WAIT_MOVE, State.ON_WAIT_STOP,
            State.ON_RELAX_START, State.ON_RELAX_MOVE, State.ON_RELAX_STOP,
        )

    @classmethod
    def stop_states_list(cls):
        return State.ON_GO_START, State.ON_GO_MOVE, State.ON_GO_STOP

    def go_start(self):
        if not self.bike.is_in_sky() and self.road.state in GoDispatcher.start_states_list():
            Clock.schedule_interval(self.on_go, SECOND_GAME)
            self.road.set_state(State.ON_GO_START)
            self.bike.anim_go()

    def go_stop(self):
        if self.road.state in GoDispatcher.stop_states_list():
            Clock.unschedule(self.on_go)
            self.road.set_state(State.ON_GO_STOP)

    def on_go(self, dt):
        print('on_go\r')
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

            # print(dt, 'x', self.bike.power, '=', dt * self.bike.power)
            # dt:0.018203228000857052 x power:68.08209114200872 = 1.239313827833115
            N_1 = 1.5
            val = dt * float("{0:.1f}".format(self.bike.power)) / N_1
            print('---', val)

            if self.bike.speed < self.bike.max_speed:
                self.bike.speed += val
                # self.bike.set_power(-val)

            self.bike.power -= val

            self.set_distances()
            self.road.set_state(State.ON_GO_MOVE)
            return True
