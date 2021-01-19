from kivy.lang import Builder
from button.left_button import LeftButtonWidget
from utils.dir import abstract_path

Builder.load_file(abstract_path('button/right_button.kv'))


class RightButtonWidget(LeftButtonWidget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.register_event_type('on_double_press')
        self.register_event_type('on_double_release')
        if kwargs.get("on_double_press") is not None:
            self.bind(on_double_press=kwargs.get('on_double_press'))
        if kwargs.get("on_double_release") is not None:
            self.bind(on_double_press=kwargs.get('on_double_release'))

    def on_touch_down(self, touch):
        print('on_touch_down')
        if touch.is_double_tap:
            self.dispatch('on_double_press', touch)
            return True
        return super().on_touch_down(touch)

    def on_touch_up(self, touch):
        print('on_touch_up')
        if touch.is_double_tap:
            self.dispatch('on_double_release', touch)
            return True
        return super().on_touch_up(touch)

    def on_press(self):
        super().on_press()
        self._background_manage_events(is_press=True)

    def on_release(self):
        super().on_release()
        self._background_manage_events(is_release=True)

    def on_double_press(self, touch):
        print('Right BTN: on_double_press')
        if not self.bike and not self.road:
            self.set_objects()
        self._road_manage_events(is_double_press=True)

    def on_double_release(self, touch):
        print('Right BTN: on_double_release')
        if not self.bike and not self.road:
            self.set_objects()
        self._road_manage_events(is_double_release=True)

    def _road_manage_events(self, is_press=False, is_release=False,
                            is_double_press=False, is_double_release=False):
        print('Right BTN: _road_manage_events')
        if is_press:
            if not self.bike.is_in_sky():
                self.road.relax_stop()
                self.road.go_start()

        elif is_release:
            if not self.bike.is_in_sky():
                self.road.landing_stop()
                self.road.go_stop()
                self.road.relax_start()

        elif is_double_press:
            self.road.relax_stop()
            self.road.jump_start()

        elif is_double_release:
            if self.bike.is_in_sky():
                self.road.jump_stop()
                self.road.landing_start()
        else:
            raise 0

    def _background_manage_events(self, is_press=False, is_release=False):
        print('Right BTN: _background_manage_events')
        if self.background.is_repeat_texture and (is_press or is_release):
            self.background.go_mountains_start()
