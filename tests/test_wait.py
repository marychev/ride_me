from kivy.base import EventLoop
from kivy.tests.common import GraphicUnitTest

from screen.game_screen import GameScreen
from utils.state import State


class WaitTest(GraphicUnitTest):
    def set_app(self):
        self.screen = GameScreen()
        self.render(self.screen)
        self.road = self.screen.ids['road']
        self.bike = self.screen.ids['bike']

        self.bike.y = self.road.y
        self.bike.speed = 0
        self.bike.power = 150
        self.bike.max_power = 300

    def test_wait_start(self):
        self.set_app()
        self.road.landing_stop()
        self.road.wait_start()
        self.assertEqual(self.road.state, State.ON_WAIT_START)

    def test_wait_move(self):
        self.set_app()
        self.bike.power = self.bike.max_power/2
        self.road.on_wait(.1)
        self.assertEqual(self.road.state, State.ON_WAIT_MOVE)

    def test_wait_stop(self):
        self.set_app()
        self.bike.power = self.bike.max_power
        self.road.wait_stop()
        self.assertEqual(self.road.state, State.ON_WAIT_STOP)
