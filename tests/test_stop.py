from kivy.base import EventLoop
from kivy.tests.common import GraphicUnitTest

from screen.game_screen import GameScreen
from utils.state import State


class StopTest(GraphicUnitTest):
    def set_app(self):
        self.screen = GameScreen()
        self.render(self.screen)
        self.road = self.screen.ids['road']
        self.bike = self.screen.ids['bike']

        self.bike.y = self.road.y
        self.bike.speed = 0
        self.bike.power = 150
        self.bike.max_power = 300
        self.road.landing_stop()
        self.road.wait_start()

    def test_stop_start(self):
        self.set_app()
        self.bike.speed = 100
        self.road.on_go(0.1)
        self.road.stop_start()
        self.assertEqual(self.road.state, State.ON_STOP_START)

    def test_stop_move(self):
        self.set_app()
        self.bike.speed = 50
        self.road.stop_start()
        self.road.on_stop(.1)
        self.assertEqual(self.road.state, State.ON_STOP_MOVE)

    def test_stop_stop(self):
        self.set_app()
        self.bike.speed = 0
        self.road.on_stop(.1)
        self.road.stop_stop()
        self.assertEqual(self.road.state, State.ON_STOP_STOP)
