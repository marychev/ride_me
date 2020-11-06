from utils.state import State
from tests.base_gui_test import BaseGameScreenGUITest


class JumpTest(BaseGameScreenGUITest):
    def set_app(self):
        super().set_app()

        self.bike.power = 150
        self.road.landing_stop()
        self.road.wait_start()
        self.road.wait_stop()

    def test_jump_start(self):
        self.set_app()
        self.road.jump_start()
        self.assertEqual(self.road.state, State.ON_JUMP_START)

    def test_jump_move(self):
        self.set_app()
        self.bike.power = self.bike.max_power/2
        self.road.on_jump(.1)
        self.assertEqual(self.road.state, State.ON_JUMP_MOVE)

    def test_jump_stop(self):
        self.set_app()
        self.bike.y = self.road.y*2
        self.bike.power = 1
        self.road.on_jump(.1)
        self.road.jump_stop()
        self.assertEqual(self.road.state, State.ON_JUMP_STOP)

    def test_go_events_for_move_state_should_fail(self):
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
