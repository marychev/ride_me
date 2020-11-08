from utils.state import State
from tests.base_gui_test import BaseGameScreenGUITest


class RelaxTest(BaseGameScreenGUITest):
    def set_app(self):
        super().set_app()
        self.bike.speed = 10
        self.road.landing_stop()

    def test_relax_start(self):
        self.set_app()
        self.road.relax_start()
        self.assertEqual(self.road.state, State.ON_RELAX_START)

    def test_relax_move(self):
        self.set_app()
        self.bike.speed = 5
        self.road.on_relax(.1)
        self.assertEqual(self.road.state, State.ON_RELAX_MOVE)

    def test_relax_stop(self):
        self.set_app()
        self.bike.speed = 1
        self.road.relax_stop()
        self.assertEqual(self.road.state, State.ON_RELAX_STOP)
