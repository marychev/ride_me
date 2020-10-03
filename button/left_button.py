from kivy.uix.image import Image
from kivy.clock import Clock
from conf import SECOND_GAME
from button.base import BaseButtonBehavior


class LeftButtonWidget(BaseButtonBehavior, Image):
    def __init__(self, **kwargs):
        super(LeftButtonWidget, self).__init__(**kwargs)
        self.size_hint = (None, None)

        self.x = self.margin_x
        self.y = self.margin_y

        self.set_canvas_button()

    def on_press(self):
        super().on_press()

        road = self.get_road()
        Clock.unschedule(road.go)
        Clock.unschedule(road.relax)
        Clock.schedule_interval(road.stop, SECOND_GAME)

