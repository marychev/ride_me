from kivy.clock import Clock
from bike.event_base import BaseBikeEvent
from conf import SECOND_GAME
from utils.logs import Log


EVENT_NAME = 'on_landing'


class LandingBikeEvent(BaseBikeEvent):
    def __init__(self, **kwargs):
        self.register_event_type(EVENT_NAME)
        super(LandingBikeEvent, self).__init__(**kwargs)

        self.gravity = 0.2

    def can_landing(self):
        Log.try_to_set(EVENT_NAME, self)
        can = self.road_pos.y < self.y
        Log.can_or_not(EVENT_NAME, can, self)
        return can

    def _set_landing(self, dt):
        if self.can_landing():
            self.y -= self.speed
            self.add_speed(self.gravity)
            self._set_pos()
            self.pre_event = self.current_event
            self.current_event = EVENT_NAME
        else:
            self.current_event = '{}-cancel'.format(self.current_event)
            self.loop_event.cancel()

        self.collision_with_land()

    def on_landing(self):
        Log.start(EVENT_NAME, self)
        # todo: need set value for _set_landing
        self.loop_event = Clock.schedule_interval(self._set_landing, SECOND_GAME)
        self.collision_with_land()

    def has_collision_with_land(self):
        return self.road_pos.y >= self.y and self.current_event == EVENT_NAME

    def collision_with_land(self):
        if self.has_collision_with_land():
            print('\n\tContact with the land. BOOM!!!\n\t------------------------------')
            self.speed = 0
            self.current_event = '{}-collision'.format(self.current_event)
            self.loop_event.cancel()
