from kivy.properties import ObjectProperty
from kivy.uix.behaviors.button import ButtonBehavior


class BaseButtonBehavior(ButtonBehavior):
    canvas = ObjectProperty(None)

    def on_press(self):
        raise NotImplementedError

    def on_release(self):
        raise NotImplementedError

    @staticmethod
    def change_text(widget, text='...'):
        widget.text = text
