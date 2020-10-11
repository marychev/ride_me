from kivy.uix.image import Image
from kivy.clock import Clock
from conf import SECOND_GAME
from button.base import BaseButtonBehavior

from kivy.lang import Builder
Builder.load_file('button/left_button.kv')


class LeftButtonWidget(BaseButtonBehavior, Image):

    def on_press(self):
        super().on_press()

        # road = self.get_road()
        # Clock.unschedule(road.go)
        # Clock.unschedule(road.relax)
        # Clock.schedule_interval(road.stop, SECOND_GAME)

