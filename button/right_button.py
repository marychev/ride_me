from kivy.core.window import Window
from kivy.graphics import Color, Rectangle, Ellipse
from kivy.properties import NumericProperty, ListProperty, ReferenceListProperty
from kivy.uix.image import Image

from button.base import BaseButtonBehavior


class RightButtonWidget(BaseButtonBehavior, Image):
    x = NumericProperty(Window.width - 110)
    y = NumericProperty(10)
    pos = ReferenceListProperty(x, y)
    height = NumericProperty(0)
    width = NumericProperty(0)
    btn_size = ListProperty([80, 80])
    margin = NumericProperty(10)

    def __init__(self, **kwargs):
        self.register_event_type('on_press')
        self.register_event_type('on_release')
        super(RightButtonWidget, self).__init__(**kwargs)

        self.set_canvas_button()

    def set_canvas_button(self):
        with self.canvas:
            Color(1, 1, 1)
            Ellipse(pos=(self.x, self.y), size=self.btn_size)
            Color(255, 0, 0)
            Rectangle(pos=(610, 45), size=(self.btn_size[0]/2, self.margin))
            Color(255, 0, 0)
            Rectangle(pos=(625, 30), size=(self.margin, self.btn_size[0]/2))

    def on_press(self):
        print(self.parent)
        self.parent.on_move(0)

    def on_release(self):
        self.parent.on_relax(0)

