from kivy.clock import Clock
from conf import SECOND_GAME
from road.events.base import BaseDispatcher
from utils.state import State


class StopDispatcher(BaseDispatcher):

    def __init__(self, **kwargs):
        super(StopDispatcher, self).__init__(**kwargs)
        self.register_event_type(State.EVENT_ON_STOP)

    @classmethod
    def bun_event(cls):
        return (
            State.ON_GO_START, State.ON_GO_MOVE,
            State.ON_RELAX_START, State.ON_RELAX_MOVE)

    @classmethod
    def start_states_list(cls):
        return State.ON_RELAX_MOVE, State.ON_RELAX_STOP

    @classmethod
    def stop_states_list(cls):
        return State.ON_STOP_START, State.ON_STOP_MOVE

    def stop_start(self):
        print('stop_start')
        if self.road.state in StopDispatcher.start_states_list():
            Clock.schedule_interval(self.on_stop, SECOND_GAME)
            self.road.set_state(State.ON_STOP_START)
            self.bike.anim_stop()

    def stop_stop(self):
        print('stop_stop => ', self.road.state,  self.road.state in StopDispatcher.stop_states_list())
        if self.road.state in StopDispatcher.stop_states_list():

            # Clock.unschedule(self.on_stop)
            if hasattr(self.on_stop, 'cancel'):
                self.on_stop.cancel()

            self.road.set_state(State.ON_STOP_STOP)

            # check road state after loop and apply needed event
            # e.g. pass managing elements to other events
            if self.bike.speed <= 0:
                self.road.wait_start()
            else:
                self.road.relax_start()

    def on_stop(self, dt):
        print('on_stop')
        stop_way = dt * 12

        if self.bike.on_collision_rock():
            self.road.set_state(State.ON_STOP_STOP)
            return False

        if (float(self.bike.speed) - float(stop_way) <= 0.0) or (self.bike.speed <= 0)\
                and not self.bike.is_in_sky():
            self.bike.set_speed(0)
            self.road.stop_stop()
            return False

        elif self.bike.is_in_sky() or self.road.state in StopDispatcher.bun_event():
            return False

        else:
            self.bike.on_collision_puddle()
            self.bike.on_collision_currency()

            self.bike.set_speed(self.bike.speed - stop_way)
            self.set_distances()

            self.road.set_state(State.ON_STOP_MOVE)
            return True
