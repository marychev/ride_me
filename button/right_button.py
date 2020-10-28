from kivy.clock import Clock
from kivy.lang import Builder
from button.left_button import LeftButtonWidget
from conf import SECOND_GAME

Builder.load_file('button/right_button.kv')


class RightButtonWidget(LeftButtonWidget):

    def on_press(self):
        self.set_objects()
        self.button_state_style()
        self.counter.start()
        self._road_manage_events(is_press=True)
        self._bg_animation_manage_events(is_press=True)
        self._bike_manage_events(is_press=True)

    def on_release(self):
        self.button_state_style()
        self.counter.stop()
        self._road_manage_events(is_release=True)
        self._bg_animation_manage_events(is_release=True)
        self._bike_manage_events(is_release=True)

    def _road_manage_events(self, is_press=False, is_release=False):
        if is_press:
            extra_acceleration = self.counter.count / 4
            self.bike.acceleration += extra_acceleration
            Clock.unschedule(self.road.relax)
            Clock.schedule_interval(self.road.go, SECOND_GAME)
        elif is_release:
            Clock.unschedule(self.road.go)
            Clock.schedule_interval(self.road.relax, SECOND_GAME)
        else:
            raise 0

    def _bg_animation_manage_events(self, is_press=False, is_release=False):
        if is_press:
            Clock.unschedule(self.bg_animation.relax_mountains)
            Clock.schedule_interval(self.bg_animation.go_mountains, SECOND_GAME)
        elif is_release:
            Clock.unschedule(self.bg_animation.go_mountains)
            Clock.schedule_interval(self.bg_animation.relax_mountains, SECOND_GAME)
        else:
            raise 0

    def _bike_manage_events(self, is_press=False, is_release=False):
        if is_press:
            self.bike.anim_go()
        elif is_release:
            self.bike.anim_relax()
        else:
            raise 0
