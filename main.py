from conf import *      # <-- don't delete!
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, WipeTransition
from screen.game_screen import GameScreen
from screen.start_screen import StartScreen
from screen.menu_screen import MenuScreen
import re
import cProfile


class RideMeApp(App):
    use_kivy_settings = True
    icon = 'rm-icon.png'
    title = 'Ride me'

    # def on_start(self):
    #     self.profile = cProfile.Profile()
    #     self.profile.enable()
    #
    # def on_stop(self):
    #     self.profile.disable()
    #     self.profile.dump_stats('myapp.profile')

    def on_pause(self):
        cProfile.run('re.compile("foo|bar")')
        return True

    def build(self):
        self.sm = ScreenManager(transition=WipeTransition())
        self.sm.add_widget(MenuScreen(name='menu'))
        self.sm.add_widget(GameScreen(name='game'))
        self.sm.add_widget(StartScreen(name='start'))
        return self.sm

    def build_settings(self, settings):
        jsondata = '''[{ "type": "title", "title": "Ride me settings" }]'''
        settings.add_json_panel('Ride me', self.config, data=jsondata)


if __name__ == '__main__':
    RideMeApp().run()
