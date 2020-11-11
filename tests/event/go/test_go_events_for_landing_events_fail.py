from utils.state import State
from tests.event.go.test_go import BaseGoTest


class GoEventAndLandingFailTest(BaseGoTest):
    """ All events for landing states should fail """

    def test_go_start_in_landing_start_should_fail(self):
        self.set_app()
        self.go_start_equal()
        self.road.landing_start()
        self.assertNotEqual(self.road.state, State.ON_LANDING_START)
        self.assertEqual(self.road.state, State.ON_GO_START)

    def test_go_start_in_landing_move_should_fail(self):
        self.set_app()
        self.go_start_equal()
        self.road.on_landing(.1)
        self.assertNotEqual(self.road.state, State.ON_LANDING_MOVE)
        self.assertEqual(self.road.state, State.ON_GO_START)

    def test_go_start_in_landing_stop_should_fail(self):
        self.set_app()
        self.go_start_equal()
        self.road.landing_stop()
        self.assertNotEqual(self.road.state, State.ON_LANDING_STOP)
        self.assertEqual(self.road.state, State.ON_GO_START)

    def test_go_move_in_landing_start_should_fail(self):
        self.set_app()
        self.go_move_equal()
        self.road.landing_start()
        self.assertNotEqual(self.road.state, State.ON_LANDING_START)
        self.assertEqual(self.road.state, State.ON_GO_MOVE)

    def test_go_move_in_landing_move_should_fail(self):
        self.set_app()
        self.go_move_equal()
        self.road.on_landing(.1)
        self.assertNotEqual(self.road.state, State.ON_LANDING_MOVE)
        self.assertEqual(self.road.state, State.ON_GO_MOVE)

    def test_go_move_in_landing_stop_should_fail(self):
        self.set_app()
        self.go_move_equal()
        self.road.landing_stop()
        self.assertNotEqual(self.road.state, State.ON_LANDING_STOP)
        self.assertEqual(self.road.state, State.ON_GO_MOVE)

    def test_go_stop_in_landing_start_should_fail(self):
        self.set_app()
        self.go_stop_equal()
        self.road.landing_start()
        self.assertNotEqual(self.road.state, State.ON_LANDING_START)
        self.assertEqual(self.road.state, State.ON_GO_STOP)

    def test_go_stop_in_landing_move_should_fail(self):
        self.set_app()
        self.go_stop_equal()
        self.road.on_landing(.1)
        self.assertNotEqual(self.road.state, State.ON_LANDING_MOVE)
        self.assertEqual(self.road.state, State.ON_GO_STOP)

    def test_go_stop_in_landing_stop_should_fail(self):
        self.set_app()
        self.go_stop_equal()
        self.road.landing_stop()
        self.assertNotEqual(self.road.state, State.ON_LANDING_STOP)
        self.assertEqual(self.road.state, State.ON_GO_STOP)
