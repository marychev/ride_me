from kivy.clock import Clock

from conf import SECOND_GAME
from road.events.base import BaseDispatcher
from utils.state import State


class LandingDispatcher(BaseDispatcher):
    def __init__(self, **kwargs):
        super(LandingDispatcher, self).__init__(**kwargs)

        self.register_event_type(State.EVENT_ON_LANDING)
        self.set_game_object()

    def landing_start(self):
        Clock.schedule_interval(self.on_landing, SECOND_GAME)
        self.road.set_state(State.ON_LANDING_START)
        # todo: trouble with access to element
        self.bike and self.bike.anim_landing()

    def landing_stop(self):
        Clock.unschedule(self.on_landing)
        self.road.set_state(State.ON_LANDING_STOP)

    def on_landing(self, dt):
        # todo: only as temp solution
        if self.bike is None or self.road is None:
            self.set_game_object()
        else:
            if self.bike.is_in_sky():
                self.bike.y -= (dt * self.bike.power) * self.road.gravity
                self.bike.set_power(dt)

                # todo: need to move into start method
                # remove all animation (need to call one time)
                if self.road.state == State.ON_LANDING_START:
                    self.bike.anim_landing()

                self.road.set_state(State.ON_LANDING_MOVE)

                # todo: only as temp solution
                self.status_bar and self.status_bar.show_status('On Landing: ' + self.road.state, self.bike, self.road)
                return True
            else:
                self.bike.y = self.road.y
                self.bike.set_power(self.bike.max_power)

                self.road.set_state(State.ON_LANDING_STOP)

                # todo: AND has only as temp solution
                self.status_bar and self.status_bar.show_status('Stop On Landing: ' + self.road.state, self.bike, self.road)

                # check road state after loop and apply needed event
                # e.g. pass managing elements to other events
                if self.bike.speed <= 0:
                    self.road.wait_start()
                else:
                    self.road.on_relax_start()

                return False
