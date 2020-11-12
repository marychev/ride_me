from tests.event.stop.base_stop_test import BaseStopTest
from utils.state import State


class StopEventAndRelaxFailTest(BaseStopTest):
    # start

    def test_stop_start_in_relax_start_should_fail(self):
        self.set_app()
        self.stop_start_equal()
        self.road.relax_start()
        self.assertNotEqual(self.road.state, State.ON_RELAX_START)
        self.assertEqual(self.road.state, State.ON_STOP_START)

    def test_stop_start_in_relax_move_should_fail(self):
        self.set_app()
        self.stop_start_equal()
        self.road.on_relax(.1)
        self.assertNotEqual(self.road.state, State.ON_RELAX_MOVE)
        self.assertEqual(self.road.state, State.ON_STOP_START)

    def test_stop_start_in_relax_stop_should_fail(self):
        self.set_app()
        self.stop_start_equal()
        self.road.relax_stop()
        self.assertNotEqual(self.road.state, State.ON_RELAX_STOP)
        self.assertEqual(self.road.state, State.ON_STOP_START)

    # move

    def test_stop_move_in_relax_start_should_fail(self):
        self.set_app()
        self.stop_move_equal()
        self.road.relax_start()
        self.assertNotEqual(self.road.state, State.ON_RELAX_START)
        self.assertEqual(self.road.state, State.ON_STOP_MOVE)

    def test_stop_move_in_relax_move_should_fail(self):
        self.set_app()
        self.stop_move_equal()
        self.road.on_relax(.1)
        self.assertNotEqual(self.road.state, State.ON_RELAX_MOVE)
        self.assertEqual(self.road.state, State.ON_STOP_MOVE)

    def test_stop_move_in_relax_stop_should_fail(self):
        self.set_app()
        self.stop_move_equal()
        self.road.relax_stop()
        self.assertNotEqual(self.road.state, State.ON_RELAX_STOP)
        self.assertEqual(self.road.state, State.ON_STOP_MOVE)

    # stop

    def test_stop_stop_in_relax_start_should_fail(self):
        self.set_app()
        self.stop_stop_equal()
        self.road.relax_start()
        self.assertNotEqual(self.road.state, State.ON_RELAX_START)
        self.assertNotEqual(self.road.state, State.ON_STOP_STOP)
        self.assertEqual(self.road.state, State.ON_WAIT_START)

    def test_stop_stop_in_relax_move_should_fail(self):
        self.set_app()
        self.stop_stop_equal()
        self.road.on_relax(.1)
        self.assertNotEqual(self.road.state, State.ON_RELAX_MOVE)
        self.assertNotEqual(self.road.state, State.ON_STOP_STOP)
        self.assertEqual(self.road.state, State.ON_WAIT_START)

    def test_stop_stop_in_relax_stop_should_fail(self):
        self.set_app()
        self.stop_stop_equal()
        self.road.relax_stop()
        self.assertNotEqual(self.road.state, State.ON_RELAX_MOVE)
        self.assertNotEqual(self.road.state, State.ON_STOP_STOP)
        self.assertEqual(self.road.state, State.ON_WAIT_START)
