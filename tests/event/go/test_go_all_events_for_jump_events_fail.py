from utils.state import State
from tests.event.go.test_go import BaseGoTest


class GoEventAndJumpFailTest(BaseGoTest):
    def test_go_start_in_jump_start_should_fail(self):
        self.set_app()
        self.go_start_equal()
        self.road.jump_start()
        self.assertNotEqual(self.road.state, State.ON_JUMP_START)
        self.assertEqual(self.road.state, State.ON_GO_START)

    def test_go_start_in_jump_move_should_fail(self):
        self.set_app()
        self.go_start_equal()
        self.road.on_jump(.1)
        self.assertNotEqual(self.road.state, State.ON_JUMP_MOVE)
        self.assertEqual(self.road.state, State.ON_GO_START)

    def test_go_start_in_jump_stop_should_fail(self):
        self.set_app()
        self.go_start_equal()
        self.road.jump_stop()
        self.assertNotEqual(self.road.state, State.ON_JUMP_STOP)
        self.assertEqual(self.road.state, State.ON_GO_START)

    def test_go_move_in_jump_start_should_fail(self):
        self.set_app()
        self.go_move_equal()
        self.road.jump_start()
        self.assertNotEqual(self.road.state, State.ON_JUMP_START)
        self.assertEqual(self.road.state, State.ON_GO_MOVE)

    def test_go_move_in_jump_move_should_fail(self):
        self.set_app()
        self.go_move_equal()
        self.road.on_jump(.1)
        self.assertNotEqual(self.road.state, State.ON_JUMP_MOVE)
        self.assertEqual(self.road.state, State.ON_GO_MOVE)

    def test_go_move_in_jump_stop_should_fail(self):
        self.set_app()
        self.go_move_equal()
        self.road.jump_stop()
        self.assertNotEqual(self.road.state, State.ON_JUMP_STOP)
        self.assertEqual(self.road.state, State.ON_GO_MOVE)

    def test_go_stop_in_jump_start_should_fail(self):
        self.set_app()
        self.go_stop_equal()
        self.road.jump_start()
        self.assertNotEqual(self.road.state, State.ON_JUMP_START)
        self.assertEqual(self.road.state, State.ON_GO_STOP)

    def test_go_stop_in_jump_move_should_fail(self):
        self.set_app()
        self.go_stop_equal()
        self.road.on_jump(.1)
        self.assertNotEqual(self.road.state, State.ON_JUMP_MOVE)
        self.assertEqual(self.road.state, State.ON_GO_STOP)

    def test_go_stop_in_jump_stop_should_fail(self):
        self.set_app()
        self.go_stop_equal()
        self.road.jump_stop()
        self.assertNotEqual(self.road.state, State.ON_JUMP_STOP)
        self.assertEqual(self.road.state, State.ON_GO_STOP)
