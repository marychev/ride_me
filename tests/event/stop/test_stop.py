from tests.event.stop.base_stop_test import BaseStopTest


class StopTest(BaseStopTest):
    def test_stop_start(self):
        self.set_app()
        self.stop_start_equal()

    def test_stop_move(self):
        self.set_app()
        self.stop_move_equal()

    def test_stop_stop_to_wait(self):
        self.set_app()
        self.stop_stop_equal()
