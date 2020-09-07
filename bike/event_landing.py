from kivy.clock import Clock
from kivy.properties import NumericProperty, StringProperty

from bike.base import BaseBikeEvent
from bike.event_stop import StopBikeEvent
from conf import SECOND_GAME
from utils.logs import Log


EVENT_NAME = 'on_landing'
WAIT_EVENT_NAME = 'on_wait'


class LandingBikeEvent(StopBikeEvent):
    gravity = NumericProperty(0.2)
    current_event = StringProperty(EVENT_NAME)

    def can_landing(self):
        Log.try_to_set(EVENT_NAME, self)
        can = self.road_pos.y < self.y
        Log.can_or_not(EVENT_NAME, can, self)
        return can

    def set_landing(self, dt):
        BaseBikeEvent.unschedule([self.on_move, self.on_relax, self.on_stop])

        if self.can_landing():
            self.y -= self.speed
            self.add_speed(self.gravity)
            self._set_pos()

        # todo: contact with the land
        if self.road_pos.y > self.y and self.current_event == EVENT_NAME:
            print('\n\tContact with the land. BOOM!!!\n\t------------------------------')
            self.wait()

    def landing(self):
        Log.start(EVENT_NAME, self)
        if self.can_landing():
            BaseBikeEvent.unschedule([self.on_move, self.on_relax, self.on_stop])
            self.pre_event = self.current_event
            self.current_event = EVENT_NAME
            self.on_landing = Clock.schedule_interval(self.set_landing, SECOND_GAME)
