from conf import *
from kivy.app import App
from rideme_game import RideMeGame


class RideMeApp(App):

    def build(self):
        game = RideMeGame()
        return game


if __name__ == '__main__':
    RideMeApp().run()
