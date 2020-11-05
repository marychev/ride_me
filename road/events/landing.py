from kivy.event import EventDispatcher
from utils.state import State
from label.status_bar import StatusBar


class LandingDispatcher(EventDispatcher):
    def __init__(self, **kwargs):
        super(LandingDispatcher, self).__init__(**kwargs)

        self.register_event_type(State.EVENT_ON_LANDING)
        self.set_game_object()

    def on_landing(self, dt):
        # todo: only as temp solution
        if self.bike is None or self.road is None:
            self.set_game_object()
        else:
            if self.bike.is_in_sky():
                self.bike.y -= (dt * self.bike.power) * self.road.gravity
                self.bike.set_power(dt)
                self.road.set_state(State.ON_LANDING_MOVE)
                self.bike.anim_landing()

                # todo: only as temp solution
                self.status_bar and self.status_bar.show_status('On Landing: ' + self.road.state, self.bike, self.road)
                return True
            else:
                self.bike.y = self.road.y
                self.bike.power = self.bike.max_power

                self.road.set_state(State.ON_LANDING_STOP)

                # todo: only as temp solution
                self.status_bar and self.status_bar.show_status('Stop On Landing: ' + self.road.state, self.bike, self.road)

                # check road state after loop and apply needed event
                if self.bike.speed <= 0:
                    self.road.on_wait_start()
                else:
                    self.road.on_relax_start()

                return False

    def set_game_object(self):
        # todo: only as temp solution
        self.status_bar = self.get_status_bar() or StatusBar.get_status_bar()
        self.road = self.get_road() or self.status_bar and self.status_bar.get_road()
        self.bike = self.get_bike() or self.status_bar and self.status_bar.get_bike()
