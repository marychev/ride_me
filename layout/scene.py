import os
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder

path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'scene.kv'))
Builder.load_file(path)


class Scene(FloatLayout):
    pass
