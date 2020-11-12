from tests.event.relax.base_relax_test import BaseRelaxTest
from utils.state import State


class RelaxEventAndWaitSuccessTest(BaseRelaxTest):

    # stop

    def test_relax_stop_in_wait_start_should_success(self):
        self.set_app()
        self.relax_stop_equal()
        self.road.wait_start()
        self.assertEqual(self.road.state, State.ON_WAIT_START)
        self.assertNotEqual(self.road.state, State.ON_RELAX_STOP)
