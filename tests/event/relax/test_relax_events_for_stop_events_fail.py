from tests.event.relax.base_relax_test import BaseRelaxTest
from utils.state import State


class RelaxEventAndStopFailTest(BaseRelaxTest):

    # start

    def test_relax_start_in_stop_start_should_fail(self):
        self.set_app()
        self.relax_start_equal()
        self.road.stop_start()
        self.assertNotEqual(self.road.state, State.ON_STOP_START)
        self.assertEqual(self.road.state, State.ON_RELAX_START)

    def test_relax_start_in_stop_move_should_fail(self):
        self.set_app()
        self.relax_start_equal()
        self.road.on_stop(.1)
        self.assertNotEqual(self.road.state, State.ON_STOP_MOVE)
        self.assertEqual(self.road.state, State.ON_RELAX_START)

    def test_relax_start_in_stop_stop_should_fail(self):
        self.set_app()
        self.relax_start_equal()
        self.road.stop_stop()
        self.assertNotEqual(self.road.state, State.ON_STOP_STOP)
        self.assertEqual(self.road.state, State.ON_RELAX_START)

    # move

    def test_relax_move_in_stop_start_should_success(self):
        self.set_app()
        self.relax_move_equal()
        self.road.stop_start()
        self.assertEqual(self.road.state, State.ON_STOP_START)
        self.assertNotEqual(self.road.state, State.ON_RELAX_MOVE)

    def test_relax_move_in_stop_move_should_fail(self):
        self.set_app()
        self.relax_move_equal()
        self.road.on_stop(.1)
        self.assertNotEqual(self.road.state, State.ON_STOP_MOVE)
        self.assertEqual(self.road.state, State.ON_RELAX_MOVE)

    def test_relax_move_in_stop_stop_should_fail(self):
        self.set_app()
        self.relax_move_equal()
        self.road.stop_stop()
        self.assertNotEqual(self.road.state, State.ON_STOP_STOP)
        self.assertEqual(self.road.state, State.ON_RELAX_MOVE)

    # stop

    def test_relax_stop_in_stop_start_should_success(self):
        self.set_app()
        self.relax_stop_equal()
        self.road.stop_start()
        self.assertEqual(self.road.state, State.ON_STOP_START)
        self.assertNotEqual(self.road.state, State.ON_RELAX_STOP)

    def test_relax_stop_in_stop_move_should_success(self):
        self.set_app()
        self.relax_stop_equal()
        self.road.on_stop(.1)
        self.assertEqual(self.road.state, State.ON_STOP_MOVE)
        self.assertNotEqual(self.road.state, State.ON_RELAX_STOP)

    def test_relax_stop_in_stop_stop_should_fail(self):
        self.set_app()
        self.relax_stop_equal()
        self.road.stop_stop()
        self.assertNotEqual(self.road.state, State.ON_STOP_STOP)
        self.assertEqual(self.road.state, State.ON_RELAX_STOP)
