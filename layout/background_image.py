import os
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from label.status_bar import StatusBar
from utils.texture import redraw_texture
from utils.validation import ValidObject
from utils.state import State

from conf import SECOND_GAME


mountains_texture_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'mountains-1.png'))
cloud_big_texture_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'cloud-big.png'))
cloud_middle_texture_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'cloud-middle.png'))
cloud_min_texture_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'cloud-min.png'))


class BackgroundImageAnimation(Widget):
    mountains_texture = ObjectProperty(Image(source=mountains_texture_path).texture)
    cloud_big_texture = ObjectProperty(Image(source=cloud_big_texture_path).texture)
    cloud_middle_texture = ObjectProperty(Image(source=cloud_middle_texture_path).texture)
    cloud_min_texture = ObjectProperty(Image(source=cloud_min_texture_path).texture)

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

    # mountains textures

    # event
    # go_mountains --
    def go_mountains(self, dt):
        # print('go_mountains INNER',  self.get_road().state)
        if self.get_road().has_finished():
            return False
        else:
            def set_ivpos(texture):
                return texture.uvpos[0] + dt/10, texture.uvpos[1]
            self.mountains_texture.uvpos = set_ivpos(self.mountains_texture)

            self.repeat_wrap(self.mountains_texture)
            redraw_texture(self, 'mountains_texture')

    def go_mountains_start(self):
        #print('go_mountains_start',  self.get_road().state)
        road = self.get_road()
        if road.state in (State.ON_RELAX_MOVE, State.ON_RELAX_STOP,
                          State.ON_GO_START, State.NONE):
            Clock.schedule_interval(self.go_mountains, SECOND_GAME)

    def go_mountains_stop(self):
        #print('go_mountains_ STOP', self.get_road().state)

        road = StatusBar.get_road()
        if road.state in (State.ON_GO_MOVE, State.ON_GO_START):
            Clock.unschedule(self.go_mountains)

    # relax mountains --

    def relax_mountains(self, dt):
        print('*************** Relax relax_mountains --')
        if self.get_road().has_finished():
            pass
        else:
            bike = self.get_bike()
            if bike.speed <= 0:
                return False

            def set_ivpos(texture):
                return texture.uvpos[0] + dt/10, texture.uvpos[1]
            self.mountains_texture.uvpos = set_ivpos(self.mountains_texture)

            self.repeat_wrap(self.mountains_texture)
            redraw_texture(self, 'mountains_texture')

    def relax_mountains_start(self):
        #print('0 relax_mountains_start')
        road = self.get_road()
        bike = self.get_bike()
        if road.state not in (State.ON_JUMP_MOVE, State.ON_GO_STOP, State.ON_LANDING_STOP):
            road.state = State.ON_RELAX_START
            road.on_relax_start()
            bike.anim_relax()

    def relax_mountains_stop(self):
        #print('relax_mountains_stop')
        road = self.get_road()
        bike = self.get_bike()
        if road.state in (State.ON_RELAX_MOVE, State.ON_RELAX_STOP):
            road.on_relax_stop()
            bike.anim_wait()

   # get game objects

    # def game_objects(self):
    #     return {
    #         'status_bar': self.get_status_bar(),
    #         'road': self,
    #         'bike': self.get_bike(),
    #         'rock': self.get_rock(),
    #         'finish': self.get_finish()}
    #

    def get_road(self):
        return ValidObject.road(self.parent.children[1])

    # def get_status_bar(self):
    #     return ValidObject.status_bar(self.parent.children[2])
    #
    # def get_tools(self):
    #     return ValidObject.tools(self.parent.parent.children[0])

    def get_bike(self):
        return ValidObject.bike(self.parent.children[0])  # if self.parent else StatusBar.get_bike()
    #
    # def get_rock(self):
    #     try:
    #         if len(self.children) > 1:
    #             return ValidObject.rock(self.children[1])
    #     except IndexError as e:
    #         print('[EXCEPT] the `Rock` item does not exist on the `Road`!')
    #
    # def get_finish(self):
    #     return ValidObject.finish(self.children[0])
