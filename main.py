from bike.model import BikeModel
from conf import *      # <-- don't delete!
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, WipeTransition

from level.model import MapModel
from screen.start_screen import StartScreen
from screen.menu_screen import MenuScreen
from screen.bikes_screen import BikesScreen
from screen.maps_screen import MapsScreen
from screen.shop_screen import ShopScreen
# from bike.bikes import BIKES, get_by_title as get_bike_by_title
# import re
# import cProfile
# from utils.init import app_config
from utils.store import Store


class RideMeApp(App):
    use_kivy_settings = True
    icon = 'rm-icon.png'
    title = 'Ride Me'

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
        return self.sm

    def build_config(self, config):
        user_rm = 1000
        store = Store()
        store.register_all_table()

        store.set_rm(user_rm)

        bike_model = BikeModel.create_empty()
        bike_model = store.add_cache_bike(None, bike_model)
        config.setdefaults('bike', {
            'rm': user_rm,
            'title': bike_model.title,
            'power': bike_model.power,
            'speed': bike_model.speed,
            'acceleration': bike_model.acceleration,
            'agility': bike_model.agility
        })

        map_model = MapModel.create_empty()
        map_model = store.add_cache_map(None, map_model)
        config.setdefaults('map', {
            'title': map_model.title,
            'level': map_model.level,
            'map': map_model.map,
            'total_way': map_model.total_way
        })

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
