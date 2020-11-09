from utils.state import State
from tests.event.go.test_go import BaseGoTest


class GoEventAndRelaxSuccessTest(BaseGoTest):
    # move

    def test_go_move_in_relax_move_should_success(self):
        self.set_app()
        self.go_move_equal()
        self.bike.speed = 10
        self.road.on_relax(.1)
        self.assertEqual(self.road.state, State.ON_RELAX_MOVE)
        self.assertNotEqual(self.road.state, State.ON_GO_MOVE)

    # stop

    def test_go_stop_in_relax_start_should_success(self):
        self.set_app()
        self.go_stop_equal()
        self.bike.speed = 10
        self.road.relax_start()
        self.assertEqual(self.road.state, State.ON_RELAX_START)
        self.assertNotEqual(self.road.state, State.ON_GO_STOP)

    def test_go_stop_in_relax_move_should_success(self):
        self.set_app()
        self.go_stop_equal()

        self.bike.speed = 1
        self.road.on_relax(.1)
        self.assertEqual(self.road.state, State.ON_RELAX_MOVE)
        self.assertNotEqual(self.road.state, State.ON_GO_STOP)

    def test_go_stop_in_relax_stop_should_success(self):
        self.set_app()
        self.go_stop_equal()
        self.road.relax_stop()
        self.assertNotEqual(self.road.state, State.ON_RELAX_STOP)
        self.assertEqual(self.road.state, State.ON_GO_STOP)
