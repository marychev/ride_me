from kivy.tests.common import GraphicUnitTest
from screen.game_screen import GameScreen
from layout.scene import CACHE_NAME
from kivy.cache import Cache
from utils.get_object import GetObject
from utils.state import State
from kivy.config import Config


class BaseGameScreenGUITest(GraphicUnitTest):
    @staticmethod
    def setdefaults_config():
        Config.setdefaults('bike', {
            'rm': '1000',
            'name': 'Hell Ride::Test',
            'power': '150',
            'speed': '10',
            'acceleration': '1',
            'agility': '1'
        })

        Config.setdefaults('map', {
            'name': 'Sakura::Test'
        })

    def set_app(self):
        BaseGameScreenGUITest.setdefaults_config()

        self.screen = GameScreen(name='game')
        self.render(self.screen)

        Cache.register(CACHE_NAME, limit=1000)

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
