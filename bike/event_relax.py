from kivy.clock import Clock
from kivy.properties import StringProperty
from bike.base import BaseBikeEvent
from bike.event_stop import StopBikeEvent
from bike.event_landing import EVENT_NAME as LANDING_EVENT_NAME
from conf import SECOND_GAME, WIDTH_GAME
from utils.logs import Log


EVENT_NAME = 'on_relax'


class RelaxBikeEvent(StopBikeEvent):
    current_event = StringProperty(EVENT_NAME)

    def can_relax(self):
        Log.try_to_set(EVENT_NAME, self)
        prohibited_events = [LANDING_EVENT_NAME, ]
        leave_screen_x = self.x > WIDTH_GAME
        can = (self.current_event not in prohibited_events) and not leave_screen_x

        Log.can_or_not(EVENT_NAME, can, self)
        return can

    def set_relax(self, dt):
        if self.can_relax():
            BaseBikeEvent.unschedule([self.on_landing, self.on_move, self.on_stop])

            self.x += self.speed
            self.add_speed(-self.acceleration)
            self._set_pos()

            if self.speed <= 0:
                Clock.unschedule(self.on_relax)
                self.stop()

    def relax(self):
        Log.start(EVENT_NAME, self)

        if self.can_relax():
            BaseBikeEvent.unschedule([self.on_landing, self.on_move, self.on_stop])

            self.acceleration = 0.01
            self.pre_event = self.current_event
            self.current_event = EVENT_NAME
            self.on_relax = Clock.schedule_interval(self.set_relax, SECOND_GAME)

