from kivy.clock import Clock
from kivy.properties import StringProperty

from bike.event_base import BaseBikeEvent
from bike.event_landing import EVENT_NAME as LANDING_EVENT_NAME
from conf import SECOND_GAME, WIDTH_GAME, HEIGHT_GAME
from utils.logs import Log

EVENT_NAME = 'on_go'


class MoveBikeEvent(BaseBikeEvent):
    def __init__(self, **kwargs):
        self.register_event_type(EVENT_NAME)
        super(MoveBikeEvent, self).__init__(**kwargs)

        if self.can_go():
            self.available_events.append(EVENT_NAME)

    def can_go(self):
        Log.try_to_set(EVENT_NAME, self)
        prohibited_events = [LANDING_EVENT_NAME, ]
        can = (
            (self.current_event not in prohibited_events)
            and not self.has_leave_screen()
            and (self.acceleration > 0)
        )
        Log.can_or_not(EVENT_NAME, can, self)
        return can

    def _set_go(self, dt):
        print(' -+- SET MOVE --', dt)
        if self.can_go() and dt:
            speed_up = dt * 20
            self.add_speed(speed_up)
            self.acceleration -= speed_up

            self.x += self.speed
            self._set_pos()
            self.pre_event = self.current_event
            self.current_event = EVENT_NAME

            self.collision_screen()
        else:
            print('???? WHY NOT GoGO?',  self.loop_event.get_callback().__name__)
            # if '_set_go' in self.loop_event.get_callback().__name__:
            #     if (self.acceleration <= 0) and (self.speed > 0):
            #         print('[x] The acceleration has ended!')
            #         self.acceleration = 0
            #         self.loop_event.cancel()
            #         self.dispatch('on_relax', dt)
            #     else:
            #         print(self.acceleration <= 0, self.speed > 0)
            # else:
            #     # print(self.show_status('<=== WHY NOT GoGO'))
            #     raise 0

    def on_go(self, dt):
        Log.start(EVENT_NAME, self)

        self.acceleration = dt
        if self.can_go():
            # static values
            self.acceleration = 8
            self.pre_event = self.current_event
            self.current_event = EVENT_NAME

            self.loop_event = Clock.schedule_interval(self._set_go, SECOND_GAME)
            self.collision_screen()
        else:
            print('*** ELSE WHY NOT ON_MOVING ... ***')
            # raise 0

    def has_leave_screen(self):
        return self.x + self.width > WIDTH_GAME or self.y > HEIGHT_GAME

    def collision_screen(self):
        if self.has_leave_screen():
            print('\n\t>> Collision <<\n\t')
            self.x -= 200
            # raise 0
            self.loop_event.cancel()
            self.on_wait()

