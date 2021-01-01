from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import NumericProperty, ObjectProperty, ListProperty, OptionProperty
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from label.status_bar import StatusBar
from road.events import RoadEvents
from level import LevelOne
from utils.dir import abstract_path
from utils.state import State
from utils.texture import repeat_texture, set_texture_uvpos
from utils.validation import ValidObject

Builder.load_file(abstract_path('road/road.kv'))

road_images = {
    'road_1': abstract_path('road/img/road-01.png'),
    'road_2': abstract_path('road/img/road-2-1.png'),
    'road_3': abstract_path('road/img/road-asphalt-0.jpg'),
    'road_4': abstract_path('road/img/road-asphalt-01.jpg'),
    'road_5': abstract_path('road/img/road-asphalt-02.jpg')
}


class Road(Widget, RoadEvents):
    road = ObjectProperty(None)
    bike = ObjectProperty(None)
    texture = ObjectProperty(Image(source=road_images['road_5']).texture)
    total_way = NumericProperty(420)
    distance_traveled = NumericProperty(0)
    gravity = NumericProperty(9.0)
    state = OptionProperty(State.NONE, options=State.list_states())
    line_points = ListProperty([100, 100, 1000, 100])
    last_states = ListProperty()

    def __init__(self, **kwargs):
        super(Road, self).__init__(**kwargs)

        repeat_texture(self.texture, int(Window.width / self.texture.width))
        self.landing_start()

    def get_distance_traveled(self):
        return self.x + self.get_bike().speed

    def set_distance_traveled(self):
        self.distance_traveled += self.get_distance_traveled()
        set_texture_uvpos(self, self.texture.uvpos[0] + self.get_bike().speed/self.texture.size[0], self.texture.uvpos[1])
        self.clear_game_objects()

    def has_finished(self):
        return self.distance_traveled >= self.total_way

    def set_state(self, name, count=5):
        self.state = name
        self.last_states.append(name)
        if len(self.last_states) > count:
            del self.last_states[0]
            del self.last_states[1]

    def unschedule_events(self):
        bg_animation = StatusBar.get_background_image_animation()
        self.jump_stop()
        self.go_stop()
        self.relax_stop()
        bg_animation and bg_animation.go_mountains_stop()

    def clear_game_objects(self):
        level = LevelOne(self, self.get_bike())
        level.remove_start()
        level.remove_rock()
        level.remove_puddles()
        level.remove_lamps()

    # get game objects

    def get_tools(self):
        return ValidObject.tools(self.parent.parent.children[0])

    def get_bike(self):
        return self.parent and ValidObject.bike(self.parent.children[0])

    def get_background(self):
        return self.parent and ValidObject.background(self.parent.children[2])

    def get_rocks(self):
        level = LevelOne(self, self.get_bike())
        return level.rocks()

    def get_puddles(self):
        level = LevelOne(self, self.get_bike())
        return level.puddles()

    def get_lamps(self):
        level = LevelOne(self, self.get_bike())
        lamps = level.lamps()
        return lamps

    def get_start(self):
        level = LevelOne(self, self.get_bike())
        return level.start()

    def get_finish(self):
        level = LevelOne(self, self.get_bike())
        return level.finish()

    def get_road(self):
        return self or StatusBar.get_road()
