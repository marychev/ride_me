from kivy.core.window import Window
from kivy.graphics import Color, Rectangle, Ellipse
from kivy.properties import NumericProperty, ListProperty, ReferenceListProperty, StringProperty
from kivy.uix.image import Image
from kivy.clock import Clock

from conf import WIDTH_GAME, HEIGHT_GAME
from button.base import BaseButtonBehavior


class RightButtonWidget(BaseButtonBehavior, Image):
    id = StringProperty('right_btn')

    def __init__(self, **kwargs):
        super(RightButtonWidget, self).__init__(**kwargs)
        self.size_hint = (None, None)

        self.x = WIDTH_GAME - self.btn_size_width - self.margin_x
        self.y = self.margin_y

        self.set_canvas_button()

    def get_road(self):
        return self.parent.parent.scene.road

    def get_bike(self):
        return self.parent.parent.scene.bike

    def on_press(self):
        super().on_press()

        road = self.get_road()
        Clock.schedule_interval(road.go, 1 / 60)

        text = 'Go bike! ===>\n'
        text += 'Road: {}, {}'.format(road.texture.uvpos, road.pos)
        BaseButtonBehavior.change_text(self.parent.status_bar, text)

    def on_release(self):
        super().on_release()

        road = self.get_road()
        Clock.unschedule(road.go)
        Clock.schedule_interval(road.relax, 1 / 60)
        # road.relax()

        bike = self.get_bike()
        text = bike.show_status('... Relax ...')
        text += 'Road: {}, {}'.format(road.texture.uvpos, road.pos)
        BaseButtonBehavior.change_text(self.parent.status_bar, text)

    def set_canvas_button(self):
        super().set_canvas_button()

        with self.canvas.after:
            icon2_x = self.icon_x - (self.icon_height / 2) + self.icon_width / 2
            icon2_y = self.icon_y - (self.icon_width / 2) + self.icon_height / 2
            Color(255, 0, 0)
            Rectangle(pos=(icon2_x, icon2_y), size=(self.icon_height, self.icon_width))


