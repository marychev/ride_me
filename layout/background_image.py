from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.uix.widget import Widget

from conf import SECOND_GAME
from road.events.go import GoDispatcher
from utils.dir import abstract_path
from utils.state import State
from utils.texture import redraw_texture
from utils.validation import ValidObject


class BackgroundImageAnimation(Widget):
    mountains_texture = ObjectProperty(Image(source=abstract_path('layout/mountains-1.png')).texture)
    cloud_big_texture = ObjectProperty(Image(source=abstract_path('layout/cloud-big.png')).texture)
    cloud_middle_texture = ObjectProperty(Image(source=abstract_path('layout/cloud-middle.png')).texture)
    cloud_min_texture = ObjectProperty(Image(source=abstract_path('layout/cloud-min.png')).texture)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.scroll_textures_clouds, 3/60)

        self.repeat_wrap(self.cloud_big_texture, uvsize_x=Window.width/self.cloud_big_texture.width)
        self.repeat_wrap(self.cloud_middle_texture, uvsize_x=Window.width/self.cloud_middle_texture.width)
        self.repeat_wrap(self.cloud_min_texture, uvsize_x=Window.width/self.cloud_min_texture.width)

    @staticmethod
    def repeat_wrap(texture, uvsize_x=1, uvsize_y=-1):
        texture.wrap = 'repeat'
        texture.uvsize = (uvsize_x, uvsize_y)

    # clouds textures

    def scroll_textures_clouds(self, dt):
        def set_ivpos(texture):
            return (texture.uvpos[0] + dt / 2.0) % Window.width, texture.uvpos[1]

        self.cloud_min_texture.uvpos = set_ivpos(self.cloud_min_texture)
        self.cloud_middle_texture.uvpos = set_ivpos(self.cloud_middle_texture)
        self.cloud_big_texture.uvpos = set_ivpos(self.cloud_big_texture)

        redraw_texture(self, 'cloud_min_texture')
        redraw_texture(self, 'cloud_middle_texture')
        redraw_texture(self, 'cloud_big_texture')

    # imitation events
    # go_mountains --
    def go_mountains(self, dt):
        print('go_mountains INNER',  self.get_road().state)
        road = self.get_road()
        bike = self.get_bike()
        rock = self.get_rock()

        if road.has_finished():
            return False

        elif road.state == State.ON_RELAX_STOP:
            return False

        elif rock and bike.collide_widget(rock):
            return False

        else:
            uvpos_x = self.mountains_texture.uvpos[0] + (bike.speed * dt)/10.0
            self.mountains_texture.uvpos = uvpos_x, self.mountains_texture.uvpos[1]

            self.repeat_wrap(self.mountains_texture)
            redraw_texture(self, 'mountains_texture')
            return True

    def go_mountains_start(self):
        road = self.get_road()
        if road.state in GoDispatcher.start_states_list() + (State.ON_GO_START, ):
            Clock.schedule_interval(self.go_mountains, SECOND_GAME)

    def go_mountains_stop(self):
        road = self.get_road()
        if road.state in GoDispatcher.stop_states_list():
            Clock.unschedule(self.go_mountains)

    def get_road(self):
        return ValidObject.road(self.parent.children[1])

    # def get_status_bar(self):
    #     return ValidObject.status_bar(self.parent.children[2])
    #
    # def get_tools(self):
    #     return ValidObject.tools(self.parent.parent.children[0])

    def get_bike(self):
        return ValidObject.bike(self.parent.children[0])  # if self.parent else StatusBar.get_bike()

    def get_rock(self):
        try:
            if len(self.children) > 1:
                return ValidObject.rock(self.children[1])
        except IndexError as e:
            print('[EXCEPT] the `Rock` item does not exist on the `Road`!')
    #
    # def get_finish(self):
    #     return ValidObject.finish(self.children[0])
