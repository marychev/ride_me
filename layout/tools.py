from button.left_button import LeftButtonWidget
from button.right_button import RightButtonWidget
from utils.keyboard import KeyboardHandler
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

# from kivy.lang import Builder
# Builder.load_file('layout/tools.kv')


class Tools(BoxLayout, KeyboardHandler):
    right_btn = ObjectProperty(LeftButtonWidget())
    left_btn = ObjectProperty(None)
    #
    # def __init__(self, **kwargs):
    #     super(Tools, self).__init__(**kwargs)
    #
    #     # Widgets
    #     self.left_btn = LeftButtonWidget()
    #     self.right_btn = RightButtonWidget()
