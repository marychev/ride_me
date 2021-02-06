import time
from kivy.app import App
from kivy.clock import Clock
from kivy.event import EventDispatcher
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from objects import Finish
from utils.get_object import GetObject
from utils.state import State


class BaseDispatcher(EventDispatcher):
    road = ObjectProperty(None)
    bike = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(BaseDispatcher, self).__init__(**kwargs)
        Clock.schedule_once(self.after_init)

    def after_init(self, dt):
        print('[after_init--BaseDispatcher--]')
        app = App.get_running_app()
        ids = app and app.root.current_screen.ids
        if ids:
            if not self.bike and ids['bike']:
                self.bike = ids['bike']
            if not self.road and ids['road']:
                self.road = ids['road']

    def set_distances(self):
        self.road.set_distance_traveled()

    def road_finish(self):
        self.bike.power = 0
        self.bike.speed = 0
        self.bike.acceleration = 0
        self.bike.finish_dt = time.time()
        self.bike.currency += self.bike.collected_currency

        self.road.set_state(State.FINISH)
        self.road.unschedule_events()

        # show finish information
        screen = GetObject(self.road).screen
        scene = GetObject(self.road).scene
        start_timer = Label(markup=True, font_size=20)
        start_timer.text = Finish.start_timer_text(self.road, self.bike)
        screen.ids['start_timer'] = start_timer
        scene.add_widget(start_timer)
        scene.start_timer_draw_background()
