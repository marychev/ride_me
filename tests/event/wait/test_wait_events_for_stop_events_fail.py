from tests.event.wait.base_wait_test import BaseWaitTest
from utils.state import State


class WaitEventAndStopFailTest(BaseWaitTest):
    # start

    def test_wait_start_in_stop_start_should_fail(self):
        self.set_app_start()
        self.road.stop_start()
        self.assertNotEqual(self.road.state, State.ON_STOP_START)
        self.assertEqual(self.road.state, State.ON_WAIT_START)

    def test_wait_start_in_stop_move_should_fail(self):
        self.set_app_start()
        self.road.on_stop(.1)
        self.assertNotEqual(self.road.state, State.ON_STOP_MOVE)
        self.assertEqual(self.road.state, State.ON_WAIT_START)

    def test_wait_start_in_stop_stop_should_fail(self):
        self.set_app_start()
        self.road.stop_stop()
        self.assertNotEqual(self.road.state, State.ON_STOP_STOP)
        self.assertEqual(self.road.state, State.ON_WAIT_START)

    # move

    def test_wait_move_in_stop_start_should_fail(self):
        self.set_app_move()
        self.road.stop_start()
        self.assertNotEqual(self.road.state, State.ON_STOP_START)
        self.assertEqual(self.road.state, State.ON_WAIT_MOVE)

    def test_wait_move_in_stop_move_should_fail(self):
        self.set_app_move()
        self.road.on_stop(.1)
        self.assertNotEqual(self.road.state, State.ON_STOP_MOVE)
        self.assertEqual(self.road.state, State.ON_WAIT_MOVE)

    def test_wait_move_in_stop_stop_should_fail(self):
        self.set_app_move()
        self.road.stop_stop()
        self.assertNotEqual(self.road.state, State.ON_STOP_STOP)
        self.assertEqual(self.road.state, State.ON_WAIT_MOVE)

    # stop

    def test_wait_stop_in_stop_start_should_fail(self):
        self.set_app_move()
        self.road.stop_start()
        self.assertNotEqual(self.road.state, State.ON_STOP_START)
        self.assertEqual(self.road.state, State.ON_WAIT_STOP)

    def test_wait_stop_in_stop_move_should_fail(self):
        self.set_app_move()
        self.road.on_stop(.1)
        self.assertNotEqual(self.road.state, State.ON_STOP_MOVE)
        self.assertEqual(self.road.state, State.ON_WAIT_STOP)

    def test_wait_stop_in_stop_stop_should_fail(self):
        self.set_app_move()
        self.road.stop_stop()
        self.assertNotEqual(self.road.state, State.ON_STOP_STOP)
        self.assertEqual(self.road.state, State.ON_WAIT_STOP)
