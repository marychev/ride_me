from tests.event.jump.base_jump_test import BaseJumpTest
from utils.state import State


class JumpEventAndStopFailTest(BaseJumpTest):
    # start

    def test_jump_start_in_stop_start_should_fail(self):
        self.set_app()
        self.jump_start_equal()
        self.road.stop_start()
        self.assertNotEqual(self.road.state, State.ON_STOP_START)
        self.assertEqual(self.road.state, State.ON_JUMP_START)

    def test_jump_start_in_stop_move_should_fail(self):
        self.set_app()
        self.jump_start_equal()
        self.road.on_stop(.1)
        self.assertNotEqual(self.road.state, State.ON_STOP_MOVE)
        self.assertEqual(self.road.state, State.ON_JUMP_START)

    def test_jump_start_in_stop_stop_should_fail(self):
        self.set_app()
        self.jump_start_equal()
        self.road.stop_stop()
        self.assertNotEqual(self.road.state, State.ON_STOP_STOP)
        self.assertEqual(self.road.state, State.ON_JUMP_START)

    # move

    def test_jump_move_in_stop_start_should_fail(self):
        self.set_app()
        self.jump_move_equal()
        self.road.stop_start()
        self.assertNotEqual(self.road.state, State.ON_STOP_START)
        self.assertEqual(self.road.state, State.ON_JUMP_MOVE)

    def test_jump_move_in_stop_move_should_fail(self):
        self.set_app()
        self.jump_move_equal()
        self.road.on_stop(.1)
        self.assertNotEqual(self.road.state, State.ON_STOP_MOVE)
        self.assertEqual(self.road.state, State.ON_JUMP_MOVE)

    def test_jump_move_in_stop_stop_should_fail(self):
        self.set_app()
        self.jump_move_equal()
        self.road.stop_stop()
        self.assertNotEqual(self.road.state, State.ON_STOP_STOP)
        self.assertEqual(self.road.state, State.ON_JUMP_MOVE)

    # stop

    def test_jump_stop_in_stop_start_should_fail(self):
        self.set_app()
        self.jump_stop_equal()
        self.road.stop_start()
        self.assertNotEqual(self.road.state, State.ON_STOP_START)
        self.assertEqual(self.road.state, State.ON_JUMP_STOP)

    def test_jump_stop_in_stop_move_should_fail(self):
        self.set_app()
        self.jump_stop_equal()
        self.road.on_stop(.1)
        self.assertNotEqual(self.road.state, State.ON_STOP_MOVE)
        self.assertEqual(self.road.state, State.ON_JUMP_STOP)

    def test_jump_stop_in_stop_stop_should_fail(self):
        self.set_app()
        self.jump_stop_equal()
        self.road.stop_stop()
        self.assertNotEqual(self.road.state, State.ON_STOP_STOP)
        self.assertEqual(self.road.state, State.ON_JUMP_STOP)
