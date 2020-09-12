from kivy.core.window import Window
from kivy.properties import ObjectProperty, NumericProperty
from button.base import BaseButtonBehavior
from button.left_button import LeftButtonWidget
from button.right_button import RightButtonWidget
from layout.base import BaseLayout
from utils.keyboard import KeyboardHandler
from utils.checks import show_outline


class Tools(BaseLayout, KeyboardHandler):
    x = NumericProperty(0)
    y = NumericProperty(0)

    height = NumericProperty(Window.height - BaseLayout.scene_default_height())
    width = NumericProperty(Window.width)

    bike = ObjectProperty(None)
    left_btn = ObjectProperty(None)
    right_btn = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(Tools, self).__init__(**kwargs)

        # Widgets
        self.left_btn = LeftButtonWidget()
        self.right_btn = RightButtonWidget()

        # Add widgets
        self.add_widget(self.left_btn)
        self.add_widget(self.right_btn)

        show_outline(self)

    def on_stop(self, dt):
        print('<<< Stop ')
        self.left_btn.canvas.opacity = 0.5
        self.right_btn.canvas.opacity = 1

        self.set_bike()
        self.bike.on_stop()

        text = self.parent.scene.bike.show_status('... Stop ...')
        BaseButtonBehavior.change_text(self.status_bar, text)
