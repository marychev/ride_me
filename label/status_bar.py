from kivy.core.window import Window
from kivy.properties import NumericProperty, StringProperty
from kivy.uix.label import Label
from utils.checks import show_outline


class StatusBar(Label):
    text = StringProperty('Start game!')

    x = NumericProperty(450)
    y = NumericProperty(450)

    height = NumericProperty(180)
    width = NumericProperty(400)

    def __init__(self, **kwargs):
        super(StatusBar, self).__init__(**kwargs)
        self.size_hint = (None, None)
        show_outline(self)

