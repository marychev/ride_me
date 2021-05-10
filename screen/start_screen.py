from kivy.app import App
from kivy.cache import Cache
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from utils.sizes import FontSize as FS
from label.curtain import Curtain
from utils.store import CACHE_NAME
from utils.dir import abstract_path
from utils.state import State
from utils.validation import ValidObject
from screen.game_screen import GameScreen

Builder.load_file(abstract_path('screen/start_screen.kv'))


class StartScreen(Screen):

    def __init__(self, **kwargs):
        super(StartScreen, self).__init__(**kwargs)

        try:
            app = App.get_running_app()
            app.sm.add_widget(GameScreen(name='game'))
        except AttributeError as e:
            from kivy.logger import Logger
            Logger.warning('{0}\r\n[NOTE] Fix of the restart test\r\n'.format(e))

    def restart_game(self):
        Cache.remove(CACHE_NAME)
        screen_name = 'game'

        screen = ValidObject.screen(self.manager.get_screen(screen_name))
        screen.ids['left_btn_wrap'].children[0].button_state_style()
        screen.ids['right_btn_wrap'].children[0].button_state_style()

        scene = screen.ids['scene']
        road = screen.ids['road']
        bike = screen.ids['bike']

        if screen.ids.get('curtain'):
            scene.remove_widget(screen.ids['curtain'])

        road.bike = bike
        road.init_app_config()
        road.set_state(State.NONE)
        road.clear_widgets()
        road.landing_start()
        road.set_distance_traveled(0)

        bike.init_app_config()
        bike.collected_currency = 0
        bike.y = 800
        bike.canvas.remove_group("background")

        Curtain(font_size=FS.H1.value).add_to_game_screen(screen, scene)
        curtain = screen.ids['curtain']
        if not curtain.text:
            curtain.do_start_timer()

        Clock.schedule_interval(scene.start_timer, 1)

        self.manager.current = screen_name
