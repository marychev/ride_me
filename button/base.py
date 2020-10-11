from kivy.clock import Clock
from kivy.graphics import Color, Rectangle, Ellipse
from kivy.properties import ObjectProperty, NumericProperty, ReferenceListProperty
from kivy.uix.behaviors.button import ButtonBehavior

from conf import SECOND_GAME


class BaseButtonBehavior(ButtonBehavior):
    def get_road(self):
        return self.parent.parent.scene.road

    def get_bike(self):
        return self.parent.parent.scene.bike

    def on_press(self):
        self.canvas.opacity = 0.5
        self.disabled = True

    def on_release(self):
        self.canvas.opacity = 1
        self.disabled = False

        # road = self.get_road()
        # Clock.unschedule(road.go)
        # Clock.unschedule(road.stop)
        # Clock.schedule_interval(road.relax, SECOND_GAME)

    @staticmethod
    def change_text(widget, text='...'):
        widget.text = text

    # def set_canvas_button(self):
    #     with self.canvas:
    #         self.canvas.clear()
    #         Color(.8, .8, .8)
    #         Ellipse(pos=self.pos, size=self.size)
    #
    #     with self.canvas.after:
    #         Color(1, 1, 1)
    #         Ellipse(pos=(self.x, self.y), size=self.btn_size)
    #
    #         self.icon_width = self.btn_size_width / 2
    #         self.icon_height = self.margin_x / 2
    #         self.icon_x = self.x + self.icon_width - self.margin_x
    #         self.icon_y = self.y + self.icon_height + self.margin_y + 5
    #         Color(255, 0, 0)
    #         Rectangle(pos=(self.icon_x, self.icon_y), size=(self.icon_width, self.icon_height))