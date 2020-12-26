from kivy.clock import Clock

from conf import SECOND_GAME
from road.events.base import BaseDispatcher
from utils.state import State


class LandingDispatcher(BaseDispatcher):
    def __init__(self, **kwargs):
        super(LandingDispatcher, self).__init__(**kwargs)

        self.register_event_type(State.EVENT_ON_LANDING)
        self.set_game_object()

    @classmethod
    def start_states_list(cls):
        return (State.NONE,
                State.ON_WAIT_START,
                State.ON_JUMP_MOVE, State.ON_JUMP_STOP)

    @classmethod
    def stop_states_list(cls):
        return State.ON_LANDING_START, State.ON_LANDING_MOVE, State.ON_LANDING_STOP

    def landing_start(self):
        print('landing_start')
        if self.road.state in LandingDispatcher.start_states_list():
            Clock.schedule_interval(self.on_landing, SECOND_GAME)
            self.road.set_state(State.ON_LANDING_START)
            # todo: trouble with access to element
            self.bike and self.bike.anim_landing()

    def landing_stop(self):
        print('landing_stop')
        if self.road.state in LandingDispatcher.stop_states_list():
            Clock.unschedule(self.on_landing)
            self.road.set_state(State.ON_LANDING_STOP)

            # check road state after loop and apply needed event
            # e.g. pass managing elements to other events
            if self.bike.speed <= 0:
                self.road.wait_start()
            else:
                self.road.relax_start()

    def on_landing(self, dt):
        print('on_landing')
        # todo: only as temp solution fix speed loading page
        if self.road.state != State.ON_JUMP_MOVE:
            # todo: only as temp solution
            # maybe use self.get_bike()
            if self.bike is None or self.road is None:
                self.set_game_object()
            else:
                if self.bike.is_in_sky():

                    self.bike.acceleration = dt * self.road.gravity
                    self.bike.y -= self.bike.acceleration * self.bike.max_power / 4
                    self.bike.power += self.bike.acceleration

                    # todo: need to move into start method
                    # remove all animation (need to call one time)
                    if self.road.state == State.ON_LANDING_START:
                        self.bike.anim_landing()

                    self.road.set_state(State.ON_LANDING_MOVE)
                    self.set_distances()
                    return True

                else:
                    self.bike.y = self.road.line_points[-1]
                    self.landing_stop()
                    return False
