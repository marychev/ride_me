from tests.event.landing.base_landing_test import BaseLandingTest
from utils.state import State


class LandingEventAndJumpFailTest(BaseLandingTest):

    # start

    def test_landing_start_in_jump_start_should_fail(self):
        self.set_app()
        self.landing_start_equal()
        self.road.jump_start()
        self.assertNotEqual(self.road.state, State.ON_JUMP_START)
        self.assertEqual(self.road.state, State.ON_LANDING_START)

    def test_landing_start_in_jump_move_should_fail(self):
        self.set_app()
        self.landing_start_equal()
        self.road.on_jump(.1)
        self.assertNotEqual(self.road.state, State.ON_JUMP_MOVE)
        self.assertEqual(self.road.state, State.ON_LANDING_START)

    def test_landing_start_in_jump_stop_should_fail(self):
        self.set_app()
        self.landing_start_equal()
        self.road.jump_stop()
        self.assertNotEqual(self.road.state, State.ON_JUMP_STOP)
        self.assertEqual(self.road.state, State.ON_LANDING_START)

    # move

    def test_landing_move_in_jump_start_should_fail(self):
        self.set_app()
        self.landing_move_equal()
        self.road.jump_start()
        self.assertNotEqual(self.road.state, State.ON_JUMP_START)
        self.assertEqual(self.road.state, State.ON_LANDING_MOVE)

    def test_landing_move_in_jump_move_should_fail(self):
        self.set_app()
        self.landing_move_equal()
        self.road.on_jump(.1)
        self.assertNotEqual(self.road.state, State.ON_JUMP_MOVE)
        self.assertEqual(self.road.state, State.ON_LANDING_MOVE)

    def test_landing_move_in_jump_stop_should_fail(self):
        self.set_app()
        self.landing_move_equal()
        self.road.jump_stop()
        self.assertNotEqual(self.road.state, State.ON_JUMP_STOP)
        self.assertEqual(self.road.state, State.ON_LANDING_MOVE)

    # stop

    def test_landing_stop_in_jump_start_should_fail(self):
        self.set_app()
        self.road.set_state(State.ON_LANDING_STOP)
        self.road.jump_start()
        self.assertNotEqual(self.road.state, State.ON_JUMP_START)
        self.assertEqual(self.road.state, State.ON_LANDING_STOP)

    def test_landing_stop_in_jump_move_should_fail(self):
        self.set_app()
        self.road.set_state(State.ON_LANDING_STOP)
        self.road.on_jump(.1)
        self.assertNotEqual(self.road.state, State.ON_JUMP_MOVE)
        self.assertEqual(self.road.state, State.ON_LANDING_STOP)

    def test_landing_stop_in_jump_stop_should_fail(self):
        self.set_app()
        self.road.set_state(State.ON_LANDING_STOP)
        self.road.jump_stop()
        self.assertNotEqual(self.road.state, State.ON_JUMP_STOP)
        self.assertEqual(self.road.state, State.ON_LANDING_STOP)
