from utils.state import State
from tests.event.landing.base_landing_test import BaseLandingTest


class LandingEventAndWaitFailTest(BaseLandingTest):
    # start

    def test_landing_start_for_wait_start_should_fail(self):
        self.set_app()
        self.landing_start_equal()

        self.bike.y = self.road.line_points[-1]
        self.bike.power = 0
        self.bike.speed = 0

        self.road.wait_start()
        self.assertNotEqual(self.road.state, State.ON_WAIT_START)
        self.assertEqual(self.road.state, State.ON_LANDING_START)

    def test_landing_move_for_wait_start_state_should_fail(self):
        self.set_app()
        self.landing_move_equal()

        self.road.wait_start()
        self.assertNotEqual(self.road.state, State.ON_WAIT_START)
        self.assertEqual(self.road.state, State.ON_LANDING_MOVE)

        self.road.on_wait(.1)
        self.assertNotEqual(self.road.state, State.ON_WAIT_MOVE)
        self.assertEqual(self.road.state, State.ON_LANDING_MOVE)

        self.road.wait_stop()
        self.assertNotEqual(self.road.state, State.ON_WAIT_STOP)
        self.assertEqual(self.road.state, State.ON_LANDING_MOVE)

    # stop

    def test_landing_stop_for_wait_move_should_fail(self):
        self.set_app()
        self.road.set_state(State.ON_LANDING_STOP)
        self.road.on_wait(.1)
        self.assertNotEqual(self.road.state, State.ON_WAIT_MOVE)
        self.assertEqual(self.road.state, State.ON_LANDING_STOP)

    def test_landing_stop_for_wait_move_state_should_fail(self):
        self.set_app()
        self.road.set_state(State.ON_LANDING_STOP)
        self.road.wait_stop()
        self.assertNotEqual(self.road.state, State.ON_WAIT_STOP)
        self.assertEqual(self.road.state, State.ON_LANDING_STOP)
