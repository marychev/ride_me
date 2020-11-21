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
    texture = ObjectProperty(Image(source=road_images['road_5']).texture)
    total_way = NumericProperty(3000)
    distance_traveled = NumericProperty(0)
    gravity = NumericProperty(2)
    state = OptionProperty(State.NONE, options=State.list_states())

    line_points = ListProperty([100, 100, 1000, 100])

    last_states = ListProperty()

    road = ObjectProperty(None)
    bike = ObjectProperty(None)

    # rock = ObjectProperty(None)
    # puddle = ObjectProperty(None)
    # start = ObjectProperty(None)
    # finish = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(Road, self).__init__(**kwargs)

        repeat_texture(self.texture, int(Window.width / self.texture.width))
        self.landing_start()

    def get_distance_traveled(self):
        return self.x + self.get_bike().speed

    def set_distance_traveled(self):
        self.distance_traveled += self.get_distance_traveled()
        set_texture_uvpos(self, self.texture.uvpos[0] + self.get_bike().speed/self.texture.size[0], self.texture.uvpos[1])

        # remove old objects
        level = LevelOne(self, self.get_bike())
        level.remove_start()
        level.remove_rock()

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

    # get game objects

    def get_tools(self):
        return ValidObject.tools(self.parent.parent.children[0])

    def get_bike(self):
        return self.parent and ValidObject.bike(self.parent.children[0])

    def get_rocks(self):
        level = LevelOne(self, self.get_bike())
        rocks = level.rocks()
        return rocks

    def get_puddle(self):
        pass
        # if len(self.children) > 2:
        #     return ValidObject.puddle(self.children[2])
        # else:
        #     #print('[EXCEPT] the `Puddle` item does not exist on the `Road`!')
        #     pass

    def get_lamp(self):
        pass
        # if len(self.children) > 1:
        #     return ValidObject.lamp(self.children[1])
        # else:
        #     #print('[EXCEPT] the `Lamp` item does not exist on the `Road`!')
        #     pass

    def get_start(self):
        level = LevelOne(self, self.get_bike())
        start = level.start()
        return start

    def get_finish(self):
        if len(self.children) > 1:
            widgets = [w for w in self.road.children if w.__class__.__name__ == 'Finish']
            return ValidObject.finish(widgets[0]) if len(widgets) > 0 else None
        else:
            return StatusBar.get_finish()

    def get_road(self):
        return self or StatusBar.get_road()
