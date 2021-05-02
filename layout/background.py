from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import ObjectProperty, BooleanProperty, StringProperty
from kivy.uix.widget import Widget
from layout.events.go_background import GoBackgroundDispatcher
from utils.texture import redraw_texture, image_texture, repeat_texture
from utils.validation import ValidObject
from utils.get_object import GetObject


class Background(Widget, GoBackgroundDispatcher):
    sid = StringProperty('background')
    texture = ObjectProperty(None)
    cloud_big_texture = ObjectProperty(None)
    cloud_middle_texture = ObjectProperty(None)
    cloud_min_texture = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.after_init)

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
        ids and hasattr(ids, 'road') and self.set_texture(ids['road'])

    def set_texture(self, road):
        """ self.texture = image_texture('layout/img/default.png') """
        if not self.texture and road:
            self.texture = road.level.background_texture

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
        return self.parent and ValidObject.road(GetObject.get_child(self.parent, 'Road'))

    def get_bike(self):
        return ValidObject.bike(GetObject.get_child(self.parent, 'Bike'))

