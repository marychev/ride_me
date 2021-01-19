from kivy.app import App
from kivy.clock import Clock
from kivy.event import EventDispatcher
from kivy.properties import ObjectProperty

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
        root_ids = app and app.root.current_screen.ids
        if root_ids:
            if not self.bike and root_ids.get('bike'):
                self.bike = root_ids['bike']
            if not self.road and root_ids.get('road'):
                self.road = root_ids['road']

    def set_distances(self):
        self.road.set_distance_traveled()

        # self.start and self.start.set_x()
        # if len(self.rocks) > 0:
        #     [rock.set_x() for rock in self.rocks]
        # if len(self.puddles) > 0:
        #     [puddle.set_x() for puddle in self.puddles]
        # if len(self.lamps) > 0:
        #     [lamp.set_x() for lamp in self.lamps]
        #
        # self.finish and self.finish.set_x()

    def road_finish(self):
        self.bike.power = 0
        self.bike.speed = 0
        self.bike.acceleration = 0

        self.road.set_state(State.FINISH)
        self.road.unschedule_events()

