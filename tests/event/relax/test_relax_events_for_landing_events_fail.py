from tests.event.relax.base_relax_test import BaseRelaxTest
from utils.state import State


class RelaxEventAndLandingFailTest(BaseRelaxTest):

    # start

    def test_relax_start_in_landing_start_should_fail(self):
        self.set_app()
        self.relax_start_equal()
        self.road.relax_start()
        self.assertNotEqual(self.road.state, State.ON_LANDING_START)
        self.assertEqual(self.road.state, State.ON_RELAX_START)

    def test_relax_start_in_landing_move_should_fail(self):
        self.set_app()
        self.relax_start_equal()
        self.road.on_landing(.1)
        self.assertNotEqual(self.road.state, State.ON_LANDING_MOVE)
        self.assertEqual(self.road.state, State.ON_RELAX_START)

    def test_relax_start_in_landing_stop_should_fail(self):
        self.set_app()
        self.relax_start_equal()
        self.road.landing_stop()
        self.assertNotEqual(self.road.state, State.ON_LANDING_STOP)
        self.assertEqual(self.road.state, State.ON_RELAX_START)

    # move

    def test_relax_move_in_landing_start_should_fail(self):
        self.set_app()
        self.relax_move_equal()
        self.road.landing_start()
        self.assertNotEqual(self.road.state, State.ON_LANDING_START)
        self.assertEqual(self.road.state, State.ON_RELAX_MOVE)

    def test_relax_move_in_landing_move_should_fail(self):
        self.set_app()
        self.relax_move_equal()
        self.road.on_landing(.1)
        self.assertNotEqual(self.road.state, State.ON_LANDING_MOVE)
        self.assertEqual(self.road.state, State.ON_RELAX_MOVE)

    def test_relax_move_in_landing_stop_should_fail(self):
        self.set_app()
        self.relax_move_equal()
        self.road.landing_stop()
        self.assertNotEqual(self.road.state, State.ON_LANDING_STOP)
        self.assertEqual(self.road.state, State.ON_RELAX_MOVE)

    # stop

    def test_relax_stop_in_landing_start_should_fail(self):
        self.set_app()
        self.relax_stop_equal()
        self.road.landing_start()
        self.assertNotEqual(self.road.state, State.ON_LANDING_START)
        self.assertEqual(self.road.state, State.ON_RELAX_STOP)

    def test_relax_stop_in_landing_move_should_fail(self):
        self.set_app()
        self.relax_stop_equal()
        self.road.on_landing(.1)
        self.assertNotEqual(self.road.state, State.ON_LANDING_MOVE)
        self.assertEqual(self.road.state, State.ON_RELAX_STOP)

    def test_relax_stop_in_landing_stop_should_fail(self):
        self.set_app()
        self.relax_stop_equal()
        self.road.landing_stop()
        self.assertNotEqual(self.road.state, State.ON_LANDING_STOP)
        self.assertEqual(self.road.state, State.ON_RELAX_STOP)
