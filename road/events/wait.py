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
        return (State.ON_LANDING_STOP,
                State.ON_RELAX_STOP)

    @classmethod
    def stop_states_list(cls):
        return (State.ON_WAIT_START, State.ON_WAIT_MOVE, State.ON_WAIT_STOP,
                # fix test_wait
                State.ON_LANDING_STOP)

    def wait_start(self):
        if self.road.state in WaitDispatcher.start_states_list():
            Clock.schedule_interval(self.on_wait, SECOND_GAME)
            self.road.set_state(State.ON_WAIT_START)
            self.bike.anim_wait()

    def wait_stop(self):
        if self.road.state in WaitDispatcher.stop_states_list():
            Clock.unschedule(self.on_wait)
            self.road.set_state(State.ON_WAIT_STOP)

    def on_wait(self, dt):

        if self.bike.speed <= 0 and self.bike.power < self.bike.max_power and not self.bike.is_in_sky():
            self.bike.speed = 0
            self.bike.power += dt*10
            self.road.set_state(State.ON_WAIT_MOVE)
            # todo: fix test landing
            self.status_bar and self.status_bar.show_status('On Wait: ' + self.road.state, self.bike, self.road)
            return True
        else:
            self.wait_stop()
            # todo: fix test landing
            self.status_bar and self.status_bar.show_status('Stop On Wait: ' + self.road.state, self.bike, self.road)
            return False
