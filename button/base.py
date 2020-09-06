from kivy.properties import ObjectProperty
from kivy.uix.behaviors.button import ButtonBehavior


class BaseButtonBehavior(ButtonBehavior):
    canvas = ObjectProperty(None)

    @staticmethod
    def change_text(widget, text='...'):
        widget.text = text
