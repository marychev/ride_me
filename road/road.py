from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import NumericProperty, ObjectProperty, ListProperty, OptionProperty
from kivy.uix.image import Image
from kivy.uix.widget import Widget

from level.one.level_one import LevelOne
from road.events import RoadEvents
from utils.dir import abstract_path
from utils.get_object import GetObject
from utils.state import State
from utils.texture import repeat_texture, set_texture_uvpos

Builder.load_file(abstract_path('road/road.kv'))

road_images = {
    'road_1': abstract_path('road/img/road-01.png'),
    'road_2': abstract_path('road/img/road-2-1.png'),
    'road_3': abstract_path('road/img/road-asphalt-0.jpg'),
    'road_4': abstract_path('road/img/road-asphalt-01.jpg'),
    'road_5': abstract_path('road/img/road-asphalt-02.jpg')
}


class Road(Widget, RoadEvents):
    level = ObjectProperty(None)

    texture = ObjectProperty(Image(source=road_images['road_5']).texture)
    total_way = NumericProperty(88888888)
    distance_traveled = NumericProperty(0)
    gravity = NumericProperty(9.0)
    state = OptionProperty(State.NONE, options=State.list_states())
    line_points = ListProperty([100, 100, 1000, 100])
    last_states = ListProperty()

    def __init__(self, **kwargs):
        super(Road, self).__init__(**kwargs)

        self.road = self
        self.bike = self.get_bike()
        self.level = LevelOne(self, self.bike)

        repeat_texture(self.texture, int(Window.width / self.texture.width))

        # todo: auto-define
        self.landing_start()

    def get_distance_traveled(self):
        return self.x + self.bike.speed

    def set_distance_traveled(self):
        self.distance_traveled += self.get_distance_traveled()
        set_texture_uvpos(self, self.texture.uvpos[0] + self.bike.speed / self.texture.size[0], self.texture.uvpos[1])

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

    # get game objects

    def get_road(self):
        return self

    def get_tools(self):
        return GetObject(road=self).tools

    def get_bike(self):
        return GetObject(road=self).bike

    def get_background(self):
        return GetObject(road=self).background
