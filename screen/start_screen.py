from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from screen.game_screen import GameScreen
from utils.dir import abstract_path

Builder.load_file(abstract_path('screen/start_screen.kv'))


class StartScreen(Screen):

    def restart_game(self):
        self.manager.clear_widgets(screens=[self.manager.get_screen('game')])
        self.manager.add_widget(GameScreen(name='game'))

