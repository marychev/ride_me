from utils.state import State
from tests.event.go.test_go import BaseGoTest


class GoEventAndWaitFailTest(BaseGoTest):
    # start

    def test_go_start_in_wait_start_should_fail(self):
        self.set_app()
        self.go_start_equal()
        self.road.wait_start()
        self.assertNotEqual(self.road.state, State.ON_WAIT_START)
        self.assertEqual(self.road.state, State.ON_GO_START)

    def test_go_start_in_wait_move_should_fail(self):
        self.set_app()
        self.go_start_equal()
        self.road.on_wait(.1)
        self.assertNotEqual(self.road.state, State.ON_WAIT_MOVE)
        self.assertEqual(self.road.state, State.ON_GO_START)

    def test_go_start_in_wait_stop_should_fail(self):
        self.set_app()
        self.go_start_equal()

        self.bike.power = self.bike.max_power / 2
        self.road.wait_stop()
        self.assertNotEqual(self.road.state, State.ON_WAIT_STOP)
        self.assertEqual(self.road.state, State.ON_GO_START)

    # move

    def test_go_move_in_wait_start_should_fail(self):
        self.set_app()
        self.go_move_equal()
        self.road.wait_start()
        self.assertNotEqual(self.road.state, State.ON_WAIT_START)
        self.assertEqual(self.road.state, State.ON_GO_MOVE)

    def test_go_move_in_wait_move_should_fail(self):
        self.set_app()
        self.go_move_equal()
        self.road.on_wait(.1)
        self.assertNotEqual(self.road.state, State.ON_WAIT_MOVE)
        self.assertEqual(self.road.state, State.ON_GO_MOVE)

    def test_go_move_in_wait_stop_should_fail(self):
        self.set_app()
        self.go_move_equal()
        # self.bike.speed = self.bike.max_speed / 2
        self.road.wait_stop()
        self.assertNotEqual(self.road.state, State.ON_WAIT_STOP)
        self.assertEqual(self.road.state, State.ON_GO_MOVE)

    # stop

    # [?] 9/11/20
    def test_go_stop_in_wait_start_should_fail(self):
        self.set_app()
        self.go_stop_equal()
        self.road.wait_start()
        self.assertNotEqual(self.road.state, State.ON_WAIT_START)
        self.assertEqual(self.road.state, State.ON_GO_STOP)

    def test_go_stop_in_wait_move_should_fail(self):
        self.set_app()
        self.go_stop_equal()

        self.bike.speed = 1
        self.road.on_wait(.1)
        self.assertNotEqual(self.road.state, State.ON_WAIT_MOVE)
        self.assertEqual(self.road.state, State.ON_GO_STOP)

    def test_go_stop_in_wait_stop_should_fail(self):
        self.set_app()
        self.go_stop_equal()
        self.road.wait_stop()
        self.assertNotEqual(self.road.state, State.ON_WAIT_STOP)
        self.assertEqual(self.road.state, State.ON_GO_STOP)
