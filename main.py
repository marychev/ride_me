from conf import *      # <-- don't delete!
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, WipeTransition
from screen.game_screen import GameScreen
from screen.start_screen import StartScreen
from screen.menu_screen import MenuScreen
from screen.bikes_screen import BikesScreen
from screen.maps_screen import MapsScreen
from screen.shop_screen import ShopScreen
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
    #
    # def on_pause(self):
    #     cProfile.run('re.compile("foo|bar")')
    #     return True

    def build(self):
        self.sm = ScreenManager(transition=WipeTransition())
        self.sm.add_widget(MenuScreen(name='menu'))
        self.sm.add_widget(BikesScreen(name='bikes'))
        self.sm.add_widget(MapsScreen(name='maps'))
        self.sm.add_widget(ShopScreen(name='shop'))
        self.sm.add_widget(GameScreen(name='game'))
        self.sm.add_widget(StartScreen(name='start'))
        return self.sm

    def build_config(self, config):
        config.setdefaults('bike', {
            'rm': '1000',
            'name': 'None',
            'power': '0',
            'speed': '0',
            'acceleration': '0',
            'agility': '0'
        })
        config.setdefaults('map', {
            'name': 'None',
        })

    def build_settings(self, settings):
        jsondata = '''[
            { "type": "numeric",
              "title": "rm",
              "section": "bike",
              "key": "rm" 
            },
            { "type": "title", "title": "Bike settings" },
            { "type": "string",
              "title": "Bike name",
              "section": "bike",
              "key": "name" },
            { "type": "numeric",
              "title": "Power",
              "section": "bike",
              "key": "power" },
            { "type": "numeric",
              "title": "Speed",
              "section": "bike",
              "key": "speed" },
            { "type": "numeric",
              "title": "Acceleration",
              "section": "bike",
              "key": "acceleration" },
            { "type": "numeric",
              "title": "Agility",
              "section": "bike",
              "key": "agility" 
            },
            { "type": "title", "title": "Map settings" },
            { "type": "string",
              "title": "Map name",
              "section": "map",
              "key": "name" }
        ]'''
        settings.add_json_panel('Ride me', self.config, data=jsondata)


if __name__ == '__main__':
    RideMeApp().run()
