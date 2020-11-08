from utils.state import State
from tests.base_gui_test import BaseGameScreenGUITest


class GoTest(BaseGameScreenGUITest):
    def set_app(self):
        super().set_app()
        self.bike.speed = 10
        self.bike.max_speed = 20
        self.road.landing_stop()

    def test_go_start(self):
        self.set_app()

        self.road.go_start()
        self.assertEqual(self.road.state, State.ON_GO_START)

    def test_go_move(self):
        self.set_app()
        self.bike.speed = self.bike.max_speed/2
        self.road.on_go(.1)
        self.assertEqual(self.road.state, State.ON_GO_MOVE)

    def test_go_stop(self):
        self.set_app()
        self.bike.speed = 0
        self.road.on_go(.1)
        self.road.go_stop()
        self.assertEqual(self.road.state, State.ON_GO_STOP)
