from tests.event.landing.base_landing_test import BaseLandingTest
from utils.state import State


class LandingTest(BaseLandingTest):
    def test_landing_start(self):
        self.set_app()
        self.road.landing_start()

    def test_landing_move(self):
        self.set_app()
        self.landing_move_equal()

    def test_landing_stop(self):
        self.set_app()
        self.landing_stop_equal()

    def test_bike_has_landed_already(self):
        self.set_app()
        self.bike.y = self.road.line_points[-1]
        self.road.on_landing(.1)
        self.assertEqual(self.road.state, State.ON_WAIT_START)

    def test_start_and_end_landing_success(self):
        self.set_app()
        self.road.set_state(State.ON_WAIT_START)
        self.assertEqual(self.road.state, State.ON_WAIT_START)

        self.bike.y = self.road.line_points[-1] + self.road.height + 10
        self.road.on_landing(.1)
        self.assertEqual(self.road.state, State.ON_LANDING_MOVE)

        # bike is waiting for something actions Set Stop state
        self.bike.y = self.road.line_points[-1]
        self.road.on_wait(.1)
        self.assertEqual(self.road.state, State.ON_WAIT_MOVE)

        # bike has ended to wait. Set Stop state
        self.bike.power = self.bike.max_power
        self.road.on_wait(.1)
        self.assertEqual(self.road.state, State.ON_WAIT_STOP)
