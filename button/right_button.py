from kivy.graphics import Color, Rectangle
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
from kivy.properties import StringProperty, BooleanProperty, NumericProperty, ObjectProperty
from kivy.uix.image import Image
from button.left_button import LeftButtonWidget
from utils.counter import CounterClock
from conf import WIDTH_GAME, SECOND_GAME
from kivy.event import EventDispatcher

from kivy.lang import Builder
Builder.load_file('button/right_button.kv')


class RightButtonWidget(LeftButtonWidget):
    counter = ObjectProperty(CounterClock())

    def on_press(self):
        self.button_state_style()
        self.counter.start()

        road = self.get_road()
        print(road)
        # Clock.unschedule(road.stop)
        # Clock.unschedule(road.relax)
        Clock.schedule_interval(road.go, SECOND_GAME)

    def on_release(self):
        self.button_state_style()
        self.counter.stop()



