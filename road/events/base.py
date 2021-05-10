import time
from typing import Union

from kivy.app import App
from kivy.clock import Clock
from kivy.event import EventDispatcher
from kivy.properties import ObjectProperty
from objects import Finish
from utils.state import State
from label.curtain import Curtain


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
            if not self.bike and hasattr(ids, 'bike') and ids['bike']:
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
        curtain = Curtain(road=self.road)
        curtain.text = Finish.curtain_text(self.road, self.bike)
        curtain.add_to_game_screen()

    def set_bike_acceleration_for_landing(self, dt: Union[float, int]):
        self.bike.acceleration += dt * self.road.gravity

    def get_bike_y_for_landing(self) -> Union[float, int]:
        return self.bike.acceleration + (self.bike.power/self.bike.max_power)
