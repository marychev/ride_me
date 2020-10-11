from kivy.properties import StringProperty, ReferenceListProperty
from kivy.uix.label import Label
from kivy.graphics import Color, Line, Rectangle

from conf import HEIGHT_GAME, WIDTH_GAME
from utils.checks import background


class StatusBar(Label):
    text = StringProperty('Start Game!')
    state = StringProperty('')
    state_none = StringProperty('None')
    state_start = StringProperty('Start')
    states = ReferenceListProperty(state_none, state_start)

    def __init__(self, **kwargs):
        super(StatusBar, self).__init__(**kwargs)

        self.size_hint = (None, None)
        self.width = WIDTH_GAME / 2
        self.height = HEIGHT_GAME / 2
        self.x = self.width - self.center_x
        self.y = HEIGHT_GAME - self.height - 8
        self.state = self.state_none

        self.background()
        self.start_widget()

    def background(self):
        self.state != self.state_none and background(self, '111111bd')

    def start_widget(self):
        with self.canvas:
            Color(.1, .2, .4, .8)
            Rectangle(size=(WIDTH_GAME, HEIGHT_GAME), pos=(0, 0))

    def show_status(self, title, bike, road):
        self.text = '{}\n{}{}'.format(title, bike.show_status(), road.show_status())
        return self.text
