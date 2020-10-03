from kivy.properties import StringProperty
from kivy.uix.label import Label

from conf import HEIGHT_GAME, WIDTH_GAME
from utils.checks import background


class StatusBar(Label):
    text = StringProperty('Start game!')

    def __init__(self, **kwargs):
        super(StatusBar, self).__init__(**kwargs)

        self.size_hint = (None, None)
        self.width = WIDTH_GAME / 2
        self.height = HEIGHT_GAME / 2
        self.x = self.width - self.center_x
        self.y = HEIGHT_GAME - self.height - 8

        self.background()

    def background(self):
        background(self, 'c3131a')

    def show_status(self, title, bike, road):
        self.text = '{}\n{}{}'.format(title, bike.show_status(), road.show_status())
        return self.text
