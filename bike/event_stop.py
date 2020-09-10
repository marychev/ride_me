from kivy.clock import Clock
from kivy.properties import StringProperty
from bike.base import BaseBikeEvent
from conf import SECOND_GAME, WIDTH_GAME
from utils.logs import Log

# ERR: from bike.event_landing import LANDING_EVENT_NAME
LANDING_EVENT_NAME = 'on_landing'
EVENT_NAME = 'on_stop'


class StopBikeEvent(BaseBikeEvent):
    current_event = StringProperty(EVENT_NAME)

    def can_stop(self):
        Log.try_to_set(EVENT_NAME, self)
        prohibited_events = [LANDING_EVENT_NAME, ]
        leave_screen_x = self.x > WIDTH_GAME
        can = (self.current_event not in prohibited_events) and not leave_screen_x

        Log.can_or_not(EVENT_NAME, can, self)
        return can

    def set_stop(self, dt):
        self.on_move.cancel()
        if self.can_stop():
            BaseBikeEvent.unschedule([self.on_landing, self.on_relax, self.on_move])

            self.x += self.speed
            self.add_speed(-self.acceleration)
            self._set_pos()

            if self.speed < 0:
                self.on_stop.cancel()
                self.wait()

    def stop(self):
        Log.start(EVENT_NAME, self)

        if self.can_stop():
            BaseBikeEvent.unschedule([self.on_landing, self.on_relax, self.on_move])

            self.speed = 0
            self.acceleration = 0
            self.current_event = EVENT_NAME
            self.on_stop = Clock.schedule_interval(self.set_stop, SECOND_GAME)
