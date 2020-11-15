from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import NumericProperty, ObjectProperty, ListProperty, OptionProperty
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from label.status_bar import StatusBar
from road.events import RoadEvents
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
    total_way = NumericProperty(1000)
    distance_traveled = NumericProperty(0)
    gravity = NumericProperty(2)
    state = OptionProperty(State.NONE, options=State.list_states())
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

    def game_objects(self):
        return {
            'status_bar': self.get_status_bar(),
            'road': self,
            'bike': self.get_bike(),
            'rock': self.get_rock(),
            'start': self.get_start(),
            'finish': self.get_finish()}

    def get_status_bar(self):
        if len(self.children) > 1:
            return ValidObject.status_bar(self.parent.children[2])
        else:
            return StatusBar.get_status_bar()

    def get_tools(self):
        return ValidObject.tools(self.parent.parent.children[0])

    def get_bike(self):
        return self.parent and ValidObject.bike(self.parent.children[0])

    def get_rock(self):
        if len(self.children) > 1:
            return ValidObject.rock(self.children[1])
        else:
            #print('[EXCEPT] the `Rock` item does not exist on the `Road`!')
            pass

    def get_start(self):
        if len(self.children) > 1:
            return ValidObject.start(self.children[2])
        else:
            return StatusBar.get_start()

    def get_finish(self):
        if len(self.children) > 1:
            return ValidObject.finish(self.children[0])
        else:
            return StatusBar.get_finish()

    def get_road(self):
        return self or StatusBar.get_road()
