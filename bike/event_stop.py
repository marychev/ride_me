from kivy.clock import Clock
from kivy.properties import StringProperty
from bike.base import BaseBikeEvent
from conf import SECOND_GAME


class StopBikeEvent(BaseBikeEvent):
    current_event = StringProperty('on_stop')

    def set_stop(self, dt):
        print('... set stop ...', self.current_event)
        BaseBikeEvent.unschedule([self.on_landing, self.on_relax, self.on_move])

        self.x += self.speed
        self.add_speed(-self.acceleration)
        self._set_pos()

        if self.speed <= 0:
            Clock.unschedule(self.on_stop)

    def stop(self):
        BaseBikeEvent.unschedule([self.on_landing, self.on_relax, self.on_move])

        self.speed = 0
        self.acceleration = 0.05
        self.current_event = 'on_stop'
        self.on_stop = Clock.schedule_interval(self.set_stop, SECOND_GAME)
