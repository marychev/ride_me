from utils.state import State
from tests.base_gui_test import BaseGameScreenGUITest


class BaseJumpTest(BaseGameScreenGUITest):
    def set_app(self):
        super().set_app()
        self._init_properties()

    def _init_properties(self):
        self.bike.power = 150
        self.road.landing_stop()
        self.road.wait_start()
        self.road.wait_stop()

    def jump_start_equal(self):
        self.road.jump_start()
        self.assertEqual(self.road.state, State.ON_JUMP_START)

    def jump_move_equal(self):
        self.bike.power = self.bike.max_power/2
        self.road.on_jump(.1)
        self.assertEqual(self.road.state, State.ON_JUMP_MOVE)

    def jump_stop_equal(self):
        self.bike.y = self.road.line_points[-1]*2
        self.bike.power = 1
        self.road.on_jump(.1)
        self.road.jump_stop()
        self.assertEqual(self.road.state, State.ON_JUMP_STOP)
