from kivy.cache import Cache
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from layout.scene import CACHE_NAME
from screen.game_screen import GameScreen
from utils.dir import abstract_path
from utils.validation import ValidObject
from kivy.app import App
from utils.get_object import GetObject
from kivy.clock import Clock
from road.road import Road
from utils.state import State
from kivy.uix.label import Label
from objects import Finish

Builder.load_file(abstract_path('screen/start_screen.kv'))


class StartScreen(Screen):

    def restart_game(self):
        Cache.remove(CACHE_NAME)
        screen_name = 'game'

        screen = ValidObject.screen(self.manager.get_screen(screen_name))
        scene = screen.ids['scene']
        road = screen.ids['road']
        bike = screen.ids['bike']
        start_timer = screen.ids['start_timer']

        if not start_timer.text:
            scene.remove_widget(start_timer)
            start_timer = Label(markup=True, font_size=120)
            screen.ids['start_timer'] = start_timer
            scene.add_widget(start_timer)

        bike.speed = 0
        bike.acceleration = 0
        bike.y = 300
        bike.canvas.remove_group("background")
        bike.anim_landing()

        road.set_state(State.NONE)
        road.landing_start()
        road.clear_widgets()
        road.distance_traveled = 0
        road.set_distance_traveled()

        start_timer.font_size = 120
        scene.do_start_timer()
        Clock.schedule_interval(scene.start_timer, 1)

        self.manager.current = screen_name
