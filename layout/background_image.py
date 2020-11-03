from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from label.status_bar import StatusBar
from utils.texture import redraw_texture
from utils.state import State
from conf import SECOND_GAME


class BackgroundImageAnimation(Widget):
    mountains_texture = ObjectProperty(Image(source='layout/mountains-1.png').texture)
    cloud_big_texture = ObjectProperty(Image(source='layout/cloud-big.png').texture)
    cloud_middle_texture = ObjectProperty(Image(source='layout/cloud-middle.png').texture)
    cloud_min_texture = ObjectProperty(Image(source='layout/cloud-min.png').texture)

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
        print(0.1)
        print('go_mountains')
        if StatusBar.get_road().has_finished():
            return False
        else:
            def set_ivpos(texture):
                return texture.uvpos[0] + dt/10, texture.uvpos[1]
            self.mountains_texture.uvpos = set_ivpos(self.mountains_texture)

            self.repeat_wrap(self.mountains_texture)
            redraw_texture(self, 'mountains_texture')

    def go_mountains_start(self):
        print('go_mountains_start')
        print(0.2)
        road = StatusBar.get_road()
        if road.state in (State.ON_RELAX_MOVE, State.ON_RELAX_STOP,
                          State.ON_GO_START, State.NONE):
            Clock.schedule_interval(self.go_mountains, SECOND_GAME)

    def go_mountains_stop(self):
        print('go_mountains_ STOP')

        road = StatusBar.get_road()
        if road.state in (State.ON_GO_MOVE, State.ON_GO_START):
            Clock.unschedule(self.go_mountains)

    # relax mountains --

    def relax_mountains(self, dt):
        print('*************** Relax relax_mountains --')
        print(0.3)
        if StatusBar.get_road().has_finished():
            pass
        else:
            bike = StatusBar.get_bike()
            if bike.speed <= 0:
                return False

            def set_ivpos(texture):
                return texture.uvpos[0] + dt/10, texture.uvpos[1]
            self.mountains_texture.uvpos = set_ivpos(self.mountains_texture)

            self.repeat_wrap(self.mountains_texture)
            redraw_texture(self, 'mountains_texture')

    def relax_mountains_start(self):
        print('0 relax_mountains_start')
        print(0.4)
        road = StatusBar.get_road()
        bike = StatusBar.get_bike()
        if road.state not in (State.ON_JUMP_UP_MOVE, State.ON_GO_STOP, State.ON_JUMP_LANDING_STOP):
            road.state = State.ON_RELAX_START
            road.on_relax_start()
            bike.anim_relax()

    def relax_mountains_stop(self):
        print('relax_mountains_stop')
        print(0.5)
        road = StatusBar.get_road()
        bike = StatusBar.get_bike()
        if road.state in (State.ON_RELAX_MOVE, State.ON_RELAX_STOP):
            road.on_relax_stop()
            bike.anim_wait()
