from tests.event.stop.base_stop_test import BaseStopTest
from utils.state import State


class StopEventAndGoSuccessTest(BaseStopTest):
    # start

    def test_stop_start_in_go_move_should_success(self):
        self.set_app()
        self.stop_start_equal()
        self.road.on_go(.1)
        self.assertEqual(self.road.state, State.ON_GO_MOVE)
        self.assertNotEqual(self.road.state, State.ON_STOP_START)
