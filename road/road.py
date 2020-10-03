from kivy.clock import Clock
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, StringProperty
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.core.window import Window
from conf import SECOND_GAME, WIDTH_GAME
from layout.base import BaseLayout
from kivy.graphics import Color, Rectangle, Ellipse


class Road(Widget):
    id = StringProperty('road')

    x = NumericProperty(0)
    y = NumericProperty(BaseLayout.tools_default_height())

    height = NumericProperty(60)
    width = NumericProperty(WIDTH_GAME)

    canvas = ObjectProperty()
    texture = ObjectProperty(Image(source='road/road.png').texture)

    tmp_ac = NumericProperty(0)

    def __init__(self, **kwargs):
        super(Road, self).__init__(**kwargs)
        # Clock.schedule_interval(self.move, SECOND_GAME)
        self.size_hint = None, None

        self.texture.wrap = 'repeat'
        self.texture.uvsize = (Window.width / self.texture.width, -1)
        with self.canvas.before:
            Rectangle(texture=self.texture, size=self.size, pos=self.pos)

    def go(self, dt):
        print(self.texture.uvpos[0], self.tmp_ac, SECOND_GAME)
        self.tmp_ac += 0.01

        uv_pos_x = (self.texture.uvpos[0] + SECOND_GAME) + self.tmp_ac
        self.texture.uvpos = (uv_pos_x, self.texture.uvpos[1])
        with self.canvas.before:
            Rectangle(texture=self.texture, size=self.size, pos=self.pos)
        print('> > > > > ', self.texture.uvpos)

    def relax(self, dt):
        print('*** relax ***', self.tmp_ac)
        uv_pos_x = (self.texture.uvpos[0] + SECOND_GAME)  # % Window.width
        self.texture.uvpos = (uv_pos_x, self.texture.uvpos[1])
        with self.canvas.before:
            Rectangle(texture=self.texture, size=self.size, pos=self.pos)

        print('... relax ... ', self.texture.uvpos)