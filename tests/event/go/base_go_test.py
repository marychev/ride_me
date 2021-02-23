from utils.state import State
from tests.base_gui_test import BaseGameScreenGUITest


class BaseGoTest(BaseGameScreenGUITest):
    def set_app(self):
        super().set_app()
        self._init_properties()

    def set_app_start(self):
        self.set_app()
        self.go_start_equal()

    def set_app_move(self):
        self.set_app()
        self.go_move_equal()

    def set_app_stop(self):
        self.set_app()
        self.go_stop_equal()

    def _init_properties(self):
        self.bike.speed = 10
        self.bike.max_speed = 20
        self.road.bike = self.bike
        self.road.landing_stop()

    def go_start_equal(self):
        self.road.go_start()
        self.assertEqual(self.road.state, State.ON_GO_START)

    def go_move_equal(self):
        self.bike.speed = self.bike.max_speed/2
        self.road.on_go(.1)
        self.assertEqual(self.road.state, State.ON_GO_MOVE)

    def go_stop_equal(self):
        self.bike.speed = 0
        self.road.on_go(.1)
        self.road.go_stop()
        self.assertEqual(self.road.state, State.ON_GO_STOP)
