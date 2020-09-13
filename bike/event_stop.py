from kivy.clock import Clock
from kivy.properties import StringProperty

from bike.base_event import BaseBikeEvent
from bike.event_landing import EVENT_NAME as LANDING_EVENT_NAME
from conf import SECOND_GAME, WIDTH_GAME
from utils.logs import Log

EVENT_NAME = 'on_stop'


class StopBikeEvent(BaseBikeEvent):
    current_event = StringProperty(EVENT_NAME)

    def __init__(self, **kwargs):
        self.register_event_type(EVENT_NAME)
        super(StopBikeEvent, self).__init__(**kwargs)

    def can_stop(self):
        Log.try_to_set(EVENT_NAME, self)
        prohibited_events = [LANDING_EVENT_NAME, ]
        leave_screen_x = self.x > WIDTH_GAME
        can = (self.current_event not in prohibited_events) and not leave_screen_x

        Log.can_or_not(EVENT_NAME, can, self)
        return can

    def set_stop(self, dt):
        # self.on_move and self.on_move.cancel()

        if self.can_stop():
            self.unschedule([self.on_landing, self.on_relax, self.on_motion])

            self.x += self.speed
            self.add_speed(-self.acceleration)
            self._set_pos()

            if self.speed < 0:
                self.on_stop.cancel()
                self.wait()

    def on_stop(self):
        Log.start(EVENT_NAME, self)

        if self.can_stop():
            self.unschedule([self.on_landing, self.on_relax, self.on_motion])

            self.speed = 0
            self.acceleration = 0
            self.current_event = EVENT_NAME
            self.on_stop = Clock.schedule_interval(self.set_stop, SECOND_GAME)
