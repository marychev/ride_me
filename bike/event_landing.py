from kivy.clock import Clock
from kivy.properties import NumericProperty, StringProperty
from bike.base import BaseBikeEvent
from bike.event_stop import StopBikeEvent
from conf import SECOND_GAME


class LandingBikeEvent(StopBikeEvent):
    gravity = NumericProperty(0.2)
    current_event = StringProperty('on_landing')

    def set_lending(self, dt):
        print('... set_lending ...')
        BaseBikeEvent.unschedule([self.on_move, self.on_relax, self.on_stop])

        if self.road_pos.y < self.y:
            self.y -= self.speed
            self.add_speed(self.gravity)
        else:
            self.on_landing.cancel()
            self.stop()

        self._set_pos()

    def lending(self):
        print('LANDING')
        BaseBikeEvent.unschedule([self.on_move, self.on_relax, self.on_stop])
        self.current_event = 'on_landing'
        self.on_landing = Clock.schedule_interval(self.set_lending, SECOND_GAME)
