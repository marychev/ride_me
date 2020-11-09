from tests.event.jump.base_jump_test import BaseJumpTest
from utils.state import State


class JumpEventAndLandingFailTes(BaseJumpTest):
    # start

    def test_jump_start_in_landing_start_should_fail(self):
        self.set_app()
        self.jump_start_equal()
        self.road.landing_start()
        self.assertNotEqual(self.road.state, State.ON_LANDING_START)
        self.assertEqual(self.road.state, State.ON_JUMP_START)

    def test_jump_start_in_landing_move_should_fail(self):
        self.set_app()
        self.jump_start_equal()
        self.road.on_landing(.1)
        self.assertNotEqual(self.road.state, State.ON_LANDING_MOVE)
        self.assertEqual(self.road.state, State.ON_JUMP_START)

    def test_jump_start_in_landing_stop_should_fail(self):
        self.set_app()
        self.jump_start_equal()
        self.road.landing_stop()
        self.assertNotEqual(self.road.state, State.ON_LANDING_STOP)
        self.assertEqual(self.road.state, State.ON_JUMP_START)

    # move

    def test_jump_move_in_landing_move_should_fail(self):
        self.set_app()
        self.jump_move_equal()
        self.road.on_landing(.1)
        self.assertNotEqual(self.road.state, State.ON_LANDING_MOVE)
        self.assertEqual(self.road.state, State.ON_JUMP_MOVE)

    def test_jump_move_in_landing_stop_should_fail(self):
        self.set_app()
        self.jump_move_equal()
        self.road.landing_stop()
        self.assertNotEqual(self.road.state, State.ON_LANDING_STOP)
        self.assertEqual(self.road.state, State.ON_JUMP_MOVE)

    # stop

    def test_jump_stop_in_landing_stop_should_fail(self):
        self.set_app()
        self.jump_stop_equal()
        self.road.landing_stop()
        self.assertNotEqual(self.road.state, State.ON_LANDING_STOP)
        self.assertEqual(self.road.state, State.ON_JUMP_STOP)
