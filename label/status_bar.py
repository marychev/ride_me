from kivy.properties import StringProperty, ReferenceListProperty
from kivy.uix.label import Label
from kivy.graphics import Color, Line, Rectangle

from conf import HEIGHT_GAME, WIDTH_GAME
from utils.checks import background


class StatusBar(Label):
    text = StringProperty('Start Game!')

    def __init__(self, **kwargs):
        super(StatusBar, self).__init__(**kwargs)

    def show_status(self, title, bike, road):
        if not road.has_finished():
            self.text = '{}\r{}{}'.format(title, bike.show_status(), road.show_status())
        else:
            self.text = 'FINISH!'
        return self.text
