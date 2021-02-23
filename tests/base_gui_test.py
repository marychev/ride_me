from kivy.tests.common import GraphicUnitTest
from screen.game_screen import GameScreen
from layout.scene import CACHE_NAME
from kivy.cache import Cache
from utils.get_object import GetObject
from kivy.config import Config


class BaseGameScreenGUITest(GraphicUnitTest):
    def set_app(self):
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

        self.screen = GameScreen(name='game')
        self.render(self.screen)

        Cache.register(CACHE_NAME, limit=1000)

        self.road = self.screen.ids['road']
        self.bike = self.screen.ids['bike']

        self.road.init_app_config()
        self.bike.init_app_config()

        curtain = GetObject(self.road).curtain
        curtain.text = ''

        # default value
        self.road.state = 'on_landing__start'

        self.bike.y = self.road.line_points[-1]
        self.bike.speed = 0
        self.bike.max_speed = 20
        self.bike.power = 0
        self.bike.max_power = 300
