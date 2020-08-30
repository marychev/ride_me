from kivy.properties import ObjectProperty
from kivy.uix.behaviors.button import ButtonBehavior


class BaseButtonBehavior(ButtonBehavior):
    canvas = ObjectProperty(None)

    def on_press(self):
        self.canvas.opacity = 0.5

    def on_release(self):
        self.canvas.opacity = 1

    @staticmethod
    def change_text(widget, text='...'):
        widget.text = text
