from kivy.core.window import Window
from kivy.graphics import Color, Rectangle, Ellipse
from kivy.properties import NumericProperty, ListProperty, ReferenceListProperty
from kivy.uix.image import Image
from kivy.clock import Clock

from conf import SECOND_GAME
from button.base import BaseButtonBehavior


class RightButtonWidget(BaseButtonBehavior, Image):
    x = NumericProperty(Window.width - 110)
    y = NumericProperty(10)

    height = NumericProperty(10)
    width = NumericProperty(10)
    btn_size = ListProperty([80, 80])

    def __init__(self, **kwargs):
        super(RightButtonWidget, self).__init__(**kwargs)

        self.set_canvas_button()

    def set_canvas_button(self):
        with self.canvas:
            Color(1, 1, 1)
            Ellipse(pos=(self.x, self.y), size=self.btn_size)
            Color(255, 0, 0)
            Rectangle(pos=(610, 45), size=(self.btn_size[0]/2, 10))
            Color(255, 0, 0)
            Rectangle(pos=(625, 30), size=(10, self.btn_size[0]/2))

    def on_press(self):
        self.canvas.opacity = 0.5
        self.disabled = True

        bike = self.parent.parent.scene.bike
        # bike.on_go()

        text = 'Go bike! ==>'
        BaseButtonBehavior.change_text(self.parent.status_bar, text)

    def on_release(self):
        self.canvas.opacity = 1
        self.disabled = False

        bike = self.parent.parent.scene.bike
        # bike.on_relax()

        text = '... Relax ...'
        BaseButtonBehavior.change_text(self.parent.status_bar, text)
