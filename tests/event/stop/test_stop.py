from tests.base_gui_test import BaseGameScreenGUITest
from utils.state import State


class StopTest(BaseGameScreenGUITest):
    def set_app(self):
        super().set_app()
        self.road.landing_stop()
        self.road.wait_start()

    def test_stop_start(self):
        self.set_app()
        self.bike.speed = 100
        self.road.on_go(0.1)
        self.road.stop_start()
        self.assertEqual(self.road.state, State.ON_STOP_START)

    def test_stop_move(self):
        self.set_app()
        self.bike.speed = 50
        self.road.stop_start()
        self.road.on_stop(.1)
        self.assertEqual(self.road.state, State.ON_STOP_MOVE)

    def test_stop_stop_to_wait(self):
        self.set_app()
        self.road.stop_stop()
        self.assertNotEqual(self.road.state, State.ON_STOP_STOP)
        self.assertEqual(self.road.state, State.ON_WAIT_START)
