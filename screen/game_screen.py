from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from utils.dir import abstract_path
from kivy.loader import Loader
from kivy.uix.image import Image


Builder.load_file(abstract_path('screen/game_screen.kv'))


class GameScreen(Screen):
    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)

        # self.add_widget(self.build())

    # def _image_loaded(self, proxy_img):
    #     if proxy_img.image.texture:
    #         self.image.texture = proxy_img.image.texture
    #
    # def build(self):
    #     proxy_img = Loader.image('download.jpeg')
    #
    #     Loader.stop()
    #
    #     proxy_img.bind(on_load=self._image_loaded)
    #     self.image = Image()
    #     return self.image
