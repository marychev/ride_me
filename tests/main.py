# It's import all the tests
from tests.event.landing.test_landing import LandingTest
from tests.event.landing.test_landing_move import LandingMoveTest
from tests.event.wait.test_wait import WaitTest
from tests.event.jump.test_jump import JumpTest
from tests.event.jump.test_jump_move import JumpMoveTest
from tests.event.stop.test_stop import StopTest
from tests.event.go.test_go import GoTest
from tests.event.go.test_go_background import GoBackgroundTest
from tests.event.relax.test_relax import RelaxTest
from tests.event.relax.test_relax_move import RelaxMoveTest
from tests.test_runtouchapp import RunTouchAppTest


if __name__ == '__main__':
    import unittest
    unittest.main()
