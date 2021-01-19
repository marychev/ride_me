from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import ObjectProperty, BooleanProperty
from kivy.uix.widget import Widget
from layout.events.go_background import GoBackgroundDispatcher
from utils.texture import redraw_texture, image_texture, repeat_texture
from utils.validation import ValidObject


class Background(Widget, GoBackgroundDispatcher):
    texture = ObjectProperty(None)
    is_repeat_texture = BooleanProperty(False)
    cloud_big_texture = ObjectProperty(None)
    cloud_middle_texture = ObjectProperty(None)
    cloud_min_texture = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.after_init)

        self.texture = image_texture('layout/img/default.png')

        self.cloud_big_texture = image_texture('layout/img/cloud-big.png')
        self.cloud_middle_texture = image_texture('layout/img/cloud-middle.png')
        self.cloud_min_texture = image_texture('layout/img/cloud-min.png')

        Clock.schedule_interval(self.scroll_textures_clouds, 3/60)

        repeat_texture(self.cloud_big_texture, uvsize_x=Window.width/self.cloud_big_texture.width)
        repeat_texture(self.cloud_middle_texture, uvsize_x=Window.width/self.cloud_middle_texture.width)
        repeat_texture(self.cloud_min_texture, uvsize_x=Window.width/self.cloud_min_texture.width)

    def after_init(self, dt):
        print('[after_init--BaseDispatcher--2]')
        app = App.get_running_app()
        ids = app and app.root.current_screen.ids
        if ids and ids['road']:
            self.texture = ids['road'].level.background_texture

    # clouds textures --

    def scroll_textures_clouds(self, dt):
        # print('Background:scroll_textures_clouds')
        def __set_ivpos(texture):
            return (texture.uvpos[0] + dt / 2.0) % Window.width, texture.uvpos[1]

        self.cloud_min_texture.uvpos = __set_ivpos(self.cloud_min_texture)
        self.cloud_middle_texture.uvpos = __set_ivpos(self.cloud_middle_texture)
        self.cloud_big_texture.uvpos = __set_ivpos(self.cloud_big_texture)

        redraw_texture(self, 'cloud_min_texture')
        redraw_texture(self, 'cloud_middle_texture')
        redraw_texture(self, 'cloud_big_texture')

    # get game objects --

    def get_road(self):
        return self.parent and ValidObject.road(self.parent.children[1])

    def get_bike(self):
        return ValidObject.bike(self.parent.children[0])

    # def get_start(self):
    #     if len(self.children) > 1:
    #         return ValidObject.start(self.children[2])
    #
    # def get_finish(self):
    #     if len(self.children) > 1:
    #         return ValidObject.finish(self.children[0])
