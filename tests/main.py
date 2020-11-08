# It's import all the tests
from tests.test_landing import LandingTest
from tests.test_landing_move import LandingMoveTest
from tests.test_wait import WaitTest
from tests.test_jump import JumpTest
from tests.test_jump_move import JumpMoveTest
from tests.test_stop import StopTest
from tests.test_go import GoTest
from tests.test_go_background import GoBackgroundTest
from tests.test_relax import RelaxTest
from tests.test_relax_move import RelaxMoveTest
from tests.test_runtouchapp import RunTouchAppTest

if __name__ == '__main__':
    import unittest
    unittest.main()
