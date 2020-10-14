from conf import *      # <-- don't delete!
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition


ride_me = Builder.load_file("ride_me.kv")


class StartScreen(Screen):
    pass


class GameScreen(Screen):
    pass


sm = ScreenManager(transition=WipeTransition())
sm.add_widget(StartScreen(name='start'))
sm.add_widget(GameScreen(name='game'))


class RideMeApp(App):
    def build(self):
        return sm


if __name__ == '__main__':
    RideMeApp().run()
