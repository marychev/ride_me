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
        print('>> SET RELAX', dt)
        if self.can_relax():
            speed_up = -dt * 8
            self.add_speed(speed_up)
            self.x += self.speed
            self._set_pos()

            self.pre_event = self.current_event
            self.current_event = EVENT_NAME
        else:
            # # define reason for why can't relax
            # print('???? WHY NOT RELAX? --> ', self.loop_event.get_callback().__name__)
            # if '_set_relax' in self.loop_event.get_callback().__name__:
            #     self.handle_speed_ended()
            # elif '_set_go' in self.loop_event.get_callback().__name__:
            #     self.handle_speed_ended()
            # elif '_set_wait' in self.loop_event.get_callback().__name__:
            #     self.handle_speed_ended()
            # else:
            #     print(self.show_status('<== WHY NOT RELAX .....'))
            #     raise ValueError('WHY NOT RELAX!')
            print('???? WHY NOT Relax?', self.loop_event.get_callback().__name__)

    def on_relax(self, dt):
        Log.start(EVENT_NAME, self)

        # handling on_go event
        if '_set_go' in self.loop_event.get_callback().__name__:
            self.loop_event.cancel()
            # that bike can move when speed == 0
            self.speed += dt

            if self.can_relax() and dt:
                # static values
                self.pre_event = self.current_event
                self.current_event = EVENT_NAME
                self.loop_event = Clock.schedule_interval(self._set_relax, SECOND_GAME)
            else:
                raise 0

        else:
            print(self.show_status('!!!!!!!!!!!!!!!!!!!'))
            print(self.loop_event.get_callback().__name__)
            # raise ValueError('*** ELSE ON_RELAX ... ***')

    def handle_speed_ended(self):
        if self.speed <= 0:
            print('[x] The speed has ended!')
            self.speed = 0
            self.loop_event.cancel()
            self.on_wait()
        else:
            raise ValueError('[x] The speed has ended! WHY NOT RELAX!')