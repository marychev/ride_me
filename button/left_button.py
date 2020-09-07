from kivy.graphics import Color, Rectangle, Ellipse
from kivy.properties import ListProperty
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.uix.image import Image

from button.base import BaseButtonBehavior


class LeftButtonWidget(BaseButtonBehavior, Image):
    x = NumericProperty(10)
    y = NumericProperty(10)
    pos = ReferenceListProperty(x, y)

    height = NumericProperty(0)
    width = NumericProperty(0)

    btn_size = ListProperty([80, 80])
    margin = NumericProperty(10)

    def __init__(self, **kwargs):
        super(LeftButtonWidget, self).__init__(**kwargs)
        self.set_canvas_button()

    def set_canvas_button(self):
        with self.canvas:
            Color(1, 1, 1)
            Ellipse(pos=(10, 10), size=self.btn_size)
            Color(255, 0, 0)
            Rectangle(pos=(30, 45), size=(self.btn_size[0]/2, self.margin))
