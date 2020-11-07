from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from utils.dir import abstract_path

Builder.load_file(abstract_path('layout/scene.kv'))


class Scene(FloatLayout):
    pass
