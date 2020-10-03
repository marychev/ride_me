from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from button.base import BaseButtonBehavior
from button.left_button import LeftButtonWidget
from button.right_button import RightButtonWidget
from layout.base import BaseLayout
from utils.keyboard import KeyboardHandler
from utils.checks import background
from conf import WIDTH_GAME

TOOLS_BACKGROUND = '000000'


class Tools(BaseLayout, KeyboardHandler):
    id = StringProperty('tools')

    height = NumericProperty(BaseLayout.tools_default_height())
    width = NumericProperty(WIDTH_GAME)

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

        self.background()

    def background(self):
        background(self, TOOLS_BACKGROUND)


