from tests.event.stop.base_stop_test import BaseStopTest
from utils.state import State


class StopEventAndLandingFailTest(BaseStopTest):
    # start

    def test_stop_start_in_landing_start_should_fail(self):
        self.set_app()
        self.stop_start_equal()
        self.road.landing_start()
        self.assertNotEqual(self.road.state, State.ON_LANDING_START)
        self.assertEqual(self.road.state, State.ON_STOP_START)

    def test_stop_start_in_landing_move_should_fail(self):
        self.set_app()
        self.stop_start_equal()
        self.road.on_landing(.1)
        self.assertNotEqual(self.road.state, State.ON_LANDING_MOVE)
        self.assertEqual(self.road.state, State.ON_STOP_START)

    def test_stop_start_in_landing_stop_should_fail(self):
        self.set_app()
        self.stop_start_equal()
        self.road.landing_stop()
        self.assertNotEqual(self.road.state, State.ON_LANDING_STOP)
        self.assertEqual(self.road.state, State.ON_STOP_START)

    # move

    def test_stop_move_in_landing_start_should_fail(self):
        self.set_app()
        self.stop_move_equal()
        self.road.landing_start()
        self.assertNotEqual(self.road.state, State.ON_LANDING_START)
        self.assertEqual(self.road.state, State.ON_STOP_MOVE)

    def test_stop_move_in_landing_move_should_fail(self):
        self.set_app()
        self.stop_move_equal()
        self.road.on_landing(.1)
        self.assertNotEqual(self.road.state, State.ON_LANDING_MOVE)
        self.assertEqual(self.road.state, State.ON_STOP_MOVE)

    def test_stop_move_in_landing_stop_should_fail(self):
        self.set_app()
        self.stop_move_equal()
        self.road.landing_stop()
        self.assertNotEqual(self.road.state, State.ON_LANDING_STOP)
        self.assertEqual(self.road.state, State.ON_STOP_MOVE)

    # stop

    def test_stop_stop_in_landing_move_should_fail(self):
        self.set_app()
        self.stop_stop_equal()
        self.road.on_landing(.1)
        self.assertNotEqual(self.road.state, State.ON_LANDING_MOVE)
        self.assertEqual(self.road.state, State.ON_WAIT_START)

    def test_stop_stop_in_landing_stop_should_fail(self):
        self.set_app()
        self.stop_stop_equal()
        self.road.landing_stop()
        self.assertNotEqual(self.road.state, State.ON_LANDING_STOP)
        self.assertNotEqual(self.road.state, State.ON_STOP_STOP)
        self.assertEqual(self.road.state, State.ON_WAIT_START)
