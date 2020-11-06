from tests.base_gui_test import BaseGameScreenGUITest
from utils.state import State


class LandingMoveTest(BaseGameScreenGUITest):
    def set_app(self):
        super(LandingMoveTest, self).set_app()

        self.bike.power = 150
        self.bike.y = self.road.y + 100
        self.road.on_landing(.1)
        self.assertEqual(self.road.state, State.ON_LANDING_MOVE)

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

    def test_stop_events_for_move_state_should_fail(self):
        self.set_app()
        self.bike.y = self.road.y + 100
        self.road.on_landing(.1)
        self.assertEqual(self.road.state, State.ON_LANDING_MOVE)

        self.road.stop_start()
        self.assertNotEqual(self.road.state, State.ON_STOP_START)
        self.assertEqual(self.road.state, State.ON_LANDING_MOVE)

        self.road.on_stop(.1)
        self.assertNotEqual(self.road.state, State.ON_STOP_MOVE)
        self.assertEqual(self.road.state, State.ON_LANDING_MOVE)

        self.road.stop_stop()
        self.assertNotEqual(self.road.state, State.ON_STOP_STOP)
        self.assertEqual(self.road.state, State.ON_LANDING_MOVE)

    def test_jump_events_for_move_state_should_fail(self):
        self.set_app()
        self.bike.y = self.road.y + 100
        self.road.on_landing(.1)
        self.assertEqual(self.road.state, State.ON_LANDING_MOVE)

        self.road.jump_start()
        self.assertNotEqual(self.road.state, State.ON_JUMP_START)
        self.assertEqual(self.road.state, State.ON_LANDING_MOVE)

        self.road.on_jump(.1)
        self.assertNotEqual(self.road.state, State.ON_JUMP_MOVE)
        self.assertEqual(self.road.state, State.ON_LANDING_MOVE)

        self.road.jump_stop()
        self.assertNotEqual(self.road.state, State.ON_JUMP_STOP)
        self.assertEqual(self.road.state, State.ON_LANDING_MOVE)

    def test_wait_events_for_move_state_should_fail(self):
        self.set_app()
        self.bike.y = self.road.y + 100
        self.road.on_landing(.1)
        self.assertEqual(self.road.state, State.ON_LANDING_MOVE)

        self.road.wait_start()
        self.assertNotEqual(self.road.state, State.ON_WAIT_START)
        self.assertEqual(self.road.state, State.ON_LANDING_MOVE)

        self.road.on_wait(.1)
        self.assertNotEqual(self.road.state, State.ON_WAIT_MOVE)
        self.assertEqual(self.road.state, State.ON_LANDING_MOVE)

        self.road.wait_stop()
        self.assertNotEqual(self.road.state, State.ON_WAIT_STOP)
        self.assertEqual(self.road.state, State.ON_LANDING_MOVE)
