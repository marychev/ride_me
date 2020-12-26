from tests.event.relax.base_relax_test import BaseRelaxTest
from utils.state import State


class RelaxEventAndStopSuccessTest(BaseRelaxTest):

    # move

    def test_relax_move_in_stop_start_should_success(self):
        self.set_app()
        self.relax_move_equal()
        self.road.stop_start()
        self.assertEqual(self.road.state, State.ON_STOP_START)
        self.assertNotEqual(self.road.state, State.ON_RELAX_MOVE)

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
        self.bike.speed = self.bike.max_speed / 2
        self.road.on_stop(.1)
        self.assertEqual(self.road.state, State.ON_STOP_MOVE)
        self.assertNotEqual(self.road.state, State.ON_RELAX_STOP)
