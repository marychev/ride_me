from kivy.clock import Clock
from kivy.properties import StringProperty
from bike.base import BaseBikeEvent
from bike.event_landing import EVENT_NAME as LANDING_EVENT_NAME
from conf import SECOND_GAME, WIDTH_GAME, HEIGHT_GAME
from utils.logs import Log


EVENT_NAME = 'on_move'


class MoveBikeEvent(BaseBikeEvent):
    current_event = StringProperty(EVENT_NAME)

    def has_leave_screen(self):
        return self.x > WIDTH_GAME or self.y > HEIGHT_GAME

    def can_move(self):
        Log.try_to_set(EVENT_NAME, self)
        prohibited_events = [LANDING_EVENT_NAME, ]
        can = (self.current_event not in prohibited_events) and not self.has_leave_screen()
        Log.can_or_not(EVENT_NAME, can, self)
        return can

    def set_move(self, dt):
        if self.can_move():
            BaseBikeEvent.unschedule([self.on_landing, self.on_relax, self.on_stop])

            self.x += self.speed
            self.add_speed(self.acceleration)
            self._set_pos()

        self.collision_screen()

    def move(self):
        Log.start(EVENT_NAME, self)

        if self.can_move():
            BaseBikeEvent.unschedule([self.on_landing, self.on_relax, self.on_stop])

            self.acceleration = 0.2
            self.pre_event = self.current_event
            self.current_event = EVENT_NAME
            self.on_move = Clock.schedule_interval(self.set_move, SECOND_GAME)

    def collision_screen(self):
        if self.has_leave_screen():
            print('>> Collision <<')
            self.x = WIDTH_GAME - self.width
            self.speed = 0
            self.acceleration = 0

            # self.unschedule_all_events()
