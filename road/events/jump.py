from kivy.clock import Clock

from conf import SECOND_GAME
from road.events.base import BaseDispatcher
from utils.state import State


class JumpDispatcher(BaseDispatcher):

    def __init__(self, **kwargs):
        self.register_event_type(State.EVENT_ON_JUMP)
        super(JumpDispatcher, self).__init__(**kwargs)

    @classmethod
    def bun_events(cls):
        return (
            State.ON_LANDING_START, State.ON_LANDING_MOVE, State.ON_LANDING_STOP,
            State.ON_STOP_START, State.ON_STOP_MOVE, State.ON_STOP_STOP,
            State.ON_WAIT_START,
            State.ON_RELAX_MOVE
        )

    @classmethod
    def start_states_list(cls):
        return (
            State.ON_RELAX_MOVE, State.ON_RELAX_STOP,
            State.ON_WAIT_MOVE, State.ON_WAIT_STOP,
        )

    @classmethod
    def stop_states_list(cls):
        return State.ON_JUMP_START, State.ON_JUMP_MOVE, State.ON_JUMP_STOP

    def jump_start(self):
        print('jump_start')
        if int(self.bike.power) > 0 and self.road.state in JumpDispatcher.start_states_list():
            self.road.wait_stop()
            Clock.schedule_interval(self.on_jump, SECOND_GAME)
            self.road.set_state(State.ON_JUMP_START)
            self.bike.anim_jump_up()

            self.bike.acceleration = self.bike.power / self.road.gravity + self.bike.speed / self.road.gravity

    def jump_stop(self):
        print('jump_stop')
        if self.road.state in JumpDispatcher.stop_states_list():

            # Clock.unschedule(self.on_jump)
            if hasattr(self.on_jump, 'cancel'):
                self.on_jump.cancel()

            self.road.set_state(State.ON_JUMP_STOP)

    def on_jump(self, dt):
        print('on_jump', self.bike.y, self.bike.height)
        if self.road.state in self.bun_events():
            return False

        elif int(self.bike.power) > 0 \
                and self.road.state not in self.bun_events() \
                and (self.bike.y < self.bike.height * 3):
            self.bike.on_collision_currency()
            self.bike.y += self.get_bike_y_for_landing()

            self.set_bike_acceleration_for_landing(dt)
            self.bike.set_power(self.bike.power - (dt * self.road.gravity))
            self.bike.set_speed(self.bike.speed - (dt * self.road.gravity))

            self.road.set_state(State.ON_JUMP_MOVE)
            self.set_distances()
            return True

        else:
            self.jump_stop()
            self.road.landing_start()
            return False
