from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import ObjectProperty, NumericProperty
from kivy.uix.behaviors.button import ButtonBehavior
from kivy.uix.image import Image
from conf import SECOND_GAME
from label.status_bar import StatusBar
from utils.dir import abstract_path
from utils.get_object import GetObject
from utils.sizes import GOSize as GOS

Builder.load_file(abstract_path('button/left_button.kv'))


class LeftButtonWidget(ButtonBehavior, Image):
    height = NumericProperty(GOS.WH_BUTTON_LR.value)
    width = NumericProperty(GOS.WH_BUTTON_LR.value)
    road = ObjectProperty(None)
    bike = ObjectProperty(None)
    background = ObjectProperty(None)

    @classmethod
    def set_objects(cls):
        cls.status_bar = StatusBar()
        cls.road = cls.status_bar.get_road()
        cls.bike = cls.status_bar.get_bike()
        cls.background = cls.status_bar.get_background()

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
        if not self.bike and not self.road:
            self.set_objects()

        curtain = GetObject(self.road).curtain
        if curtain.text == '':
            self.button_state_style()
            self._road_manage_events(is_press=True)

    def on_release(self):
        print('BTN: on_release')
        if not self.bike and not self.road:
            self.set_objects()

        curtain = GetObject(self.road).curtain
        if curtain.text == '':
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

    def _background_manage_events(self, is_press=False, is_release=False):
        print('BTN: _background_manage_events')
        if self.bike.speed <= 0:
            # Clock.unschedule(self.background.relax_mountains)
            if hasattr(self.background.relax_mountains, 'cancel'):
                self.background.relax_mountains.cancel()

            Clock.schedule_interval(self.background.stop_mountains, SECOND_GAME)
        else:
            raise 0
