from utils.state import State
from tests.event.go.test_go import BaseGoTest


class GoEventAndStopFailTest(BaseGoTest):
    # start

    def test_go_start_in_stop_start_should_fail(self):
        self.set_app()
        self.go_start_equal()
        self.road.stop_start()
        self.assertNotEqual(self.road.state, State.ON_STOP_START)
        self.assertEqual(self.road.state, State.ON_GO_START)

    def test_go_start_in_stop_move_should_fail(self):
        self.set_app()
        self.go_start_equal()
        self.road.on_stop(.1)
        self.assertNotEqual(self.road.state, State.ON_STOP_MOVE)
        self.assertEqual(self.road.state, State.ON_GO_START)

    def test_go_start_in_stop_stop_should_fail(self):
        self.set_app()
        self.go_start_equal()
        self.road.stop_stop()
        self.assertNotEqual(self.road.state, State.ON_STOP_STOP)
        self.assertEqual(self.road.state, State.ON_GO_START)

    # move

    def test_go_move_in_stop_start_should_fail(self):
        self.set_app()
        self.go_move_equal()
        self.road.stop_start()
        self.assertNotEqual(self.road.state, State.ON_STOP_START)
        self.assertEqual(self.road.state, State.ON_GO_MOVE)

    def test_go_move_in_stop_move_should_fail(self):
        self.set_app()
        self.go_move_equal()
        self.road.on_stop(.1)
        self.assertNotEqual(self.road.state, State.ON_STOP_MOVE)
        self.assertEqual(self.road.state, State.ON_GO_MOVE)

    def test_go_move_in_stop_stop_should_fail(self):
        self.set_app()
        self.go_move_equal()
        self.road.stop_stop()
        self.assertNotEqual(self.road.state, State.ON_STOP_STOP)
        self.assertEqual(self.road.state, State.ON_GO_MOVE)

    # stop

    def test_go_stop_in_stop_start_should_fail(self):
        self.set_app()
        self.go_stop_equal()
        self.road.stop_start()
        self.assertNotEqual(self.road.state, State.ON_STOP_START)
        self.assertEqual(self.road.state, State.ON_GO_STOP)

    def test_go_stop_in_stop_move_should_fail(self):
        self.set_app()
        self.go_stop_equal()
        self.road.on_stop(.1)
        self.assertNotEqual(self.road.state, State.ON_STOP_MOVE)
        self.assertEqual(self.road.state, State.ON_GO_STOP)

    def test_go_stop_in_jump_stop_should_fail(self):
        self.set_app()
        self.go_stop_equal()
        self.road.stop_stop()
        self.assertNotEqual(self.road.state, State.ON_STOP_STOP)
        self.assertEqual(self.road.state, State.ON_GO_STOP)
