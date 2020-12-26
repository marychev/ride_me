from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import ObjectProperty, ListProperty
from kivy.uix.behaviors.button import ButtonBehavior
from kivy.core.window import Window
from kivy.uix.image import Image
from conf import SECOND_GAME
from label.status_bar import StatusBar
from utils.counter import CounterClock
from utils.dir import abstract_path

Builder.load_file(abstract_path('button/left_button.kv'))

BUTTON_WIDTH = int(Window.width / 9)


class LeftButtonWidget(ButtonBehavior, Image):
    counter = ObjectProperty(CounterClock())
    btn_size = ListProperty([BUTTON_WIDTH, BUTTON_WIDTH])
    status_bar = ObjectProperty(None)
    road = ObjectProperty(None)
    bike = ObjectProperty(None)
    bg_animation = ObjectProperty(None)

    @classmethod
    def set_objects(cls):
        print('Left/RightButtonWidget: set object')
        cls.status_bar = StatusBar()
        cls.road = cls.status_bar.get_road()
        cls.bike = cls.status_bar.get_bike()
        cls.bg_animation = cls.status_bar.get_background_image_animation()

    def button_state_style(self):
        if 'down' in self.state:
            self.canvas.opacity = 0.5
            self.disabled = True
        elif 'normal' in self.state:
            self.canvas.opacity = 1
            self.disabled = False
        else:
            raise 0

    # events --

    def on_press(self):
        print('BTN: on_press')
        self.set_objects()
        self.button_state_style()
        self._road_manage_events(is_press=True)

    def on_release(self):
        print('BTN: on_release')
        self.set_objects()
        self.button_state_style()
        self._road_manage_events(is_release=True)

    def _road_manage_events(self, is_press=False, is_release=False):
        print('BTN: _road_manage_events')
        if is_press:
            self.road.relax_stop()
            self.road.stop_start()
        elif is_release:
            self.road.stop_stop()
            self.road.relax_start()
        else:
            raise 0

    def _bg_animation_manage_events(self, is_press=False, is_release=False):
        print('BTN: _bg_animation_manage_events')
        if self.bike.speed <= 0:
            Clock.unschedule(self.bg_animation.relax_mountains)
            Clock.schedule_interval(self.bg_animation.stop_mountains, SECOND_GAME)
        else:
            raise 0
