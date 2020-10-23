from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from button.keyboard import KeyboardHandler


class Tools(BoxLayout, KeyboardHandler):
    right_btn = ObjectProperty(None)
    left_btn = ObjectProperty(None)

