from kivy.cache import Cache
from kivy.config import Config
from kivy.tests.common import GraphicUnitTest
from kivy.uix.screenmanager import ScreenManager, WipeTransition

from layout.scene import CACHE_NAME
from screen.game_screen import GameScreen
from screen.start_screen import StartScreen
from tests.level.test_map_road import TESTMAP
from tests.base_gui_test import BaseGameScreenGUITest
from utils.validation import ValidObject
from level.one.level_one import LevelOne


class RestartGameScreenTest(GraphicUnitTest):
    def set_app(self):
        BaseGameScreenGUITest.setdefaults_config()
        Cache.register(CACHE_NAME, limit=1000)

        self.manager = ScreenManager(transition=WipeTransition())
        self.manager.add_widget(StartScreen(name='start'))
        self.manager.add_widget(GameScreen(name='game'))
        self.render(self.manager)

        screen = ValidObject.screen(self.manager.get_screen('game'))
        self.road = screen.ids['road']
        self.bike = screen.ids['bike']
        self.road.bike = self.bike
        self.bike.speed = 0

    def test_restart_game_screen(self):
        self.set_app()
        self.road.level = LevelOne(self.road, self.bike, TESTMAP)
        self.road.level.map = TESTMAP

        self.road.init_app_config()
        self.bike.init_app_config()

        # thirty position
        self.road.distance_traveled = 4200
        self.road.set_distance_traveled()
        road_names = [r.__class__.__name__ for r in self.road.children[:]]
        thirty_map_names = [t['name'] for t in TESTMAP[3:4]]
        self.assertEqual(road_names[0], thirty_map_names[0])

        self.manager.get_screen('start').restart_game()
        self.assertEqual(self.road.distance_traveled, 0)

        # start first position
        start_map_names = [t['name'] for t in TESTMAP[0:2]]
        self.assertEqual(len(self.road.children), len(start_map_names))

