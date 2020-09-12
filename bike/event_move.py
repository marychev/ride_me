from kivy.clock import Clock
from kivy.properties import StringProperty

from bike.base_event import BaseBikeEvent
from bike.event_landing import EVENT_NAME as LANDING_EVENT_NAME
from conf import SECOND_GAME, WIDTH_GAME, HEIGHT_GAME
from utils.logs import Log

EVENT_NAME = 'on_move'


class MoveBikeEvent(BaseBikeEvent):
    current_event = StringProperty(EVENT_NAME)

    def __init__(self, **kwargs):
        self.register_event_type(EVENT_NAME)
        super(MoveBikeEvent, self).__init__(**kwargs)

    def has_leave_screen(self):
        return self.x + self.width > WIDTH_GAME or self.y > HEIGHT_GAME

    def can_move(self):
        Log.try_to_set(EVENT_NAME, self)
        prohibited_events = [LANDING_EVENT_NAME, ]
        can = (self.current_event not in prohibited_events) and not self.has_leave_screen()
        Log.can_or_not(EVENT_NAME, can, self)
        return can

    def set_move(self, dt):
        self.unschedule([self.on_landing, self.on_relax, self.on_stop, self.on_wait])

        self.acceleration = 4
        self.add_speed(self.acceleration)
        self.x += self.speed
        self._set_pos()

        self.pre_event = self.current_event
        self.current_event = EVENT_NAME

        self.collision_screen()

    def on_move(self, dt, *args):
        print('....on move.. ? ...')
        Log.start(EVENT_NAME, self)

        if self.can_move():
            self.unschedule([self.on_landing, self.on_relax, self.on_stop, self.on_wait])

            self.pre_event = self.current_event
            self.current_event = EVENT_NAME

            self.on_move = Clock.schedule_interval(self.set_move, SECOND_GAME)

    def collision_screen(self):
        if self.has_leave_screen():
            print('\n\t>> Collision <<\n\t')
            self.x -= 200
            self.speed = 0
            self.acceleration = 0
            self.on_wait()
