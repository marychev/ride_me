from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.behaviors.button import ButtonBehavior
from kivy.uix.image import Image
from conf import SECOND_GAME
from label.status_bar import StatusBar
from utils.counter import CounterClock

Builder.load_file('button/left_button.kv')


class LeftButtonWidget(ButtonBehavior, Image):
    counter = ObjectProperty(CounterClock())

    status_bar = ObjectProperty(None)
    road = ObjectProperty(None)
    bike = ObjectProperty(None)
    bg_animation = ObjectProperty(None)

    @classmethod
    def set_objects(cls):
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

    # events

    def on_touch_down(self, touch):
        if touch.is_double_tap:
            self.dispatch('on_double_press', touch)
            return True
        return super().on_touch_down(touch)

    def on_press(self):
        self.set_objects()
        self.button_state_style()
        self._road_manage_events(is_press=True)
        self.bike.anim_stop()

    def on_release(self):
        self.button_state_style()
        self._road_manage_events(is_release=True)
        self.bike.anim_relax()

    def _road_manage_events(self, is_press=False, is_release=False):
        if is_press:
            self.road.on_relax_stop()
            Clock.schedule_interval(self.road.stop, SECOND_GAME)
        elif is_release:
            Clock.unschedule(self.road.stop)
            self.road.on_relax_start()
        else:
            raise 0

    def _bg_animation_manage_events(self, is_press=False, is_release=False):
        if self.bike.speed <= 0:
            Clock.unschedule(self.bg_animation.relax_mountains)
            Clock.schedule_interval(self.bg_animation.stop_mountains, SECOND_GAME)
