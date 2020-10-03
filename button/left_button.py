from kivy.uix.image import Image
from kivy.clock import Clock

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
        Clock.unschedule(road.relax)
        Clock.schedule_interval(road.go, 1 / 60)

        text = 'S T O P'
        BaseButtonBehavior.change_text(self.parent.status_bar, text)

    def on_release(self):
        super().on_release()

        text = '... Relax ...'
        BaseButtonBehavior.change_text(self.parent.status_bar, text)