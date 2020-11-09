from utils.state import State
from tests.event.go.base_go_test import BaseGoTest


class GoTest(BaseGoTest):
    def test_go_start(self):
        self.set_app()
        self.go_start_equal()

    def test_go_move(self):
        self.set_app()
        self.go_move_equal()

    def test_go_stop(self):
        self.set_app()
        self.go_stop_equal()
