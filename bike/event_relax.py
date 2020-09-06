from kivy.clock import Clock
from kivy.properties import StringProperty
from bike.base import BaseBikeEvent
from bike.event_stop import StopBikeEvent
from conf import SECOND_GAME


class RelaxBikeEvent(StopBikeEvent):
    current_event = StringProperty('on_relax')

    def set_relax(self, dt):
        print('... set relax ...', self.current_event)
        BaseBikeEvent.unschedule([self.on_landing, self.on_move, self.on_stop])

        self.x += self.speed
        self.add_speed(-self.acceleration)

        if self.speed <= 0:
            Clock.unschedule(self.on_relax)
            self.stop()

        self._set_pos()

    def relax(self):
        print('RELAX')
        if self.current_event not in ['on_landing', ]:

            BaseBikeEvent.unschedule([self.on_landing, self.on_move, self.on_stop])

            self.acceleration = 0.01
            self.current_event = 'on_relax'
            self.on_relax = Clock.schedule_interval(self.set_relax, SECOND_GAME)

