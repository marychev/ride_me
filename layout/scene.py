from kivy.uix.floatlayout import FloatLayout
from layout.base import BaseLayout
from utils.checks import set_texture_uvpos
from kivy.lang import Builder

Builder.load_file('layout/scene.kv')


class Scene(FloatLayout):

    def animate(self, dt):
        self.y = BaseLayout.tools_default_height()
        uvpos_x = (self.texture.uvpos[0] + 0.0005)
        set_texture_uvpos(self, uvpos_x, self.texture.uvpos[1])
