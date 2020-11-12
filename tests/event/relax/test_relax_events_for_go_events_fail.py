from tests.event.relax.base_relax_test import BaseRelaxTest
from utils.state import State


class RelaxEventAndGoFailTest(BaseRelaxTest):

    # start

    def test_relax_start_in_go_move_should_fail(self):
        self.set_app()
        self.relax_start_equal()
        self.road.go_start()
        self.assertNotEqual(self.road.state, State.ON_GO_MOVE)
        self.assertNotEqual(self.road.state, State.ON_RELAX_START)

    def test_relax_start_in_go_stop_should_fail(self):
        self.set_app()
        self.relax_start_equal()
        self.road.go_stop()
        self.assertNotEqual(self.road.state, State.ON_GO_STOP)
        self.assertEqual(self.road.state, State.ON_RELAX_START)

    # move

    def test_relax_move_in_go_stop_should_fail(self):
        self.set_app()
        self.relax_move_equal()
        self.road.go_stop()
        self.assertNotEqual(self.road.state, State.ON_GO_STOP)
        self.assertEqual(self.road.state, State.ON_RELAX_MOVE)

    # stop

    def test_relax_stop_in_go_stop_should_fail(self):
        self.set_app()
        self.relax_stop_equal()
        self.road.go_stop()
        self.assertNotEqual(self.road.state, State.ON_GO_STOP)
        self.assertEqual(self.road.state, State.ON_RELAX_STOP)
