from kivy.core.window import Window
from kivy.properties import NumericProperty, ObjectProperty, StringProperty
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line, Rectangle
from kivy.app import App

from conf import SECOND_GAME, WIDTH_GAME
from layout.base import BaseLayout
from utils.checks import background_texture, set_texture_uvpos


class Road(Widget):
    # height = NumericProperty(120)
    # width = NumericProperty(WIDTH_GAME)
    texture = ObjectProperty(Image(source='road/road-2.png').texture)

    def __init__(self, **kwargs):
        super(Road, self).__init__(**kwargs)

        self.texture.wrap = 'repeat'
        self.texture.uvsize = (Window.width / self.texture.width, -1)

    @staticmethod
    def get_game_screen():
        app = App.get_running_app()
        return app.root.get_screen('game')

    def get_status_bar(self):
        return self.parent.status_bar

    def go(self, dt):
        print(self.texture.uvpos[0])
        game_screen = self.get_game_screen()
        self.y = game_screen.ids.tools.height
        uvpos_x = self.texture.uvpos[0] + SECOND_GAME
        uvpos_y = self.texture.uvpos[1]
        set_texture_uvpos(self, uvpos_x, uvpos_y)
        # self.get_status_bar().show_status('Go bike ===>', self.parent.bike, self)

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
