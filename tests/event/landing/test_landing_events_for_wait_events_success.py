from utils.state import State
from tests.event.landing.base_landing_test import BaseLandingTest


class LandingEventAndWaitSuccessTest(BaseLandingTest):
    # stop

    def test_landing_stop_for_wait_start_should_success(self):
        self.set_app()
        self.road.set_state(State.ON_LANDING_STOP)

        self.road.wait_start()
        self.assertEqual(self.road.state, State.ON_WAIT_START)
        self.assertNotEqual(self.road.state, State.ON_LANDING_STOP)


