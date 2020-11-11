from utils.state import State
from tests.event.landing.base_landing_test import BaseLandingTest


class LandingEventAndRelaxFailTest(BaseLandingTest):
    # move

    def test_landing_move_should_fail(self):
        self.set_app()
        self.landing_move_equal()

        self.road.wait_start()
        self.assertNotEqual(self.road.state, State.ON_RELAX_START)
        self.assertEqual(self.road.state, State.ON_LANDING_MOVE)

        self.road.on_wait(.1)
        self.assertNotEqual(self.road.state, State.ON_WAIT_MOVE)
        self.assertEqual(self.road.state, State.ON_LANDING_MOVE)

        self.road.wait_stop()
        self.assertNotEqual(self.road.state, State.ON_WAIT_STOP)
        self.assertEqual(self.road.state, State.ON_LANDING_MOVE)

    # stop

    def test_landing_stop_for_relax_move_should_fail(self):
        self.set_app()
        self.landing_stop_equal()
