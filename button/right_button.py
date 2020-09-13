from kivy.core.window import Window
from kivy.graphics import Color, Rectangle, Ellipse
from kivy.properties import NumericProperty, ListProperty, ReferenceListProperty
from kivy.uix.image import Image

from conf import SECOND_GAME
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
        print('---------------------')
        print('-- on_press RB -- ')
        print('---------------------')
        self.canvas.opacity = 0.5

        bike = self.parent.parent.scene.bike
        bike.on_motion(SECOND_GAME)

        text = bike.show_status('Go bike! ==>')
        BaseButtonBehavior.change_text(self.parent.status_bar, text)

    def on_release(self):
        print('---------------------')
        print('-- on_release RB -- ')
        print('---------------------')
        self.canvas.opacity = 1

        bike = self.parent.parent.scene.bike
        bike.on_relax(0)

        text = bike.show_status('... Relax ...')
        BaseButtonBehavior.change_text(self.parent.status_bar, text)

