from utils.state import State
from tests.base_gui_test import BaseGameScreenGUITest


class BaseStopTest(BaseGameScreenGUITest):
    def set_app(self):
        super().set_app()
        self._init_properties()

    def _init_properties(self):
        self.road.landing_stop()
        self.road.wait_start()

    def stop_start_equal(self):
        self.bike.speed = 10
        self.road.on_relax(0.1)
        self.road.stop_start()
        self.assertEqual(self.road.state, State.ON_STOP_START)

    def stop_move_equal(self):
        self.set_app()
        self.bike.speed = 50
        self.road.stop_start()
        self.road.on_stop(.1)
        self.assertEqual(self.road.state, State.ON_STOP_MOVE)

    def stop_stop_equal(self):
        self.road.stop_stop()
        self.bike.speed = 0
        self.assertNotEqual(self.road.state, State.ON_STOP_STOP)
        self.assertEqual(self.road.state, State.ON_WAIT_START)
