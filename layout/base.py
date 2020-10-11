from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from utils.checks import show_outline


class BaseLayout(FloatLayout):
    status_bar = ObjectProperty(None)

    # def __init__(self, **kwargs):
    #     super(BaseLayout, self).__init__(**kwargs)
    #     self.status_bar = kwargs.get('status_bar')
    #     show_outline(self)

    @staticmethod
    def scene_default_height():
        return int(Window.height - (Window.height / 5.5))

    @staticmethod
    def tools_default_height():
        return int(Window.height - BaseLayout.scene_default_height())
