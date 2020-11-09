from utils.state import State
from tests.event.go.test_go import BaseGoTest


class GoEventAndRelaxFailTest(BaseGoTest):
    # start

    def test_go_start_in_relax_start_should_fail(self):
        self.set_app()
        self.go_start_equal()
        self.road.relax_stop()
        self.assertNotEqual(self.road.state, State.ON_RELAX_START)
        self.assertEqual(self.road.state, State.ON_GO_START)

    def test_go_start_in_relax_move_should_fail(self):
        self.set_app()
        self.go_start_equal()
        self.road.on_relax(.1)
        self.assertNotEqual(self.road.state, State.ON_RELAX_MOVE)
        self.assertEqual(self.road.state, State.ON_GO_START)

    def test_go_start_in_relax_stop_should_fail(self):
        self.set_app()
        self.go_start_equal()
        self.road.relax_stop()
        self.assertNotEqual(self.road.state, State.ON_RELAX_STOP)
        self.assertEqual(self.road.state, State.ON_GO_START)

    # move

    def test_go_move_in_relax_start_should_fail(self):
        self.set_app()
        self.go_move_equal()
        self.road.relax_start()
        self.assertNotEqual(self.road.state, State.ON_RELAX_START)
        self.assertEqual(self.road.state, State.ON_GO_MOVE)

    def test_go_move_in_relax_stop_should_fail(self):
        self.set_app()
        self.go_move_equal()
        self.road.relax_stop()
        self.assertNotEqual(self.road.state, State.ON_WAIT_STOP)
        self.assertEqual(self.road.state, State.ON_GO_MOVE)

    # stop

    def test_go_stop_in_relax_start_should_fail(self):
        self.set_app()
        self.go_stop_equal()

        self.bike.speed = 0
        self.road.relax_start()
        self.assertNotEqual(self.road.state, State.ON_RELAX_START)
        self.assertEqual(self.road.state, State.ON_GO_STOP)

    def test_go_stop_in_relax_move_should_fail(self):
        self.set_app()
        self.go_stop_equal()

        self.bike.speed = 0
        self.road.on_relax(.1)
        self.assertNotEqual(self.road.state, State.ON_RELAX_MOVE)
        self.assertEqual(self.road.state, State.ON_GO_STOP)

    def test_go_stop_in_relax_stop_should_fail(self):
        self.set_app()
        self.go_stop_equal()

        self.bike.speed = 1
        self.road.relax_stop()
        self.assertNotEqual(self.road.state, State.ON_RELAX_STOP)
        self.assertEqual(self.road.state, State.ON_GO_STOP)
