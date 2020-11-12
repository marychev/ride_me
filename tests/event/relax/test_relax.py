from utils.state import State
from tests.event.relax.base_relax_test import BaseRelaxTest


class RelaxTest(BaseRelaxTest):
    def test_relax_start(self):
        self.set_app()
        self.relax_start_equal()

    def test_relax_move(self):
        self.set_app()
        self.relax_move_equal()

    def test_relax_stop(self):
        self.set_app()
        self.relax_stop_equal()
