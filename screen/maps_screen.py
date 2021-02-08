from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from utils.dir import abstract_path
from kivy.properties import ObjectProperty

Builder.load_file(abstract_path('screen/maps_screen.kv'))


class MapsScreen(Screen):
    pass

