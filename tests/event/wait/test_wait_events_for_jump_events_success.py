from tests.event.wait.base_wait_test import BaseWaitTest
from utils.state import State


class WaitEventAndJumpSuccessTest(BaseWaitTest):
    # move

    def test_wait_move_in_jump_start_should_success(self):
        self.set_app_move()
        self.road.jump_start()
        self.assertEqual(self.road.state, State.ON_JUMP_START)
        self.assertNotEqual(self.road.state, State.ON_WAIT_MOVE)

    def test_wait_move_in_jump_move_should_success(self):
        self.set_app_move()
        self.road.on_jump(.1)
        self.assertEqual(self.road.state, State.ON_JUMP_MOVE)
        self.assertNotEqual(self.road.state, State.ON_WAIT_MOVE)

    # stop

    def test_wait_stop_in_jump_start_should_success(self):
        self.set_app_stop()
        self.road.jump_start()
        self.assertEqual(self.road.state, State.ON_JUMP_START)
        self.assertNotEqual(self.road.state, State.ON_WAIT_STOP)

    def test_wait_stop_in_jump_move_should_success(self):
        self.set_app_stop()
        self.road.on_jump(.1)
        self.assertEqual(self.road.state, State.ON_JUMP_MOVE)
        self.assertNotEqual(self.road.state, State.ON_WAIT_STOP)
