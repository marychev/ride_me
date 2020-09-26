from kivy.clock import Clock
from kivy.properties import StringProperty, ObjectProperty

from bike.event_base import BaseBikeEvent
from bike.event_landing import EVENT_NAME as LANDING_EVENT_NAME
from conf import SECOND_GAME, WIDTH_GAME, HEIGHT_GAME
from utils.logs import Log

EVENT_NAME = 'on_go'


class MoveBikeEvent(BaseBikeEvent):
    on_go_clock = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(MoveBikeEvent, self).__init__(**kwargs)

        if self.can_go():
            self.register_event_type(EVENT_NAME)
            self.available_events.append(EVENT_NAME)

    def can_go(self):
        # Log.try_to_set(EVENT_NAME, self)
        prohibited_events = [LANDING_EVENT_NAME, ]
        can = (
            (self.current_event not in prohibited_events)
            and not self.has_leave_screen()
            # and self.acceleration > 0
            # and self.speed >= 0
        )
        Log.can_or_not(EVENT_NAME, can, self)
        return can

    def _set_go(self, dt):
        if dt > 0 and self.speed > 0:
            print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>', self.speed)
            self.add_speed(dt)
            self._set_pos()

            self.acceleration -= dt
            self.pre_event = self.current_event
            self.current_event = EVENT_NAME

            self.collision_screen()
        else:
            self.on_go_clock.cancel()
            return False

    def on_go(self):
        Log.start(EVENT_NAME, self)

        if self.speed == 0:
            self.speed = SECOND_GAME

        if self.can_go():
            self.collision_screen()
            self.on_go_clock = Clock.schedule_interval(self._set_go, SECOND_GAME)
        else:
            print('******* GO ********')
            raise 1

    def has_leave_screen(self):
        return self.x + self.width > WIDTH_GAME or self.y > HEIGHT_GAME

    def collision_screen(self):
        if self.has_leave_screen():
            print('\n\t>> Collision <<\n\t')
            self.x -= 200

            Clock.unschedule(self.on_go)
            self.on_wait()

