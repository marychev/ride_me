from tests.event.jump.base_jump_test import BaseJumpTest
from utils.state import State


class JumpEventAndRelaxFailTest(BaseJumpTest):
    # start

    def test_jump_start_in_relax_start_should_fail(self):
        self.set_app()
        self.jump_start_equal()
        self.road.relax_start()
        self.assertNotEqual(self.road.state, State.ON_RELAX_START)
        self.assertEqual(self.road.state, State.ON_JUMP_START)

    def test_jump_start_in_relax_move_should_fail(self):
        self.set_app()
        self.jump_start_equal()
        self.road.on_relax(.1)
        self.assertNotEqual(self.road.state, State.ON_RELAX_MOVE)
        self.assertEqual(self.road.state, State.ON_JUMP_START)

    def test_jump_start_in_relax_stop_should_fail(self):
        self.set_app()
        self.jump_start_equal()
        self.road.relax_stop()
        self.assertNotEqual(self.road.state, State.ON_RELAX_STOP)
        self.assertEqual(self.road.state, State.ON_JUMP_START)

    # move

    def test_jump_move_in_relax_start_should_fail(self):
        self.set_app()
        self.jump_move_equal()
        self.road.relax_start()
        self.assertNotEqual(self.road.state, State.ON_RELAX_START)
        self.assertEqual(self.road.state, State.ON_JUMP_MOVE)

    def test_jump_move_in_relax_move_should_fail(self):
        self.set_app()
        self.jump_move_equal()
        self.road.on_relax(.1)
        self.assertNotEqual(self.road.state, State.ON_RELAX_MOVE)
        self.assertEqual(self.road.state, State.ON_JUMP_MOVE)

    def test_jump_move_in_relax_stop_should_fail(self):
        self.set_app()
        self.jump_move_equal()
        self.road.go_stop()
        self.assertNotEqual(self.road.state, State.ON_RELAX_STOP)
        self.assertEqual(self.road.state, State.ON_JUMP_MOVE)

    # stop

    def test_jump_stop_in_relax_start_should_fail(self):
        self.set_app()
        self.jump_stop_equal()
        self.road.relax_start()
        self.assertNotEqual(self.road.state, State.ON_RELAX_START)
        self.assertEqual(self.road.state, State.ON_JUMP_STOP)

    def test_jump_stop_in_relax_move_should_fail(self):
        self.set_app()
        self.jump_stop_equal()
        self.road.on_relax(.1)
        self.assertNotEqual(self.road.state, State.ON_RELAX_MOVE)
        self.assertEqual(self.road.state, State.ON_JUMP_STOP)

    def test_jump_stop_in_relax_stop_should_fail(self):
        self.set_app()
        self.jump_stop_equal()
        self.road.relax_stop()
        self.assertNotEqual(self.road.state, State.ON_RELAX_STOP)
        self.assertEqual(self.road.state, State.ON_JUMP_STOP)
