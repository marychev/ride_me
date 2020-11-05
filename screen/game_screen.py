import os
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'game_screen.kv'))
Builder.load_file(path)


class GameScreen(Screen):
    pass

