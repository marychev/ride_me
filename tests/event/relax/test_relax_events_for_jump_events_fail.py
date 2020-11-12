from tests.event.relax.base_relax_test import BaseRelaxTest
from utils.state import State


class RelaxEventAndJumpFailTest(BaseRelaxTest):

    # start

    def test_relax_start_in_jump_start_should_fail(self):
        self.set_app()
        self.relax_start_equal()
        self.road.jump_start()
        self.assertNotEqual(self.road.state, State.ON_JUMP_START)
        self.assertEqual(self.road.state, State.ON_RELAX_START)

    def test_relax_start_in_jump_move_should_fail(self):
        self.set_app()
        self.relax_start_equal()
        self.road.on_jump(.1)
        self.assertNotEqual(self.road.state, State.ON_JUMP_MOVE)
        self.assertEqual(self.road.state, State.ON_RELAX_START)

    def test_relax_start_in_jump_stop_should_fail(self):
        self.set_app()
        self.relax_start_equal()
        self.road.jump_stop()
        self.assertNotEqual(self.road.state, State.ON_JUMP_STOP)
        self.assertEqual(self.road.state, State.ON_RELAX_START)

    # move

    def test_relax_move_in_jump_start_should_fail(self):
        self.set_app()
        self.relax_move_equal()
        self.road.jump_start()
        self.assertNotEqual(self.road.state, State.ON_JUMP_START)
        self.assertEqual(self.road.state, State.ON_RELAX_MOVE)

    def test_relax_move_in_jump_move_should_fail(self):
        self.set_app()
        self.relax_move_equal()
        self.road.on_jump(.1)
        self.assertNotEqual(self.road.state, State.ON_JUMP_MOVE)
        self.assertEqual(self.road.state, State.ON_RELAX_MOVE)

    def test_relax_move_in_jump_stop_should_fail(self):
        self.set_app()
        self.relax_move_equal()
        self.road.jump_stop()
        self.assertNotEqual(self.road.state, State.ON_JUMP_STOP)
        self.assertEqual(self.road.state, State.ON_RELAX_MOVE)

    # stop

    def test_relax_stop_in_jump_start_should_fail(self):
        self.set_app()
        self.relax_stop_equal()
        self.road.jump_start()
        self.assertNotEqual(self.road.state, State.ON_JUMP_START)
        self.assertEqual(self.road.state, State.ON_RELAX_STOP)

    def test_relax_stop_in_jump_move_should_fail(self):
        self.set_app()
        self.relax_stop_equal()
        self.road.on_jump(.1)
        self.assertNotEqual(self.road.state, State.ON_JUMP_MOVE)
        self.assertEqual(self.road.state, State.ON_RELAX_STOP)

    def test_relax_stop_in_jump_stop_should_fail(self):
        self.set_app()
        self.relax_stop_equal()
        self.road.jump_stop()
        self.assertNotEqual(self.road.state, State.ON_JUMP_STOP)
        self.assertEqual(self.road.state, State.ON_RELAX_STOP)
