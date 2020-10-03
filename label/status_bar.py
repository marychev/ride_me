from kivy.properties import StringProperty
from kivy.uix.label import Label

from conf import HEIGHT_GAME, WIDTH_GAME
from utils.checks import background


class StatusBar(Label):
    text = StringProperty('Start game!')

    def __init__(self, **kwargs):
        super(StatusBar, self).__init__(**kwargs)

        self.size_hint = (None, None)
        self.x = WIDTH_GAME / 2 - self.center_x
        self.y = HEIGHT_GAME - self.height - self.center_y / 2

        # self.text_size = 400, None
        # self.size = self.texture_size

        self.width = 320
        print(self.text_size)

        self.background()

    def background(self):
        background(self, 'c3131a')

