from tests.base_gui_test import BaseGameScreenGUITest
from utils.state import State


class RelaxMoveTest(BaseGameScreenGUITest):
    def set_app(self):
        super(RelaxMoveTest, self).set_app()

        self.bike.y = self.road.y
        self.bike.power = 30
        self.bike.speed = 10

        self.road.on_relax(.1)
        self.assertEqual(self.road.state, State.ON_RELAX_MOVE)

    def test_jump_start_for_move_state_should_fail(self):
        self.set_app()

        self.bike.power = 0

        self.road.jump_start()
        self.assertNotEqual(self.road.state, State.ON_JUMP_START)
        self.road.on_jump(.1)
        self.assertNotEqual(self.road.state, State.ON_JUMP_MOVE)
        self.road.jump_stop()
        self.assertNotEqual(self.road.state, State.ON_JUMP_STOP)

    # success events

    def test_jump_events_for_move_state_should_success(self):
        self.set_app()
        self.road.jump_start()
        self.assertEqual(self.road.state, State.ON_JUMP_START)
        self.road.on_jump(.1)
        self.assertEqual(self.road.state, State.ON_JUMP_MOVE)
        self.road.jump_stop()
        self.assertEqual(self.road.state, State.ON_JUMP_STOP)

    def test_go_events_for_move_state_should_success(self):
        self.set_app()
        self.road.go_start()
        self.assertEqual(self.road.state, State.ON_GO_START)
        self.road.on_go(.1)
        self.assertEqual(self.road.state, State.ON_GO_MOVE)
        self.road.go_stop()
        self.assertEqual(self.road.state, State.ON_GO_STOP)

    def test_stop_events_for_move_state_should_success(self):
        self.set_app()

        self.road.stop_start()
        self.assertEqual(self.road.state, State.ON_STOP_START)
        self.road.on_stop(.1)
        self.assertEqual(self.road.state, State.ON_STOP_MOVE)

        self.bike.speed = 0
        self.road.stop_stop()
        self.assertNotEqual(self.road.state, State.ON_STOP_STOP)
        self.assertEqual(self.road.state, State.ON_WAIT_START)

    # fail events

    def test_stop_move_for_move_state_should_fail(self):
        self.set_app()
        self.bike.speed = 0
        self.road.on_stop(.1)
        self.assertEqual(self.road.state, State.ON_RELAX_MOVE)
        self.assertNotEqual(self.road.state, State.ON_STOP_MOVE)

    def test_landing_events_for_move_state_should_fail(self):
        self.set_app()
        self.road.landing_start()
        self.assertNotEqual(self.road.state, State.ON_LANDING_START)
        self.assertEqual(self.road.state, State.ON_RELAX_MOVE)

        self.road.on_landing(.1)
        self.assertNotEqual(self.road.state, State.ON_LANDING_MOVE)
        self.assertEqual(self.road.state, State.ON_RELAX_MOVE)

        self.road.landing_stop()
        self.assertNotEqual(self.road.state, State.ON_LANDING_STOP)
        self.assertEqual(self.road.state, State.ON_RELAX_MOVE)

    def test_wait_events_for_move_state_should_fail(self):
        self.set_app()
        self.road.wait_start()
        self.assertNotEqual(self.road.state, State.ON_WAIT_START)
        self.assertEqual(self.road.state, State.ON_RELAX_MOVE)

        self.road.on_wait(.1)
        self.assertNotEqual(self.road.state, State.ON_WAIT_MOVE)
        self.assertEqual(self.road.state, State.ON_RELAX_MOVE)

        self.road.wait_stop()
        self.assertNotEqual(self.road.state, State.ON_WAIT_STOP)
        self.assertEqual(self.road.state, State.ON_RELAX_MOVE)
