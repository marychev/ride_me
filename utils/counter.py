from kivy.clock import Clock
from kivy.properties import NumericProperty
from kivy.event import EventDispatcher


class CounterClock(EventDispatcher):
    count = NumericProperty(0)

    def __init__(self, **kwargs):
        super(CounterClock, self).__init__(**kwargs)
        self.register_event_type('on_counter')

    def on_counter(self):
        print('INIT on_counter event', self)

    def _on_counter(self, dt):
        self.count += dt

    def start(self):
        self.on_counter = Clock.schedule_interval(self._on_counter, 1/60)

    def stop(self):
        self.on_counter.cancel()
