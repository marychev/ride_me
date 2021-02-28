from kivy.cache import Cache
from kivy.tests.common import GraphicUnitTest
from kivy.uix.screenmanager import ScreenManager, WipeTransition
from bike.bike import Bike
from bike.bikes import get_by_title as get_bike_by_title
from level.maps import get_by_title as get_map_by_title
from level.one.level_one import LevelOne
from screen.game_screen import GameScreen
from screen.menu_screen import MenuScreen
from utils.validation import ValidObject

RM = 1000


class AppConfigTest(GraphicUnitTest):
    def set_app(self):
        Cache.register('bike')
        Cache.register('map')
        Cache.remove('bike', 'rm')
        Cache.append('bike', 'rm', RM)

        self.sm = ScreenManager(transition=WipeTransition())
        self.sm.add_widget(MenuScreen(name='menu'))
        self.sm.add_widget(GameScreen(name='game'))
        self.render(self.sm)

    def test_bike_buy_success(self):
        self.set_app()
        _bike = get_bike_by_title('Default')

        menu_screen = ValidObject.menu_screen(self.sm.get_screen('menu'))
        self.assertEqual(menu_screen.get_label_item('No bike').text, 'No bike')

        self.assertEqual(_bike['title'], 'Default')
        self.assertTrue(Bike.buy(_bike))
        self.assertEqual(_bike['title'], Cache.get('bike', 'title'))
        self.assertEqual(_bike['power'], Cache.get('bike', 'power'))
        self.assertEqual(_bike['speed'], Cache.get('bike', 'speed'))
        self.assertEqual(_bike['acceleration'], Cache.get('bike', 'acceleration'))
        self.assertEqual(_bike['agility'], Cache.get('bike', 'agility'))
        self.assertEqual(RM - int(_bike['price']), Cache.get('bike', 'rm'))

    def test_map_buy_success(self):
        self.set_app()
        _map = get_map_by_title('Default')

        menu_screen = ValidObject.menu_screen(self.sm.get_screen('menu'))
        self.assertEqual(menu_screen.get_label_item('No map').text, 'No map')

        self.assertEqual(_map['title'], 'Default')
        self.assertTrue(LevelOne.buy(_map))
        self.assertEqual(_map['title'], Cache.get('map', 'title'))
        self.assertEqual(_map['level'], Cache.get('map', 'level'))
        self.assertEqual(_map['map'], Cache.get('map', 'map'))
        self.assertEqual(_map['total_way'], Cache.get('map', 'total_way'))
        self.assertEqual(RM - int(_map['price']), Cache.get('bike', 'rm'))



