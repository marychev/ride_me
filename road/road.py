from kivy.clock import Clock
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, StringProperty
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.core.window import Window
from conf import SECOND_GAME, WIDTH_GAME
from layout.base import BaseLayout
from kivy.graphics import Color, Rectangle, Ellipse
from button.base import BaseButtonBehavior


class Road(Widget):
    id = StringProperty('road')

    x = NumericProperty(0)
    y = NumericProperty(BaseLayout.tools_default_height())

    height = NumericProperty(420)
    width = NumericProperty(WIDTH_GAME)

    canvas = ObjectProperty()
    texture = ObjectProperty(Image(source='road/road-1.png').texture)

    tmp_ac = NumericProperty(0)

    def __init__(self, **kwargs):
        super(Road, self).__init__(**kwargs)
        self.size_hint = None, None

        self.texture.wrap = 'repeat'
        self.texture.uvsize = (Window.width / self.texture.width, -1)
        with self.canvas.before:
            Rectangle(texture=self.texture, size=self.size, pos=self.pos)

    def get_status_bar(self):
        return self.parent.status_bar

    def go(self, dt):
        self.tmp_ac += 0.01

        uv_pos_x = (self.texture.uvpos[0] + SECOND_GAME) + self.tmp_ac
        self.texture.uvpos = (uv_pos_x, self.texture.uvpos[1])
        with self.canvas.before:
            Rectangle(texture=self.texture, size=self.size, pos=self.pos)

        self.get_status_bar().show_status('Go bike ===>', self.parent.bike, self)

    def relax(self, dt):
        uv_pos_x = (self.texture.uvpos[0] + SECOND_GAME)  # % Window.width
        self.texture.uvpos = (uv_pos_x, self.texture.uvpos[1])
        with self.canvas.before:
            Rectangle(texture=self.texture, size=self.size, pos=self.pos)

        self.get_status_bar().show_status('... Relax ...', self.parent.bike, self)

    def stop(self, dt):
        uv_pos_x = (self.texture.uvpos[0] - (SECOND_GAME * 10))
        self.texture.uvpos = (uv_pos_x, self.texture.uvpos[1])
        with self.canvas.before:
            Rectangle(texture=self.texture, size=self.size, pos=self.pos)

        self.get_status_bar().show_status('S T O P', self.parent.bike, self)

    def show_status(self, title='ROAD'):
        return '''
{}
-----------------------------------------------
UVPos:          {}
Pos:            {}'''.format(
            title,
            self.texture.uvpos, self.pos
        )
