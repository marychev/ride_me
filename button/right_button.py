from kivy.clock import Clock
from kivy.lang import Builder
from button.left_button import LeftButtonWidget
from conf import SECOND_GAME

Builder.load_file('button/right_button.kv')


class RightButtonWidget(LeftButtonWidget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.register_event_type('on_double_press')

        if kwargs.get("on_double_press") is not None:
            self.bind(on_double_press=kwargs.get("on_double_press"))

    def on_press(self):
        self.set_objects()
        self.button_state_style()
        self.counter.start()
        self._road_manage_events(is_press=True)
        self._bg_animation_manage_events(is_press=True)

    def on_release(self):
        self.button_state_style()
        self.counter.stop()
        self._road_manage_events(is_release=True)
        self._bg_animation_manage_events(is_release=True)

    def on_double_press(self, touch):
        print('\rON PRESS DOUBLE JUMP\r', touch)
        self.status_bar or self.set_objects()
        self._road_manage_events(is_double_press=True)

    def _road_manage_events(self, is_press=False, is_release=False, is_double_press=False):
        if is_press:
            # # todo: acceleration
            # extra_acceleration = self.counter.count / 4
            # self.bike.set_acceleration(extra_acceleration)

            self.road.on_relax_stop()
            self.road.on_go_start()
        elif is_release:
            self.road.on_go_stop()
            self.road.on_relax_start()
        elif is_double_press:
            self.road.on_jump_start()
        else:
            raise 0

    def _bg_animation_manage_events(self, is_press=False, is_release=False):
        if is_press:
            self.bg_animation.relax_mountains_stop()
            self.bg_animation.go_mountains_start()
        elif is_release:
            self.bg_animation.go_mountains_stop()
            self.bg_animation.relax_mountains_start()
        else:
            raise 0
