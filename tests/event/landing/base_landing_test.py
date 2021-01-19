from utils.state import State
from tests.base_gui_test import BaseGameScreenGUITest


class BaseLandingTest(BaseGameScreenGUITest):
    def set_app(self):
        super().set_app()
        self._init_properties()

    def _init_properties(self):
        self.bike.power = 150
        self.bike.y = self.road.line_points[-1] + 100
        self.road.landing_start()

    def landing_start_equal(self):
        self.bike.y = self.road.line_points[-1] + 200

        self.road.set_state(State.ON_JUMP_STOP)
        self.road.landing_start()
        self.assertEqual(self.road.state, State.ON_LANDING_START)

    def landing_move_equal(self):
        self.bike.y = self.road.line_points[-1] + 100
        self.road.on_landing(.1)
        self.assertEqual(self.road.state, State.ON_LANDING_MOVE)

    def landing_stop_equal(self):
        """
        The `road.landing_stop` state doesn't exist. It can be `relax_start` Or `wait_start`
        """
        # It is need for you, probably:
        # self.assertEqual(self.road.state, State.ON_LANDING_STOP)
        pass

