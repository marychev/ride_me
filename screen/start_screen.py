from kivy.cache import Cache
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from layout.scene import CACHE_NAME
from utils.dir import abstract_path
from utils.state import State
from utils.validation import ValidObject
from label.curtain import Curtain
from road.road import Road
Builder.load_file(abstract_path('screen/start_screen.kv'))


class StartScreen(Screen):

    def restart_game(self):
        Cache.remove(CACHE_NAME)
        screen_name = 'game'

        screen = ValidObject.screen(self.manager.get_screen(screen_name))
        scene = screen.ids['scene']
        road = screen.ids['road']
        bike = screen.ids['bike']
        curtain = screen.ids['curtain']

        # road.init_app_config()
        # bike.init_app_config()

        bike.power = 10
        bike.speed = 0

        bike.collected_currency = 0
        bike.y = 800
        bike.canvas.remove_group("background")
        bike.anim_landing()

        road.set_state(State.NONE)
        road.landing_start()
        road.clear_widgets()
        road.distance_traveled = 0
        road.set_distance_traveled()

        # todo: error was happened sometimes or timer was not show
        if not curtain.text:
            scene.remove_widget(curtain)
            curtain = Curtain(font_size=120)
            curtain.add_to_game_screen()
        curtain.font_size = 120
        curtain.do_start_timer()

        Clock.schedule_interval(scene.start_timer, 1)

        self.manager.current = screen_name
