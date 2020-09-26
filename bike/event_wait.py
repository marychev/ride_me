from kivy.clock import Clock

from bike.event_base import BaseBikeEvent
from conf import SECOND_GAME
from utils.logs import Log

EVENT_NAME = 'on_wait'


class WaitBikeEvent(BaseBikeEvent):
    def __init__(self, **kwargs):
        super(WaitBikeEvent, self).__init__(**kwargs)
        self.register_event_type(EVENT_NAME)

        if self.can_wait():
            self.available_events.append(EVENT_NAME)
            self.speed = 0

    def can_wait(self):
        # Log.try_to_set(EVENT_NAME, self)
        can = self.road_pos.y >= self.y
        Log.can_or_not(EVENT_NAME, can, self)
        return can

    def _set_wait(self, dt):
        self.speed = 0
        self.pre_event = self.current_event
        self.current_event = EVENT_NAME

    def on_wait(self):
        Log.start(EVENT_NAME, self)
        if self.can_wait():
            # self.define_available_events()
            self.on_wait_clock = Clock.schedule_once(self._set_wait)
            print('\n\tWaiting for some actions!!!\n\t------------------------------')
        else:
            self.on_wait_clock.cancel()
            return False
