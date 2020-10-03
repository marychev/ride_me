from kivy.properties import ObjectProperty, ListProperty, NumericProperty, ReferenceListProperty
from kivy.uix.behaviors.button import ButtonBehavior
from kivy.utils import get_color_from_hex
from kivy.graphics import Color, Rectangle, Ellipse


class BaseButtonBehavior(ButtonBehavior):
    height = NumericProperty(80)
    width = NumericProperty(80)

    margin_x = NumericProperty(20)
    margin_y = NumericProperty(20)
    margin = ReferenceListProperty(margin_x, margin_y)

    btn_size_height = NumericProperty(80)
    btn_size_width = NumericProperty(80)
    btn_size = ReferenceListProperty(btn_size_width, btn_size_height)

    canvas = ObjectProperty(None)

    icon_width = NumericProperty(0)
    icon_height = NumericProperty(0)
    icon_x = NumericProperty(0)
    icon_y = NumericProperty(0)

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

    @staticmethod
    def change_text(widget, text='...'):
        widget.text = text

    def set_canvas_button(self):
        with self.canvas:
            self.canvas.clear()
            Color(.8, .8, .8)
            Ellipse(pos=self.pos, size=self.size)

        with self.canvas.after:
            Color(1, 1, 1)
            Ellipse(pos=(self.x, self.y), size=self.btn_size)

            self.icon_width = self.btn_size_width / 2
            self.icon_height = self.margin_x / 2
            self.icon_x = self.x + self.icon_width - self.margin_x
            self.icon_y = self.y + self.icon_height + self.margin_y + 5
            Color(255, 0, 0)
            Rectangle(pos=(self.icon_x, self.icon_y), size=(self.icon_width, self.icon_height))


