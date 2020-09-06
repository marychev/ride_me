from kivy.clock import Clock
from kivy.properties import StringProperty
from bike.base import BaseBikeEvent
from conf import SECOND_GAME


class MoveBikeEvent(BaseBikeEvent):
    current_event = StringProperty('on_move')

    def set_move(self, dt):
        print('... set move ...', self.current_event, self.speed)
        BaseBikeEvent.unschedule([self.on_landing, self.on_relax, self.on_stop])

        self.x += self.speed
        self.add_speed(self.acceleration)
        self._set_pos()

    def move(self):
        print('MOVE', self.current_event)
        if self.current_event not in ['on_landing', 'on_relax']:
            BaseBikeEvent.unschedule([self.on_landing, self.on_relax, self.on_stop])

            self.acceleration = 0.2
            self.current_event = 'on_move'
            self.on_move = Clock.schedule_interval(self.set_move, SECOND_GAME)

