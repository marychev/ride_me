from tests.event.stop.base_stop_test import BaseStopTest
from utils.state import State


class StopEventAndWaitSuccessTest(BaseStopTest):
    # stop

    def test_stop_stop_in_wait_start_should_success(self):
        self.set_app()
        self.stop_stop_equal()
        self.road.wait_start()
        self.assertEqual(self.road.state, State.ON_WAIT_START)
        self.assertNotEqual(self.road.state, State.ON_STOP_STOP)

    def test_stop_stop_in_wait_stop_should_success(self):
        self.set_app()
        self.stop_stop_equal()
        self.bike.power = self.bike.max_power
        self.road.wait_stop()
        self.assertNotEqual(self.road.state, State.ON_STOP_STOP)
        self.assertEqual(self.road.state, State.ON_WAIT_STOP)
