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

    @staticmethod
    def change_text(widget, text='...'):
        widget.text = text

    def button_state_style(self):
        if 'down' in self.state:
            self.canvas.opacity = 0.5
            self.disabled = True
        elif 'normal' in self.state:
            self.canvas.opacity = 1
            self.disabled = False
        else:
            raise 0

    def on_press(self):
        self.button_state_style()
        self._road_manage_events(is_press=True)
        StatusBar.get_bike().anim_stop()

    def on_release(self):
        self.button_state_style()
        self._road_manage_events(is_release=True)
        StatusBar.get_bike().anim_relax()

    def _road_manage_events(self, is_press=False, is_release=False):
        road = StatusBar.get_road()
        if is_press:
            Clock.unschedule(road.relax)
            Clock.schedule_interval(road.stop, SECOND_GAME)
        elif is_release:
            Clock.unschedule(road.stop)
            Clock.schedule_interval(road.relax, SECOND_GAME)
        else:
            raise 0

    def _bg_animation_manage_events(self, is_press=False, is_release=False):
        bg_animation = StatusBar.get_background_image_animation()
        bike = StatusBar.get_bike()
        if bike.speed <= 0:
            Clock.unschedule(bg_animation.relax_mountains)
            Clock.schedule_interval(bg_animation.stop_mountains, SECOND_GAME)
