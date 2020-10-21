from kivy.clock import Clock
from kivy.lang import Builder
from button.left_button import LeftButtonWidget
from conf import SECOND_GAME
from kivy.animation import Animation
Builder.load_file('button/right_button.kv')


class RightButtonWidget(LeftButtonWidget):

    def on_press(self):
        self.button_state_style()
        self.counter.start()
        self._road_manage_events(is_press=True)
        self._bg_animation_manage_events(is_press=True)

        self.get_bike().anim_go()

    def on_release(self):
        self.button_state_style()
        self.counter.stop()
        self._road_manage_events(is_release=True)
        self._bg_animation_manage_events(is_release=True)

        self.get_bike().anim_relax()

    def _road_manage_events(self, is_press=False, is_release=False):
        road = self.get_road()
        if is_press:
            road.acceleration += self.counter.count
            Clock.unschedule(road.relax)
            Clock.schedule_interval(road.go, SECOND_GAME)
        elif is_release:
            Clock.unschedule(road.go)
            Clock.schedule_interval(road.relax, SECOND_GAME)
        else:
            raise 0

    def _bg_animation_manage_events(self, is_press=False, is_release=False):
        bg_animation = self.get_background_image_animation()
        if is_press:
            Clock.unschedule(bg_animation.relax_mountains)
            Clock.schedule_interval(bg_animation.go_mountains, SECOND_GAME)
        elif is_release:
            Clock.unschedule(bg_animation.go_mountains)
            Clock.schedule_interval(bg_animation.relax_mountains, SECOND_GAME)
        else:
            raise 0

