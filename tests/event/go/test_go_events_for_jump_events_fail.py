from utils.state import State
from tests.event.go.test_go import BaseGoTest


class GoEventAndJumpFailTest(BaseGoTest):
    # start

    def test_go_start_in_jump_start_should_fail(self):
        self.set_app_start()
        self.road.jump_start()
        self.assertNotEqual(self.road.state, State.ON_JUMP_START)
        self.assertEqual(self.road.state, State.ON_GO_START)

    def test_go_start_in_jump_move_should_fail(self):
        self.set_app_start()
        self.road.on_jump(.1)
        self.assertNotEqual(self.road.state, State.ON_JUMP_MOVE)
        self.assertEqual(self.road.state, State.ON_GO_START)

    def test_go_start_in_jump_stop_should_fail(self):
        self.set_app_start()
        self.road.jump_stop()
        self.assertNotEqual(self.road.state, State.ON_JUMP_STOP)
        self.assertEqual(self.road.state, State.ON_GO_START)

    # move

    def test_go_move_in_jump_start_should_fail(self):
        self.set_app_move()
        self.road.jump_start()
        self.assertNotEqual(self.road.state, State.ON_JUMP_START)
        self.assertEqual(self.road.state, State.ON_GO_MOVE)

    def test_go_move_in_jump_move_should_fail(self):
        self.set_app_move()
        self.road.on_jump(.1)
        self.assertNotEqual(self.road.state, State.ON_JUMP_MOVE)
        self.assertEqual(self.road.state, State.ON_GO_MOVE)

    def test_go_move_in_jump_stop_should_fail(self):
        self.set_app_move()
        self.road.jump_stop()
        self.assertNotEqual(self.road.state, State.ON_JUMP_STOP)
        self.assertEqual(self.road.state, State.ON_GO_MOVE)

    # stop

    def test_go_stop_in_jump_start_should_fail(self):
        self.set_app_stop()
        self.road.jump_start()
        self.assertNotEqual(self.road.state, State.ON_JUMP_START)
        self.assertEqual(self.road.state, State.ON_GO_STOP)

    def test_go_stop_in_jump_move_should_fail(self):
        self.set_app_stop()
        self.road.on_jump(.1)
        self.assertNotEqual(self.road.state, State.ON_JUMP_MOVE)
        self.assertEqual(self.road.state, State.ON_GO_STOP)

    def test_go_stop_in_jump_stop_should_fail(self):
        self.set_app_stop()
        self.road.jump_stop()
        self.assertNotEqual(self.road.state, State.ON_JUMP_STOP)
        self.assertEqual(self.road.state, State.ON_GO_STOP)
