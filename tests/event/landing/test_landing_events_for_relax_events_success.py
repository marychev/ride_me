from tests.event.landing.base_landing_test import BaseLandingTest
from utils.state import State


class LandingEventAndRelaxSuccessTest(BaseLandingTest):
    # stop

    def test_landing_stop_for_relax_start_should_success(self):
        self.set_app()
        self.road.set_state(State.ON_LANDING_STOP)

        self.bike.speed = 1
        self.road.relax_start()
        self.assertEqual(self.road.state, State.ON_RELAX_START)
        self.assertNotEqual(self.road.state, State.ON_LANDING_STOP)
