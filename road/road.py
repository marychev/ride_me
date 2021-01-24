from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import NumericProperty, ObjectProperty, ListProperty, OptionProperty
from kivy.uix.widget import Widget

from level.one.level_one import LevelOne
from road.events import RoadEvents
from utils.dir import abstract_path
from utils.get_object import GetObject
from utils.state import State
from utils.texture import repeat_texture, set_texture_uvpos, image_texture
from utils.validation import ValidObject

Builder.load_file(abstract_path('road/road.kv'))


class Road(Widget, RoadEvents):
    level = ObjectProperty(None)
    texture = ObjectProperty(image_texture('road/img/road-asphalt.jpg'))
    total_way = NumericProperty(20000)
    distance_traveled = NumericProperty(0)
    gravity = NumericProperty(9.0)
    state = OptionProperty(State.NONE, options=State.list_states())
    last_states = ListProperty()
    line_points = ListProperty([100, 100, 1000, 100])

    def __init__(self, **kwargs):
        super(Road, self).__init__(**kwargs)

        self.road = self
        self.bike = self.get_bike()
        self.level = LevelOne(self, self.bike)

        # set level's options, textures, ...
        if self.level:
            self.texture = self.level.road_texture
            # !! self.road.total_way = finish.pos[0]

        repeat_texture(self.texture, int(Window.width / self.texture.width))

        # todo: auto-define
        self.landing_start()

    def get_distance_traveled(self):
        return self.x + self.bike.speed

    def set_distance_traveled(self):
        self.distance_traveled += self.get_distance_traveled()
        set_texture_uvpos(self, self.texture.uvpos[0] + self.bike.speed / self.texture.size[0], self.texture.uvpos[1])

        # todo: dev
        scene = self.parent
        scene.add_map_elements()

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
