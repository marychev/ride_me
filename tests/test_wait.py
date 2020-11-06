from tests.base_gui_test import BaseGameScreenGUITest
from utils.state import State


class WaitTest(BaseGameScreenGUITest):
    def set_app(self):
        super().set_app()
        self.road.landing_stop()

    def test_wait_start(self):
        self.set_app()
        self.road.landing_stop()
        self.road.wait_start()
        self.assertEqual(self.road.state, State.ON_WAIT_START)

    def test_wait_move(self):
        self.set_app()
        self.bike.power = self.bike.max_power/2
        self.road.on_wait(.1)
        self.assertEqual(self.road.state, State.ON_WAIT_MOVE)

    def test_wait_stop(self):
        self.set_app()
        self.bike.power = self.bike.max_power
        self.road.on_wait(.1)

        self.road.wait_stop()
        self.assertEqual(self.road.state, State.ON_WAIT_STOP)
