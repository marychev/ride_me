from kivy.core.window import Window
from kivy.lang import Builder
from kivy.logger import Logger
from kivy.properties import NumericProperty, ObjectProperty, ListProperty, OptionProperty
from kivy.uix.widget import Widget

from level.one.level_one import LevelOne
from road.events import RoadEvents
from utils.dir import abstract_path
from utils.get_object import GetObject
from utils.state import State
from utils.texture import repeat_texture, set_texture_uvpos, image_texture
from utils.validation import ValidObject
from utils.init import app_config
from level.maps import get_by_title as get_map_by_title

Builder.load_file(abstract_path('road/road.kv'))


class Road(Widget, RoadEvents):
    level = ObjectProperty(None)
    texture = ObjectProperty(image_texture('road/img/road-asphalt.png'))
    total_way = NumericProperty(0)         # todo: need to fix tests
    distance_traveled = NumericProperty(0)
    gravity = NumericProperty(9.0)
    state = OptionProperty(State.NONE, options=State.list_states())
    last_states = ListProperty()
    line_points = ListProperty([100, 100, 1000, 100])

    def __init__(self, **kwargs):
        super(Road, self).__init__(**kwargs)
        self.bike = self.bike if self.bike else self.get_bike()
        self.init_app_config()

        if self.bike:
            self.set_state(State.NONE)
            self.landing_start()

    def init_app_config(self):
        if not self.level:
            self.set_state(State.INIT)
            self.road = self
            self.bike = self.bike if self.bike else self.get_bike()
            # TODO: define a Level from App Config
            self.level = LevelOne(self, self.bike)                      # todo: fix here init with app config

        if self.level:
            self.texture = self.level.road_texture
            self.total_way = self.road.total_way = self.level.total_way(self.level.map)

            # set background texture
            if self.parent:
                game_screen = ValidObject.screen(self.parent.parent)
                _map = get_map_by_title(app_config('map', 'title'))
                background = game_screen.ids['background']

                if background and _map:
                    background.texture = image_texture(_map['source'])

        repeat_texture(self.texture, int(Window.width / self.texture.width))

    def get_distance_traveled(self):
        try:
            return self.x + self.bike.speed
        except AttributeError as e:
            text = '{}.\n\tCause: Bike does not exist.\n\tTip: Need to set the bike.'.format(e)
            # Logger.exception(text)
            # raise AttributeError(text)
            print('[ERROR-1]')

    def set_distance_traveled(self):
        self.distance_traveled += self.get_distance_traveled()
        set_texture_uvpos(self, self.texture.uvpos[0] + self.bike.speed / self.texture.size[0], self.texture.uvpos[1])
        ValidObject.scene(self.parent).define_and_add_map_elements()

    def has_finished(self):
        return self.distance_traveled >= self.total_way

    def set_state(self, name, count=5):
        self.state = name
        self.last_states.append(name)
        if len(self.last_states) > count:
            del self.last_states[0]
            del self.last_states[1]

    def unschedule_events(self):
        background = self.get_background()
        self.jump_stop()
        self.go_stop()
        self.relax_stop()
        background.go_mountains_stop()

    def passed(self, pos):
        return int(self.distance_traveled) > (pos[0])

    def visible(self, pos):
        return int(self.distance_traveled) < int(pos[0]) < int(self.distance_traveled) + int(Window.width)

    def future(self, pos):
        return int(self.distance_traveled) + int(Window.width) < int(pos[0])

    # get game objects

    def get_road(self):
        return self

    def get_tools(self):
        return GetObject(road=self).tools

    def get_bike(self):
        return GetObject(road=self).bike

    def get_background(self):
        return GetObject(road=self).background
