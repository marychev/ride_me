from kivy.clock import Clock

from bike.event_base import BaseBikeEvent
from conf import SECOND_GAME
from utils.logs import Log

EVENT_NAME = 'on_wait'


class WaitBikeEvent(BaseBikeEvent):
    def __init__(self, **kwargs):
        self.register_event_type(EVENT_NAME)
        super(WaitBikeEvent, self).__init__(**kwargs)

    def can_wait(self):
        Log.try_to_set(EVENT_NAME, self)
        # it is on the land
        can = self.road_pos.y >= self.y
        Log.can_or_not(EVENT_NAME, can, self)
        return can

    def _set_wait(self, dt):
        print('SET WAIT', dt)
        self.speed = 0
        self.acceleration = 0
        self.pre_event = self.current_event
        self.current_event = EVENT_NAME

        # if self.pre_event == self.current_event and self.speed == 0:
        #     self.on_wait.cancel()

    def on_wait(self):
        Log.start(EVENT_NAME, self)
        if self.can_wait():
            self.loop_event = Clock.schedule_once(self._set_wait, SECOND_GAME)
            print('\n\tWaiting for some actions!!!\n\t------------------------------')

