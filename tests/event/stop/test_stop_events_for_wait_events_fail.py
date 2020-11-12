from tests.event.stop.base_stop_test import BaseStopTest
from utils.state import State


class StopEventAndWaitFailTest(BaseStopTest):
    # start

    def test_stop_start_in_wait_start_should_fail(self):
        self.set_app()
        self.stop_start_equal()
        self.road.wait_start()
        self.assertNotEqual(self.road.state, State.ON_WAIT_START)
        self.assertEqual(self.road.state, State.ON_STOP_START)

    def test_stop_start_in_wait_move_should_fail(self):
        self.set_app()
        self.stop_start_equal()
        self.road.on_wait(.1)
        self.assertNotEqual(self.road.state, State.ON_WAIT_MOVE)
        self.assertEqual(self.road.state, State.ON_STOP_START)

    def test_stop_start_in_wait_stop_should_fail(self):
        self.set_app()
        self.stop_start_equal()
        self.road.wait_stop()
        self.assertNotEqual(self.road.state, State.ON_WAIT_STOP)
        self.assertEqual(self.road.state, State.ON_STOP_START)

    # move

    def test_stop_move_in_wait_start_should_fail(self):
        self.set_app()
        self.stop_move_equal()
        self.road.wait_start()
        self.assertNotEqual(self.road.state, State.ON_WAIT_START)
        self.assertEqual(self.road.state, State.ON_STOP_MOVE)

    def test_stop_move_in_wait_move_should_fail(self):
        self.set_app()
        self.stop_move_equal()
        self.road.on_wait(.1)
        self.assertNotEqual(self.road.state, State.ON_WAIT_MOVE)
        self.assertEqual(self.road.state, State.ON_STOP_MOVE)

    def test_stop_move_in_wait_stop_should_fail(self):
        self.set_app()
        self.stop_move_equal()
        self.road.wait_stop()
        self.assertNotEqual(self.road.state, State.ON_WAIT_STOP)
        self.assertEqual(self.road.state, State.ON_STOP_MOVE)

    # stop

    def test_stop_stop_in_wait_start_should_success(self):
        self.set_app()
        self.stop_stop_equal()
        self.road.wait_start()
        self.assertEqual(self.road.state, State.ON_WAIT_START)
        self.assertNotEqual(self.road.state, State.ON_STOP_STOP)

    def test_stop_stop_in_wait_move_should_fail(self):
        self.set_app()
        self.stop_stop_equal()

        self.bike.speed = 1
        self.road.on_wait(.1)
        self.assertNotEqual(self.road.state, State.ON_WAIT_MOVE)
        self.assertNotEqual(self.road.state, State.ON_STOP_STOP)
        self.assertEqual(self.road.state, State.ON_WAIT_STOP)

    def test_stop_stop_in_wait_stop_should_success(self):
        self.set_app()
        self.stop_stop_equal()
        self.road.wait_stop()
        self.assertNotEqual(self.road.state, State.ON_STOP_STOP)
        self.assertEqual(self.road.state, State.ON_WAIT_STOP)
