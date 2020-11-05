import os
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from screen.game_screen import GameScreen

path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'start_screen.kv'))
Builder.load_file(path)


class StartScreen(Screen):

    def restart_game(self):
        self.manager.clear_widgets(screens=[self.manager.get_screen('game')])
        self.manager.add_widget(GameScreen(name='game'))

