from conf import *      # <-- don't delete!
from kivy.app import App
from rideme_game import RideMeGame


class RideMeApp(App):
    def build(self):
        return RideMeGame()


if __name__ == '__main__':
    RideMeApp().run()
