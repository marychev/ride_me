from tests.event.relax.base_relax_test import BaseRelaxTest
from utils.state import State


class RelaxEventAndWaitFailTest(BaseRelaxTest):

    # start

    def test_relax_start_in_wait_start_should_fail(self):
        self.set_app()
        self.relax_start_equal()
        self.road.wait_start()
        self.assertNotEqual(self.road.state, State.ON_WAIT_START)
        self.assertEqual(self.road.state, State.ON_RELAX_START)

    def test_relax_start_in_wait_move_should_fail(self):
        self.set_app()
        self.relax_start_equal()
        self.road.on_wait(.1)
        self.assertNotEqual(self.road.state, State.ON_WAIT_MOVE)
        self.assertEqual(self.road.state, State.ON_RELAX_START)

    def test_relax_start_in_wait_stop_should_fail(self):
        self.set_app()
        self.relax_start_equal()
        self.road.wait_stop()
        self.assertNotEqual(self.road.state, State.ON_WAIT_STOP)
        self.assertEqual(self.road.state, State.ON_RELAX_START)

    # move

    def test_relax_move_in_wait_start_should_fail(self):
        self.set_app()
        self.relax_move_equal()
        self.road.wait_start()
        self.assertNotEqual(self.road.state, State.ON_WAIT_START)
        self.assertEqual(self.road.state, State.ON_RELAX_MOVE)

    def test_relax_move_in_wait_move_should_fail(self):
        self.set_app()
        self.relax_move_equal()
        self.road.on_wait(.1)
        self.assertNotEqual(self.road.state, State.ON_WAIT_MOVE)
        self.assertEqual(self.road.state, State.ON_RELAX_MOVE)

    def test_relax_move_in_wait_stop_should_fail(self):
        self.set_app()
        self.relax_move_equal()
        self.road.wait_stop()
        self.assertNotEqual(self.road.state, State.ON_WAIT_STOP)
        self.assertEqual(self.road.state, State.ON_RELAX_MOVE)

    # stop

    def test_relax_stop_in_wait_move_should_fail(self):
        self.set_app()
        self.relax_stop_equal()
        self.road.on_wait(.1)
        self.assertNotEqual(self.road.state, State.ON_WAIT_MOVE)
        self.assertEqual(self.road.state, State.ON_RELAX_STOP)

    def test_relax_stop_in_wait_stop_should_fail(self):
        self.set_app()
        self.relax_stop_equal()
        self.road.wait_stop()
        self.assertNotEqual(self.road.state, State.ON_WAIT_STOP)
        self.assertEqual(self.road.state, State.ON_RELAX_STOP)
