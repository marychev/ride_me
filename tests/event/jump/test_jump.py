from utils.state import State
from tests.event.jump.base_jump_test import BaseJumpTest


class JumpTest(BaseJumpTest):
    def set_app(self):
        super().set_app()
        self._init_properties()

    def test_jump_start(self):
        self.set_app()
        self.road.jump_start()

    def test_jump_move(self):
        self.set_app()
        self.jump_move_equal()

    def test_jump_stop(self):
        self.set_app()
        self.jump_stop_equal()

    def test_go_all_events_for_move_state_should_fail(self):
        self.set_app()
        self.bike.y = self.road.y + 100
        self.road.on_landing(.1)
        self.assertEqual(self.road.state, State.ON_LANDING_MOVE)

        self.road.go_start()
        self.assertNotEqual(self.road.state, State.ON_GO_START)
        self.assertEqual(self.road.state, State.ON_LANDING_MOVE)

        self.road.on_go(.1)
        self.assertNotEqual(self.road.state, State.ON_GO_MOVE)
        self.assertEqual(self.road.state, State.ON_LANDING_MOVE)

        self.road.go_stop()
        self.assertNotEqual(self.road.state, State.ON_GO_STOP)
        self.assertEqual(self.road.state, State.ON_LANDING_MOVE)
