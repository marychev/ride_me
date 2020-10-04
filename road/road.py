from kivy.core.window import Window
from kivy.properties import NumericProperty, ObjectProperty, StringProperty
from kivy.uix.image import Image
from kivy.uix.widget import Widget

from conf import SECOND_GAME, WIDTH_GAME
from layout.base import BaseLayout
from utils.checks import background_texture, set_texture_uvpos


class Road(Widget):
    id = StringProperty('road')

    x = NumericProperty(0)
    y = NumericProperty(BaseLayout.tools_default_height())

    height = NumericProperty(120)
    width = NumericProperty(WIDTH_GAME)

    canvas = ObjectProperty()
    texture = ObjectProperty(Image(source='road/road-1.png').texture)

    tmp_ac = NumericProperty(0)

    def __init__(self, **kwargs):
        super(Road, self).__init__(**kwargs)
        self.size_hint = None, None
        background_texture(self)

    def get_status_bar(self):
        return self.parent.status_bar

    def go(self, dt):
        self.tmp_ac += 0.01
        uvpos_x = (self.texture.uvpos[0] + SECOND_GAME) + self.tmp_ac
        set_texture_uvpos(self, uvpos_x, self.texture.uvpos[1])
        self.get_status_bar().show_status('Go bike ===>', self.parent.bike, self)

    def relax(self, dt):
        uvpos_x = (self.texture.uvpos[0] + SECOND_GAME) % Window.width
        set_texture_uvpos(self, uvpos_x, self.texture.uvpos[1])
        self.get_status_bar().show_status('... Relax ...', self.parent.bike, self)

    def stop(self, dt):
        uvpos_x = (self.texture.uvpos[0] - (SECOND_GAME * 10))
        set_texture_uvpos(self, uvpos_x, self.texture.uvpos[1])
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
