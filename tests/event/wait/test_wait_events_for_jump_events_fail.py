from tests.event.wait.base_wait_test import BaseWaitTest
from utils.state import State


class WaitEventAndJumpFailTest(BaseWaitTest):
    # start

    def test_wait_start_in_jump_start_should_fail(self):
        self.set_app_start()
        self.road.jump_start()
        self.assertNotEqual(self.road.state, State.ON_JUMP_START)
        self.assertEqual(self.road.state, State.ON_WAIT_START)

    def test_wait_start_in_jump_move_should_fail(self):
        self.set_app_start()
        self.road.on_jump(.1)
        self.assertNotEqual(self.road.state, State.ON_JUMP_MOVE)
        self.assertEqual(self.road.state, State.ON_WAIT_START)

    def test_wait_start_in_jump_stop_should_fail(self):
        self.set_app_start()
        self.road.jump_stop()
        self.assertNotEqual(self.road.state, State.ON_JUMP_STOP)
        self.assertEqual(self.road.state, State.ON_WAIT_START)

    # move

    def test_wait_move_in_jump_start_should_fail(self):
        self.set_app_move()
        self.bike.power = 0
        self.road.jump_start()
        self.assertNotEqual(self.road.state, State.ON_JUMP_START)
        self.assertEqual(self.road.state, State.ON_WAIT_MOVE)

    def test_wait_move_in_jump_move_should_fail(self):
        self.set_app_move()
        self.bike.power = 0
        self.road.on_jump(.1)
        self.assertNotEqual(self.road.state, State.ON_JUMP_MOVE)
        self.assertEqual(self.road.state, State.ON_WAIT_MOVE)

    def test_wait_move_in_jump_stop_should_fail(self):
        self.set_app_move()
        self.road.jump_stop()
        self.assertNotEqual(self.road.state, State.ON_JUMP_STOP)
        self.assertEqual(self.road.state, State.ON_WAIT_MOVE)

    # stop

    def test_wait_stop_in_jump_start_should_fail(self):
        self.set_app_stop()
        self.bike.power = 0
        self.road.jump_start()
        self.assertNotEqual(self.road.state, State.ON_JUMP_START)
        self.assertEqual(self.road.state, State.ON_WAIT_STOP)

    def test_wait_stop_in_jump_move_should_fail(self):
        self.set_app_stop()
        self.bike.power = 0
        self.road.on_jump(.1)
        self.assertNotEqual(self.road.state, State.ON_JUMP_MOVE)
        self.assertEqual(self.road.state, State.ON_WAIT_STOP)

    def test_wait_stop_in_jump_stop_should_fail(self):
        self.set_app_stop()
        self.road.jump_stop()
        self.assertNotEqual(self.road.state, State.ON_JUMP_STOP)
        self.assertEqual(self.road.state, State.ON_WAIT_STOP)
