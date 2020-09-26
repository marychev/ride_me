from kivy.graphics import Color, Rectangle, Ellipse
from kivy.properties import ListProperty
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.uix.image import Image
from layout.base import BaseLayout

from button.base import BaseButtonBehavior


class LeftButtonWidget(BaseButtonBehavior, Image):
    height = NumericProperty(10)
    width = NumericProperty(10)

    btn_size = ListProperty([80, 80])

    def __init__(self, **kwargs):
        super(LeftButtonWidget, self).__init__(**kwargs)
        self.size_hint = (None, None)
        self.set_canvas_button()

    def set_canvas_button(self):
        with self.canvas:
            Color(1, 1, 1)
            Ellipse(pos=(self.x, self.y), size=self.btn_size)
            Color(255, 0, 0)
            Rectangle(
                pos=((BaseLayout.tools_default_height() / 2) - self.x, (BaseLayout.tools_default_height() / 2)),
                size=(self.btn_size[0]/2, 10))

    def on_press(self):

        self.canvas.opacity = 0.5
        self.disabled = True

        bike = self.parent.parent.scene.bike
        # bike.on_stop()

        text = 'S T O P'
        BaseButtonBehavior.change_text(self.parent.status_bar, text)

    def on_release(self):
        self.canvas.opacity = 1
        self.disabled = False

        bike = self.parent.parent.scene.bike
        # bike.on_relax()

        text = '... Relax ...'
        BaseButtonBehavior.change_text(self.parent.status_bar, text)