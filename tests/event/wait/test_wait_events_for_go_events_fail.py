from tests.event.wait.base_wait_test import BaseWaitTest
from utils.state import State


class WaitEventAndGoFailTest(BaseWaitTest):
    # start

    def test_wait_start_in_go_start_should_fail(self):
        self.set_app_start()
        self.road.go_start()
        self.assertNotEqual(self.road.state, State.ON_GO_START)
        self.assertEqual(self.road.state, State.ON_WAIT_START)

    def test_wait_start_in_go_move_should_fail(self):
        self.set_app_start()
        self.road.on_go(.1)
        self.assertNotEqual(self.road.state, State.ON_GO_MOVE)
        self.assertEqual(self.road.state, State.ON_WAIT_START)

    def test_wait_start_in_go_stop_should_fail(self):
        self.set_app_start()
        self.road.go_stop()
        self.assertNotEqual(self.road.state, State.ON_GO_STOP)
        self.assertEqual(self.road.state, State.ON_WAIT_START)

    # move

    def test_wait_move_in_go_start_should_fail(self):
        self.set_app_move()
        self.bike.y = self.road.line_points[-1] + self.bike.height
        self.road.go_start()
        self.assertNotEqual(self.road.state, State.ON_GO_START)
        self.assertEqual(self.road.state, State.ON_WAIT_MOVE)

    def test_wait_move_in_go_move_should_fail(self):
        self.set_app_move()
        self.bike.y = self.road.line_points[-1] + self.bike.height
        self.road.on_go(.1)
        self.assertNotEqual(self.road.state, State.ON_GO_MOVE)
        self.assertEqual(self.road.state, State.ON_WAIT_MOVE)

    def test_wait_move_in_go_stop_should_fail(self):
        self.set_app_move()
        self.road.go_stop()
        self.assertNotEqual(self.road.state, State.ON_GO_STOP)
        self.assertEqual(self.road.state, State.ON_WAIT_MOVE)

    # stop

    def test_wait_stop_in_go_start_should_fail(self):
        self.set_app_stop()

        self.bike.y = self.road.line_points[-1] + self.bike.height
        self.road.go_start()
        self.assertNotEqual(self.road.state, State.ON_GO_START)
        self.assertEqual(self.road.state, State.ON_WAIT_STOP)

    def test_wait_stop_in_go_move_should_fail(self):
        self.set_app_stop()
        self.bike.y = self.road.line_points[-1] + self.bike.height
        self.road.on_go(.1)
        self.assertNotEqual(self.road.state, State.ON_GO_MOVE)
        self.assertEqual(self.road.state, State.ON_WAIT_STOP)

    def test_wait_stop_in_go_stop_should_fail(self):
        self.set_app_stop()
        self.road.go_stop()
        self.assertNotEqual(self.road.state, State.ON_GO_STOP)
        self.assertEqual(self.road.state, State.ON_WAIT_STOP)
