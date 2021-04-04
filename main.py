from conf import *      # <-- don't delete!
from kivy.app import App
from kivy.cache import Cache
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
        self.sm.add_widget(StartScreen(name='start'))
        self.sm.add_widget(GameScreen(name='game'))
        return self.sm

    def build_config(self, config):
        Cache.register('bike')
        Cache.append('bike', 'rm', 1000)
        Cache.append('bike', 'title', 'None')
        Cache.append('bike', 'power', 0)
        Cache.append('bike', 'speed', 0)
        Cache.append('bike', 'acceleration', 0)
        Cache.append('bike', 'agility', 0)
        # config.setdefaults('bike', {
        #     'rm': '2020',
        #     'title': 'None',
        #     'power': '0',
        #     'speed': '0',
        #     'acceleration': '0',
        #     'agility': '0'})

        Cache.register('map')
        Cache.append('map', 'title', 'None')
        Cache.append('map', 'level', 'None')
        Cache.append('map', 'map', 'None')
        Cache.append('map', 'total_way', 0)
        # config.setdefaults('map', {
        #     'title': 'None',
        #     'level': 'None',
        #     'map': 'None',
        #     'total_way': '0'
        # })

    # def build_settings(self, settings):
    #     jsondata = '''[
    #         { "type": "numeric",
    #           "title": "rm",
    #           "section": "bike",
    #           "key": "rm"
    #         },
    #         { "type": "title", "title": "Bike settings" },
    #         { "type": "string",
    #           "title": "Bike title",
    #           "section": "bike",
    #           "key": "title" },
    #         { "type": "numeric",
    #           "title": "Power",
    #           "section": "bike",
    #           "key": "power" },
    #         { "type": "numeric",
    #           "title": "Speed",
    #           "section": "bike",
    #           "key": "speed" },
    #         { "type": "numeric",
    #           "title": "Acceleration",
    #           "section": "bike",
    #           "key": "acceleration" },
    #         { "type": "numeric",
    #           "title": "Agility",
    #           "section": "bike",
    #           "key": "agility"
    #         },
    #         { "type": "title", "title": "Map settings" },
    #         { "type": "string",
    #           "title": "Map title",
    #           "section": "map",
    #           "key": "title" },
    #         { "type": "string",
    #           "title": "Level",
    #           "section": "map",
    #           "key": "level" },
    #         { "type": "numeric",
    #           "title": "Map #",
    #           "section": "map",
    #           "key": "map" },
    #         { "type": "numeric",
    #           "title": "Total way",
    #           "section": "map",
    #           "key": "total_way"
    #         }
    #     ]'''
    #     settings.add_json_panel('Ride me', self.config, data=jsondata)


if __name__ == '__main__':
    RideMeApp().run()
