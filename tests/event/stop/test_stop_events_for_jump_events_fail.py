from tests.event.stop.base_stop_test import BaseStopTest
from utils.state import State


class StopEventAndJumpFailTest(BaseStopTest):
    # start

    def test_stop_start_in_jump_start_should_fail(self):
        self.set_app()
        self.stop_start_equal()
        self.road.jump_start()
        self.assertNotEqual(self.road.state, State.ON_JUMP_START)
        self.assertEqual(self.road.state, State.ON_STOP_START)

    def test_stop_start_in_jump_move_should_fail(self):
        self.set_app()
        self.stop_start_equal()
        self.road.on_jump(.1)
        self.assertNotEqual(self.road.state, State.ON_JUMP_MOVE)
        self.assertEqual(self.road.state, State.ON_STOP_START)

    def test_stop_start_in_jump_stop_should_fail(self):
        self.set_app()
        self.stop_start_equal()
        self.road.jump_stop()
        self.assertNotEqual(self.road.state, State.ON_JUMP_STOP)
        self.assertEqual(self.road.state, State.ON_STOP_START)

    # move

    def test_stop_move_in_jump_start_should_fail(self):
        self.set_app()
        self.stop_move_equal()
        self.road.jump_start()
        self.assertNotEqual(self.road.state, State.ON_JUMP_START)
        self.assertEqual(self.road.state, State.ON_STOP_MOVE)

    def test_stop_move_in_jump_move_should_fail(self):
        self.set_app()
        self.stop_move_equal()
        self.road.on_jump(.1)
        self.assertNotEqual(self.road.state, State.ON_JUMP_MOVE)
        self.assertEqual(self.road.state, State.ON_STOP_MOVE)

    def test_stop_move_in_jump_stop_should_fail(self):
        self.set_app()
        self.stop_move_equal()
        self.road.jump_stop()
        self.assertNotEqual(self.road.state, State.ON_JUMP_STOP)
        self.assertEqual(self.road.state, State.ON_STOP_MOVE)

    # stop

    def test_stop_stop_in_jump_start_should_fail(self):
        self.set_app()
        self.stop_stop_equal()
        self.road.jump_start()
        self.assertNotEqual(self.road.state, State.ON_JUMP_START)
        self.assertNotEqual(self.road.state, State.ON_STOP_STOP)
        self.assertEqual(self.road.state, State.ON_WAIT_START)

    def test_stop_stop_in_jump_move_should_fail(self):
        self.set_app()
        self.stop_stop_equal()
        self.road.on_jump(.1)
        self.road.landing_stop()
        self.assertNotEqual(self.road.state, State.ON_JUMP_MOVE)
        self.assertNotEqual(self.road.state, State.ON_STOP_STOP)
        self.assertEqual(self.road.state, State.ON_WAIT_START)

    def test_stop_stop_in_jump_stop_should_fail(self):
        self.set_app()
        self.stop_stop_equal()
        self.road.jump_stop()
        self.assertNotEqual(self.road.state, State.ON_JUMP_MOVE)
        self.assertNotEqual(self.road.state, State.ON_STOP_STOP)
        self.assertEqual(self.road.state, State.ON_WAIT_START)
