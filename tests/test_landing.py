from kivy.base import EventLoop
from kivy.tests.common import GraphicUnitTest

from screen.game_screen import GameScreen
from utils.state import State


class LandingTest(GraphicUnitTest):
    def set_app(self):
        self.screen = GameScreen()
        self.render(self.screen)
        self.road = self.screen.ids['road']
        self.bike = self.screen.ids['bike']

        self.bike.y = self.road.y
        self.bike.speed = 0
        self.bike.power = 150
        self.bike.max_power = 300
        self.road.set_state(State.ON_WAIT_START)
        self.road.wait_start()

    def test_runtouchapp(self):
        self.set_app()

        # get your Window instance safely
        EventLoop.ensure_window()
        window = EventLoop.window

        # your asserts
        self.assertEqual(window.children[0], self.screen)
        self.assertEqual(window.children[0].height, window.height)

    def test_landing_start(self):
        self.set_app()
        self.bike.y = self.road.y + 200
        self.road.landing_start()
        self.assertEqual(self.road.state, State.ON_LANDING_START)

    def test_landing_move(self):
        self.set_app()
        self.bike.y = self.road.y + 100
        self.road.on_landing(.1)
        self.assertEqual(self.road.state, State.ON_LANDING_MOVE)

    def test_bike_has_landed_already(self):
        self.set_app()
        self.bike.y = self.road.y
        self.road.on_landing(.1)
        self.assertEqual(self.road.state, State.ON_WAIT_START)

    def test_start_and_end_landing_success(self):
        self.set_app()
        self.assertEqual(self.road.state, State.ON_WAIT_START)
        self.bike.y = self.road.y + 10
        self.road.on_landing(.1)
        self.assertEqual(self.road.state, State.ON_LANDING_MOVE)

        # bike is waiting for something actions Set Stop state
        self.bike.y = self.road.y
        self.road.on_wait(.1)
        self.assertEqual(self.road.state, State.ON_WAIT_MOVE)

        # bike has ended to wait. Set Stop state
        self.bike.power = self.bike.max_power
        self.road.on_wait(.1)
        self.assertEqual(self.road.state, State.ON_WAIT_STOP)
