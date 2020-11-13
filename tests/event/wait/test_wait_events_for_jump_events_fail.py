from tests.event.wait.base_wait_test import BaseWaitTest
from utils.state import State


class WaitEventAndJumpFailTest(BaseWaitTest):
    # start

    def test_wait_start_in_jump_start_should_fail(self):
        self.set_app_start()
        self.road.jump_start()
        self.assertNotEqual(self.road.state, State.ON_JUMP_START)
        self.assert_equal_wait_start()

    # def test_wait_start_in_jump_move_should_fail(self):
    #     self.set_app_start()
    #     self.road.on_jump(.1)
    #     self.assertNotEqual(self.road.state, State.ON_JUMP_MOVE)
    #     self.assert_equal_wait_move()

    # def test_wait_start_in_go_stop_should_fail(self):
    #     self.set_app_start()
    #     self.road.go_stop()
    #     self.assertNotEqual(self.road.state, State.ON_GO_STOP)
    #     self.assertEqual(self.road.state, State.ON_WAIT_START)
    #
    # # move
    #
    # def test_wait_move_in_go_start_should_fail(self):
    #     self.set_app_move()
    #     self.bike.y = self.road.y + self.bike.height
    #     self.road.go_start()
    #     self.assertNotEqual(self.road.state, State.ON_GO_START)
    #     self.assertEqual(self.road.state, State.ON_WAIT_MOVE)
    #
    # def test_wait_move_in_go_move_should_fail(self):
    #     self.set_app_move()
    #     self.bike.y = self.road.y + self.bike.height
    #     self.road.on_go(.1)
    #     self.assertNotEqual(self.road.state, State.ON_GO_MOVE)
    #     self.assertEqual(self.road.state, State.ON_WAIT_MOVE)
    #
    # def test_wait_move_in_go_stop_should_fail(self):
    #     self.set_app_move()
    #     self.road.go_stop()
    #     self.assertNotEqual(self.road.state, State.ON_GO_STOP)
    #     self.assertEqual(self.road.state, State.ON_WAIT_MOVE)
    #
    # # stop
    #
    # def test_wait_stop_in_go_start_should_fail(self):
    #     self.set_app_stop()
    #
    #     self.bike.y = self.road.y + self.bike.height
    #     self.road.go_start()
    #     self.assertNotEqual(self.road.state, State.ON_GO_START)
    #     self.assertEqual(self.road.state, State.ON_WAIT_STOP)
    #
    # def test_wait_stop_in_go_move_should_fail(self):
    #     self.set_app_stop()
    #     self.bike.y = self.road.y + self.bike.height
    #     self.road.on_go(.1)
    #     self.assertNotEqual(self.road.state, State.ON_GO_MOVE)
    #     self.assertEqual(self.road.state, State.ON_WAIT_STOP)
    #
    # def test_wait_stop_in_go_stop_should_fail(self):
    #     self.set_app_stop()
    #     self.road.go_stop()
    #     self.assertNotEqual(self.road.state, State.ON_GO_STOP)
    #     self.assertEqual(self.road.state, State.ON_WAIT_STOP)
