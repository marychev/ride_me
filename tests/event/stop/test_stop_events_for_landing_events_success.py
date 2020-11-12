from tests.event.stop.base_stop_test import BaseStopTest
from utils.state import State


class StopEventAndLandingSuccessTest(BaseStopTest):
    # stop

    def test_stop_stop_in_landing_start_should_success(self):
        self.set_app()
        self.stop_stop_equal()
        self.road.landing_start()
        self.assertEqual(self.road.state, State.ON_LANDING_START)
        self.assertNotEqual(self.road.state, State.ON_WAIT_START)
