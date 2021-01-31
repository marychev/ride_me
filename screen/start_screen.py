from kivy.cache import Cache
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from layout.scene import CACHE_NAME
from screen.game_screen import GameScreen
from utils.dir import abstract_path
from utils.validation import ValidObject
from kivy.app import App

Builder.load_file(abstract_path('screen/start_screen.kv'))


class StartScreen(Screen):

    def restart_game(self):
        Cache.remove(CACHE_NAME)
        screen_name = 'game'

        screen = ValidObject.screen(self.manager.get_screen(screen_name))
        road = screen.ids['road']
        bike = screen.ids['bike']

        bike.speed = 0
        bike.acceleration = 0
        bike.y = 300
        bike.canvas.remove_group("background")
        bike.anim_landing()

        road.clear_widgets()
        road.distance_traveled = 0
        road.set_distance_traveled()

        self.manager.current = screen_name
