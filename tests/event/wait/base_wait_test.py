from utils.state import State
from tests.base_gui_test import BaseGameScreenGUITest


class BaseWaitTest(BaseGameScreenGUITest):
    def _init_properties(self):
        self.road.landing_stop()

    def set_app(self):
        super().set_app()
        self._init_properties()

    def set_app_start(self):
        self.set_app()
        self.wait_start_equal()

    def set_app_move(self):
        self.set_app()
        self.wait_move_equal()

    def set_app_stop(self):
        self.set_app()
        self.wait_stop_equal()

    def assert_equal_wait_move(self):
        self.assertEqual(self.road.state, State.ON_WAIT_MOVE)

    def assert_equal_wait_stop(self):
        self.assertEqual(self.road.state, State.ON_WAIT_STOP)

    def wait_start_equal(self):
        self.road.landing_stop()
        self.road.wait_start()
        self.assertEqual(self.road.state, State.ON_WAIT_START)

    def wait_move_equal(self):
        self.bike.power = self.bike.max_power / 2
        self.road.on_wait(.1)
        self.assert_equal_wait_move()

    def wait_stop_equal(self):
        self.bike.power = self.bike.max_power
        self.road.on_wait(.1)
        self.road.wait_stop()
        self.assertEqual(self.road.state, State.ON_WAIT_STOP)
