from tests.event.stop.base_stop_test import BaseStopTest
from utils.state import State


class StopEventAndRelaxSuccessTest(BaseStopTest):
    # stop
    def test_stop_stop_in_relax_start_should_success(self):
        self.set_app()
        self.bike.speed = 10
        self.stop_stop_equal()
        self.road.wait_stop()
        self.road.relax_start()
        self.assertEqual(self.road.state, State.ON_RELAX_START)
        self.assertNotEqual(self.road.state, State.ON_STOP_STOP)
