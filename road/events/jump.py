from kivy.clock import Clock

from conf import SECOND_GAME
from road.events.base import BaseDispatcher
from utils.state import State


class JumpDispatcher(BaseDispatcher):

    def __init__(self, **kwargs):
        super(JumpDispatcher, self).__init__(**kwargs)
        self.register_event_type(State.EVENT_ON_JUMP)

    @classmethod
    def start_states_list(cls):
        return (State.ON_RELAX_STOP,
                State.ON_WAIT_MOVE, State.ON_WAIT_STOP)

    @classmethod
    def stop_states_list(cls):
        return State.ON_JUMP_START, State.ON_JUMP_MOVE, State.ON_JUMP_STOP

    def jump_start(self):
        if self.road.state in JumpDispatcher.start_states_list():
            self.road.wait_stop()
            Clock.schedule_interval(self.on_jump, SECOND_GAME)
            self.road.set_state(State.ON_JUMP_START)
            self.bike.anim_jump_up()

    def jump_stop(self):
        if self.road.state in JumpDispatcher.stop_states_list():
            Clock.unschedule(self.on_jump)
            self.road.set_state(State.ON_JUMP_STOP)

    def on_jump(self, dt):
        if int(self.bike.power) > 0 and self.road.state != State.ON_LANDING_MOVE:
            self.bike.y += dt * self.bike.power
            self.bike.set_power(-dt)

            self.road.set_state(State.ON_JUMP_MOVE)
            self.set_distances()
            self.status_bar and self.status_bar.show_status('On Jump: ' + self.road.state, self.bike, self.road)
            return True

        else:
            self.jump_stop()
            self.road.landing_start()
            self.status_bar and self.status_bar.show_status('Stop On Jump: ' + self.road.state, self.bike, self.road)
            return False
