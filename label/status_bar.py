from kivy.core.window import Window
from kivy.graphics import Color, Line
from kivy.properties import NumericProperty, StringProperty
from kivy.uix.label import Label


class StatusBar(Label):
    text = StringProperty('Start game!')
    x = NumericProperty((Window.width / 2) - 140)
    y = NumericProperty((Window.height / 2) + 40)
    height = NumericProperty(20)
    width = NumericProperty(300)

    def __init__(self, **kwargs):
        super(StatusBar, self).__init__(**kwargs)
        self.size_hint = (None, None)
        self.show_outline()

    def show_outline(self):
        rectangle = (self.x, self.y, self.width, self.height)
        with self.canvas.before:
            Color(.5, .5, .5, 1, mode='rgb')
            Line(width=1, rectangle=rectangle)