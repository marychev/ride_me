from utils.state import State
from tests.event.wait.base_wait_test import BaseWaitTest


class WaitEventAndRelaxFailTest(BaseWaitTest):
    # start

    def test_wait_start_for_relax_start_should_fail(self):
        self.set_app_start()
        self.road.relax_start()
        self.assertNotEqual(self.road.state, State.ON_RELAX_MOVE)
        self.assertEqual(self.road.state, State.ON_WAIT_START)

    def test_wait_start_for_relax_move_should_fail(self):
        self.set_app_start()
        self.road.on_relax(.1)
        self.assertNotEqual(self.road.state, State.ON_RELAX_MOVE)
        self.assertEqual(self.road.state, State.ON_WAIT_START)

    def test_wait_start_for_relax_stop_should_fail(self):
        self.set_app_start()
        self.road.relax_stop()
        self.assertNotEqual(self.road.state, State.ON_RELAX_STOP)
        self.assertEqual(self.road.state, State.ON_WAIT_START)

    # move

    def test_wait_move_for_relax_start_should_fail(self):
        self.set_app_move()
        self.road.relax_start()
        self.assertNotEqual(self.road.state, State.ON_RELAX_START)
        self.assertEqual(self.road.state, State.ON_WAIT_MOVE)

    def test_wait_move_for_relax_move_should_fail(self):
        self.set_app_move()
        self.road.on_relax(.1)
        self.assertNotEqual(self.road.state, State.ON_RELAX_MOVE)
        self.assertEqual(self.road.state, State.ON_WAIT_MOVE)

    def test_wait_move_for_relax_stop_should_fail(self):
        self.set_app_move()
        self.road.relax_stop()
        self.assertNotEqual(self.road.state, State.ON_RELAX_STOP)
        self.assertEqual(self.road.state, State.ON_WAIT_MOVE)

    # stop

    def test_wait_stop_for_relax_start_should_fail(self):
        self.set_app_stop()
        self.road.relax_start()
        self.assertNotEqual(self.road.state, State.ON_RELAX_START)
        self.assertEqual(self.road.state, State.ON_WAIT_STOP)

    def test_wait_stop_for_relax_move_should_fail(self):
        self.set_app_stop()
        self.road.on_relax(.1)
        self.assertNotEqual(self.road.state, State.ON_RELAX_MOVE)
        self.assertEqual(self.road.state, State.ON_WAIT_STOP)

    def test_wait_stop_for_relax_stop_should_fail(self):
        self.set_app_stop()
        self.road.relax_stop()
        self.assertNotEqual(self.road.state, State.ON_RELAX_STOP)
        self.assertEqual(self.road.state, State.ON_WAIT_STOP)
