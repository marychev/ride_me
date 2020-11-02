from conf import *      # <-- don't delete!
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, WipeTransition
from screen.game_screen import GameScreen
from screen.start_screen import StartScreen

sm = ScreenManager(transition=WipeTransition())
sm.add_widget(GameScreen(name='game'))
sm.add_widget(StartScreen(name='start'))


class RideMeApp(App):
    def build(self):
        return sm


if __name__ == '__main__':
    RideMeApp().run()
