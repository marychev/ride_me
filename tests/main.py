# It's import all the tests:
# Tests Events
from tests.event.landing.test_landing import LandingTest
from tests.event.landing.test_landing_events_for_go_events_fail import LandingEventAndGoFailTest
from tests.event.landing.test_landing_events_for_stop_events_fail import LandingEventAndStopFailTest
from tests.event.landing.test_landing_events_for_jump_events_fail import LandingEventAndJumpFailTest
from tests.event.landing.test_landing_events_for_wait_events_fail import LandingEventAndWaitFailTest
from tests.event.landing.test_landing_events_for_wait_events_success import LandingEventAndWaitSuccessTest
from tests.event.landing.test_landing_events_for_relax_events_fail import LandingEventAndRelaxFailTest
from tests.event.landing.test_landing_events_for_relax_events_success import LandingEventAndRelaxSuccessTest

from tests.event.wait.test_wait import WaitTest
from tests.event.wait.test_wait_events_for_go_events_fail import WaitEventAndGoFailTest
from tests.event.wait.test_wait_events_for_go_events_success import WaitEventAndGoSuccessTest
from tests.event.wait.test_wait_events_for_jump_events_success import WaitEventAndJumpSuccessTest
from tests.event.wait.test_wait_events_for_jump_events_fail import WaitEventAndJumpFailTest
from tests.event.wait.test_wait_events_for_landing_events_fail import WaitEventAndLandingFailTest
from tests.event.wait.test_wait_events_for_stop_events_fail import WaitEventAndStopFailTest
from tests.event.wait.test_wait_events_for_relax_events_fail import WaitEventAndRelaxFailTest

from tests.event.jump.test_jump import JumpTest
from tests.event.jump.test_jump_events_for_go_events_fail import JumpEventAndGoFailTest
from tests.event.jump.test_jump_events_for_landing_events_success import JumpEventAndLandingSuccessTest
from tests.event.jump.test_jump_events_for_landing_events_fail import JumpEventAndLandingFailTest
from tests.event.jump.test_jump_events_for_relax_events_fail import JumpEventAndRelaxFailTest
from tests.event.jump.test_jump_events_for_stop_events_fail import JumpEventAndStopFailTest
from tests.event.jump.test_jump_events_for_wait_events_fail import JumpEventAndWaitFailTest

from tests.event.stop.test_stop import StopTest
from tests.event.stop.test_stop_events_for_jump_events_fail import StopEventAndJumpFailTest
from tests.event.stop.test_stop_events_for_landing_events_fail import StopEventAndLandingFailTest
from tests.event.stop.test_stop_events_for_landing_events_success import StopEventAndLandingSuccessTest
from tests.event.stop.test_stop_events_for_go_events_fail import StopEventAndGoFailTest
from tests.event.stop.test_stop_events_for_go_events_success import StopEventAndGoSuccessTest
from tests.event.stop.test_stop_events_for_relax_events_fail import StopEventAndRelaxFailTest
from tests.event.stop.test_stop_events_for_relax_events_success import StopEventAndRelaxSuccessTest
from tests.event.stop.test_stop_events_for_wait_events_fail import StopEventAndWaitFailTest
from tests.event.stop.test_stop_events_for_wait_events_success import StopEventAndWaitSuccessTest

from tests.event.go.test_go import GoTest
from tests.event.go.test_go_events_for_jump_events_fail import GoEventAndJumpFailTest
from tests.event.go.test_go_events_for_landing_events_fail import GoEventAndLandingFailTest
from tests.event.go.test_go_events_for_wait_events_fail import GoEventAndWaitFailTest
from tests.event.go.test_go_events_for_stop_events_fail import GoEventAndStopFailTest
from tests.event.go.test_go_events_for_relax_events_fail import GoEventAndRelaxFailTest
from tests.event.go.test_go_events_for_relax_events_success import GoEventAndRelaxSuccessTest

from tests.event.go_background.test_go_background import GoBackgroundTest

from tests.event.relax.test_relax import RelaxTest
from tests.event.relax.test_relax_move import RelaxMoveTest
from tests.event.relax.test_relax_events_for_jump_events_fail import RelaxEventAndJumpFailTest
from tests.event.relax.test_relax_events_for_landing_events_fail import RelaxEventAndLandingFailTest
from tests.event.relax.test_relax_events_for_go_events_fail import RelaxEventAndGoFailTest
from tests.event.relax.test_relax_events_for_go_events_success import RelaxEventAndGoSuccessTest
from tests.event.relax.test_relax_events_for_stop_events_fail import RelaxEventAndStopFailTest
from tests.event.relax.test_relax_events_for_stop_events_success import RelaxEventAndStopSuccessTest
from tests.event.relax.test_relax_events_for_wait_events_fail import RelaxEventAndWaitFailTest
from tests.event.relax.test_relax_events_for_wait_events_success import RelaxEventAndWaitSuccessTest

# Tests Level
from tests.level.test_map_road import MapRoadTest

# Tests Screens
from tests.screen.test_restart_game_screen import RestartGameScreenTest

from tests.test_runtouchapp import RunTouchAppTest





if __name__ == '__main__':
    import unittest
    unittest.main()
