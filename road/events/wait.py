from kivy.clock import Clock

from conf import SECOND_GAME
from road.events.base import BaseDispatcher
from utils.state import State


class WaitDispatcher(BaseDispatcher):

    def __init__(self, **kwargs):
        super(WaitDispatcher, self).__init__(**kwargs)
        self.register_event_type(State.EVENT_ON_WAIT)

    @classmethod
    def start_states_list(cls):
        return (
            State.ON_STOP_STOP,
            State.ON_LANDING_STOP,
            State.ON_RELAX_STOP)

    @classmethod
    def stop_states_list(cls):
        return (State.ON_WAIT_START, State.ON_WAIT_MOVE, State.ON_WAIT_STOP,
                # State.ON_GO_MOVE
                )

    def wait_start(self):
        print('wait_start')
        if self.road.state in WaitDispatcher.start_states_list():
            print('+ wait_start')
            Clock.schedule_interval(self.on_wait, SECOND_GAME)
            self.road.set_state(State.ON_WAIT_START)
            self.bike.anim_wait()

            background = self.road.get_background()
            background.go_mountains_stop()

    def wait_stop(self):
        print('wait_stop => ', self.road.state)
        if self.bike.power >= self.bike.max_power or self.road.state in WaitDispatcher.stop_states_list():
            print('+ wait_stop')
            Clock.unschedule(self.on_wait)
            self.road.set_state(State.ON_WAIT_STOP)

    def on_wait(self, dt):
        # print('on_wait', 'state: {}'.format(self.road.state))
        if self.bike.speed <= 0 and self.bike.power < self.bike.max_power and not self.bike.is_in_sky():
            # print('+ on_wait')
            self.bike.speed = 0
            self.bike.power += dt*20
            self.road.set_state(State.ON_WAIT_MOVE)
            return True

        else:
            self.wait_stop()
            return False
