from kivy.clock import Clock
from kivy.properties import StringProperty

from bike.event_base import BaseBikeEvent
from bike.event_landing import EVENT_NAME as LANDING_EVENT_NAME
from conf import SECOND_GAME, WIDTH_GAME, HEIGHT_GAME
from utils.logs import Log

EVENT_NAME = 'on_motion'


class MoveBikeEvent(BaseBikeEvent):
    def __init__(self, **kwargs):
        self.register_event_type(EVENT_NAME)
        super(MoveBikeEvent, self).__init__(**kwargs)

        if self.can_move():
            self.available_events.append(EVENT_NAME)

    def can_move(self):
        Log.try_to_set(EVENT_NAME, self)
        prohibited_events = [LANDING_EVENT_NAME, ]
        can = (
            (self.current_event not in prohibited_events)
            and not self.has_leave_screen()
            and (self.acceleration > 0)
        )
        Log.can_or_not(EVENT_NAME, can, self)
        return can

    def _set_move(self, dt):
        print('!!!!!!!!!!!!!!!!')
        print('_  set move --', dt)
        print(self)
        if self.can_move() and dt:
            speed_up = dt * 20
            self.add_speed(speed_up)
            self.acceleration -= speed_up

            self.x += self.speed
            self._set_pos()
            self.pre_event = self.current_event
            self.current_event = EVENT_NAME

            self.collision_screen()
            # if self.acceleration <= 0:
            #     self.loop_event.cancel()
            return True
        else:
            self.loop_event.cancel()
            # Clock.unschedule(self.on_move)
            return False

    def on_motion(self, dt):
        Log.start(EVENT_NAME, self)

        print(self.show_status())

        self.acceleration = dt
        if self.can_move():
            # self.loop_event.cancel()

            # static values
            self.acceleration = 20
            self.pre_event = self.current_event
            self.current_event = EVENT_NAME
            print('*****************')
            self.loop_event = Clock.schedule_interval(self._set_move, SECOND_GAME)
            print('////////////////////')

            self.collision_screen()

    def has_leave_screen(self):
        return self.x + self.width > WIDTH_GAME or self.y > HEIGHT_GAME

    def collision_screen(self):
        if self.has_leave_screen():
            print('\n\t>> Collision <<\n\t')
            self.x -= 200

            self.loop_event.cancel()
            self.on_wait(0.1)

