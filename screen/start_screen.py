from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from screen.game_screen import GameScreen

Builder.load_file("screen/start_screen.kv")


class StartScreen(Screen):

    def restart_game(self):
        self.manager.clear_widgets(screens=[self.manager.get_screen('game')])
        self.manager.add_widget(GameScreen(name='game'))

