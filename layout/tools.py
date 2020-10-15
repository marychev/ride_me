from button.left_button import LeftButtonWidget  # !
from button.right_button import RightButtonWidget  # !
from utils.keyboard import KeyboardHandler
from kivy.uix.boxlayout import BoxLayout

from kivy.lang import Builder
Builder.load_file('layout/tools.kv')


class Tools(BoxLayout, KeyboardHandler):
    #
    #     self.background()
    #
    # def background(self):
    #     background(self, TOOLS_BACKGROUND)

    """    dev    """

