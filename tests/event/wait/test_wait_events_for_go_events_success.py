from tests.event.wait.base_wait_test import BaseWaitTest
from utils.state import State


class WaitEventAndGoSuccessTest(BaseWaitTest):
    # move

    def test_wait_move_in_go_start_should_success(self):
        self.set_app_move()
        self.road.go_start()
        self.assertEqual(self.road.state, State.ON_GO_START)
        self.assertNotEqual(self.road.state, State.ON_WAIT_MOVE)

    def test_wait_move_in_go_move_should_success(self):
        self.set_app_move()
        self.road.on_go(.1)
        self.assertEqual(self.road.state, State.ON_GO_MOVE)
        self.assertNotEqual(self.road.state, State.ON_WAIT_MOVE)

    # stop

    def test_wait_stop_in_go_start_should_success(self):
        self.set_app_stop()
        self.road.go_start()
        self.assertEqual(self.road.state, State.ON_GO_START)
        self.assertNotEqual(self.road.state, State.ON_WAIT_STOP)
