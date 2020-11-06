import os

from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import NumericProperty, ObjectProperty, ListProperty, OptionProperty
from kivy.uix.image import Image
from kivy.uix.widget import Widget

from label.status_bar import StatusBar
from layout.background_image import BackgroundImageAnimation
from road.events import RoadEvents
from utils.checks import set_texture_uvpos
from utils.state import State
from utils.validation import ValidObject

KV_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'road.kv'))
Builder.load_file(KV_PATH)

TEXTURE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'img/road-01.png'))


class Road(Widget, RoadEvents):
    texture = ObjectProperty(Image(source=TEXTURE_PATH).texture)
    total_way = NumericProperty(3000)
    distance_traveled = NumericProperty(0)
    gravity = NumericProperty(2)
    state = OptionProperty(State.NONE, options=State.list_states())
    last_states = ListProperty()

    def __init__(self, **kwargs):
        super(Road, self).__init__(**kwargs)

        BackgroundImageAnimation.repeat_wrap(self.texture, Window.width / self.texture.width)
        self.landing_start()

    def get_distance_traveled(self):
        return self.x + self.get_bike().speed

    def set_distance_traveled(self):
        self.distance_traveled += self.get_distance_traveled()
        set_texture_uvpos(self, self.texture.uvpos[0] + self.get_bike().speed, self.texture.uvpos[1])

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
        bg_animation.go_mountains_stop()
        bg_animation.relax_mountains_stop()

    def show_status(self, title='ROAD'):
        return '''
----------------------------------------------- [{}]
total_way:                    {}
distance_traveled:    {}
*left_go:                          {}'''.format(
            title,
            self.total_way,
            self.distance_traveled,
            self.total_way - self.distance_traveled,
        )

    # get game objects

    def game_objects(self):
        return {
            'status_bar': self.get_status_bar(),
            'road': self,
            'bike': self.get_bike(),
            'rock': self.get_rock(),
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

    def get_finish(self):
        if len(self.children) > 1:
            return ValidObject.finish(self.children[0])
        else:
            return StatusBar.get_finish()

    def get_road(self):
        return self or StatusBar.get_road()
