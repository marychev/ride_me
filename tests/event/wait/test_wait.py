from tests.event.wait.base_wait_test import BaseWaitTest
from utils.state import State


class WaitTest(BaseWaitTest):
    def test_wait_start(self):
        self.set_app()
        self.wait_start_equal()

    def test_wait_move(self):
        self.set_app()
        self.wait_move_equal()

    def test_wait_stop(self):
        self.set_app()
        self.wait_stop_equal()
