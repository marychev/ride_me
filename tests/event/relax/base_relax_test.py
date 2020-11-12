from utils.state import State
from tests.base_gui_test import BaseGameScreenGUITest


class BaseRelaxTest(BaseGameScreenGUITest):
    def set_app(self):
        super().set_app()
        self._init_properties()

    def _init_properties(self):
        self.bike.speed = 10
        self.road.landing_stop()

    def relax_start_equal(self):
        self.road.relax_start()
        self.assertEqual(self.road.state, State.ON_RELAX_START)

    def relax_move_equal(self):
        self.bike.speed = 5
        self.road.on_relax(.1)
        self.assertEqual(self.road.state, State.ON_RELAX_MOVE)

    def relax_stop_equal(self):
        self.bike.speed = 1
        self.road.relax_stop()
        self.assertEqual(self.road.state, State.ON_RELAX_STOP)
