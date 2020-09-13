from kivy.clock import Clock

from bike.event_base import BaseBikeEvent
from conf import SECOND_GAME
from utils.logs import Log

EVENT_NAME = 'on_wait'


class WaitBikeEvent(BaseBikeEvent):
    def __init__(self, **kwargs):
        self.register_event_type(EVENT_NAME)
        super(WaitBikeEvent, self).__init__(**kwargs)

        if self.can_wait():
            self.available_events.append(EVENT_NAME)
            self.speed = 0

    def can_wait(self):
        Log.try_to_set(EVENT_NAME, self)
        # it is on the land
        can = self.road_pos.y >= self.y and self.speed == 0
        Log.can_or_not(EVENT_NAME, can, self)
        return can

    def _set_wait(self, dt):
        print('SET WAIT', dt)
        if self.can_wait():
            self.speed = 0
            self.acceleration = 0.001
            self.pre_event = self.current_event
            self.current_event = EVENT_NAME
        else:
            print('*** ELSE _SET_WAIT ***')

    def on_wait(self):
        Log.start(EVENT_NAME, self)
        if self.can_wait():
            self.speed = 0
            self.acceleration = 0.001
            self.pre_event = self.current_event
            self.current_event = EVENT_NAME

            self.define_available_events()

            self.loop_event = Clock.schedule_once(self._set_wait, SECOND_GAME)
            print('\n\tWaiting for some actions!!!\n\t------------------------------')
        else:
            print('*** ELSE ON_WAIT ***')
