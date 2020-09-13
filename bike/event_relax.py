from kivy.clock import Clock
from kivy.properties import StringProperty
from bike.event_base import BaseBikeEvent
from bike.event_landing import EVENT_NAME as LANDING_EVENT_NAME
from conf import SECOND_GAME, WIDTH_GAME
from utils.logs import Log


EVENT_NAME = 'on_relax'


class RelaxBikeEvent(BaseBikeEvent):
    def __init__(self, **kwargs):
        self.register_event_type(EVENT_NAME)
        super(RelaxBikeEvent, self).__init__(**kwargs)

        if self.can_relax():
            self.available_events.append(EVENT_NAME)

    def can_relax(self):
        Log.try_to_set(EVENT_NAME, self)
        prohibited_events = [LANDING_EVENT_NAME, ]
        leave_screen_x = self.x > WIDTH_GAME
        can = (
                (self.current_event not in prohibited_events)
                and not leave_screen_x
                and self.speed > 0
        )
        Log.can_or_not(EVENT_NAME, can, self)
        return can

    def _set_relax(self, dt):
        print('- -  set relax - -', dt)

        Clock.unschedule(self.on_motion)

        if self.can_relax():
            print('>> SET RELAX', dt)
            speed_up = -dt
            self.add_speed(speed_up)

            self.x += self.speed
            self._set_pos()

            self.pre_event = self.current_event
            self.current_event = EVENT_NAME

            # if self.speed <= 0:
            #     Clock.unschedule(self.on_relax)
            #     self.on_wait(0)

            return True
        else:
            self.loop_event.cancel()
            return False

    def on_relax(self, dt, *args):
        Log.start(EVENT_NAME, self)

        self.speed = dt
        if self.can_relax() and dt:
            self.loop_event.cancel()
            Clock.unschedule(self.on_motion)

            # static values
            self.pre_event = self.current_event
            self.current_event = EVENT_NAME
            self.loop_event = Clock.schedule_interval(self._set_relax, SECOND_GAME)



