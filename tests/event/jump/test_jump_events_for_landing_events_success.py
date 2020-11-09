from tests.event.jump.base_jump_test import BaseJumpTest
from utils.state import State


class JumpEventAndLandingSuccessTest(BaseJumpTest):
    # move

    def test_jump_move_in_landing_start_should_success(self):
        self.set_app()
        self.jump_move_equal()

        self.bike.power = 0
        self.road.landing_start()
        self.assertEqual(self.road.state, State.ON_LANDING_START)
        self.assertNotEqual(self.road.state, State.ON_JUMP_MOVE)

    # stop

    def test_jump_stop_in_landing_start_should_success(self):
        self.set_app()
        self.jump_stop_equal()
        self.road.landing_start()
        self.assertEqual(self.road.state, State.ON_LANDING_START)
        self.assertNotEqual(self.road.state, State.ON_JUMP_STOP)

    def test_jump_stop_in_landing_move_should_success(self):
        self.set_app()
        self.jump_stop_equal()
        self.road.on_landing(.1)
        self.assertEqual(self.road.state, State.ON_LANDING_MOVE)
        self.assertNotEqual(self.road.state, State.ON_JUMP_STOP)
