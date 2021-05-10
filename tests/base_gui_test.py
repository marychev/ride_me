from kivy.tests.common import GraphicUnitTest
from screen.game_screen import GameScreen
from utils.store import CACHE_NAME
from kivy.cache import Cache
from utils.get_object import GetObject
from utils.state import State

# TODO-WARNING: The tests have broken!
#  `test_gradual_loading_and_deleting_map_elements_onto_road`
#  `test_restart_game_screen`
# This test was failing for next sizes: 800x610, 800x600, 700x500, 600x400
# It is dirty fix temporary.
from kivy.utils import platform
from kivy.config import Config
from kivy.core.window import Window

from utils.store import Store

if platform not in ('android', 'ios'):
    Config.set('graphics', 'resizable', '1')
    Window.size = (1000, 700)


class BaseGameScreenGUITest(GraphicUnitTest):
    @staticmethod
    def setdefaults_config():
        Cache.register(CACHE_NAME, limit=1000)
        store = Store()
        store.register_all_table()

        store.set_rm(1000)
        store.add_cache_bike('Default')
        store.add_cache_map('Default')

    def set_app(self):
        BaseGameScreenGUITest.setdefaults_config()

        self.screen = GameScreen(name='game')
        self.render(self.screen)

        self.road = self.screen.ids['road']
        self.bike = self.screen.ids['bike']
        self.road.bike = self.bike

        self.road.init_app_config()
        self.bike.init_app_config()

        curtain = GetObject(self.road).curtain
        curtain.text = ''

        # default value
        self.bike.x = 800
        self.road.set_state(State.ON_LANDING_START)

        self.bike.y = self.road.line_points[-1]
        self.bike.speed = 0
        self.bike.max_speed = 20
        self.bike.power = 0
        self.bike.max_power = 300
