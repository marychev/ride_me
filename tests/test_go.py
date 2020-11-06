from kivy.base import EventLoop
from kivy.tests.common import GraphicUnitTest

from screen.game_screen import GameScreen
from utils.state import State


class GoTest(GraphicUnitTest):
    def set_app(self):
        self.screen = GameScreen()
        self.render(self.screen)
        self.road = self.screen.ids['road']
        self.bike = self.screen.ids['bike']

        self.bike.y = self.road.y
        self.bike.speed = 100
        self.bike.power = 150
        self.bike.max_power = 300

    def test_go_start(self):
        self.set_app()
        self.road.go_start()
        self.assertEqual(self.road.state, State.ON_GO_START)

    # def test_go_move(self):
    #     self.set_app()
    #     self.bike.power = self.bike.max_power/2
    #     self.road.on_jump(.1)
    #     self.assertEqual(self.road.state, State.ON_JUMP_MOVE)
    #
    # def test_go_stop(self):
    #     self.set_app()
    #     self.bike.y = self.road.y*2
    #     self.bike.power = 1
    #     self.road.on_jump(.1)
    #     self.road.jump_stop()
    #     self.assertEqual(self.road.state, State.ON_JUMP_STOP)
