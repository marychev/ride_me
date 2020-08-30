from kivy.core.window import Window
from kivy.properties import ObjectProperty, NumericProperty

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
    left_btn = ObjectProperty(None)
    right_btn = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(Tools, self).__init__(**kwargs)

        # Widgets
        self.left_btn = LeftButtonWidget()
        self.right_btn = RightButtonWidget()

        # Bind Events
        self.left_btn.fbind('on_press', lambda x: self.on_stop())
        self.right_btn.fbind('on_press', lambda x: self.on_move())
        self.left_btn.fbind('on_release', lambda x: self.on_relax())
        self.right_btn.fbind('on_release', lambda x: self.on_relax())

        # Add widgets
        self.add_widget(self.left_btn)
        self.add_widget(self.right_btn)

        show_outline(self)

    def on_move(self):
        self.parent.scene.bike.move()
        RightButtonWidget.change_text(self.status_bar, 'Go')

    def on_relax(self):
        self.parent.scene.bike.relax()
        RightButtonWidget.change_text(self.status_bar)

    def on_stop(self):
        self.parent.scene.bike.stop()
        LeftButtonWidget.change_text(self.status_bar, '...breakup...')
