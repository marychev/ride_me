from kivy.clock import Clock
from kivy.properties import StringProperty, ObjectProperty
from bike.event_base import BaseBikeEvent
from bike.event_landing import EVENT_NAME as LANDING_EVENT_NAME
from conf import SECOND_GAME, WIDTH_GAME
from utils.logs import Log


EVENT_NAME = 'on_relax'


class RelaxBikeEvent(BaseBikeEvent):
    on_relax_clock = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(RelaxBikeEvent, self).__init__(**kwargs)

        if self.can_relax():
            self.register_event_type(EVENT_NAME)
            self.available_events.append(EVENT_NAME)

    def can_relax(self):
        # Log.try_to_set(EVENT_NAME, self)
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
        if dt > 0 and (self.speed > 0):
            print(' >> set relax <<', dt)
            self.add_speed(-dt)
            self._set_pos()

            self.pre_event = self.current_event
            self.current_event = EVENT_NAME
        else:
            self.on_relax_clock.cancel()
            return False

    def on_relax(self):
        Log.start(EVENT_NAME, self)
        if self.can_relax():
            self.on_relax_clock = Clock.schedule_interval(self._set_relax, SECOND_GAME)
        else:
            self.on_relax_clock.cancel()
            Clock.unschedule(self.on_relax)

            if self.speed <= 0:
                self.on_wait()

    def handle_speed_ended(self):
        if self.speed <= 0:
            print('[x] The speed has ended!')
            self.speed = 0
            self.loop_event.cancel()
            self.on_wait()
        else:
            print('[x] The speed has ended! WHY NOT RELAX!')
