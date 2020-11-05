from kivy.base import EventLoop
from kivy.tests.common import GraphicUnitTest
from screen.game_screen import GameScreen
from utils.state import State
from kivy.clock import Clock


class LandingTest(GraphicUnitTest):
    def set_app(self):
        self.screen = GameScreen()
        self.render(self.screen)
        self.road = self.screen.ids['road']
        self.bike = self.screen.ids['bike']

        self.bike.y = self.road.y
        self.bike.speed = 0
        self.road.set_state(State.ON_WAIT_START)
        self.road.on_wait_start()

    def test_runtouchapp(self):
        self.set_app()

        # get your Window instance safely
        EventLoop.ensure_window()
        window = EventLoop.window

        # your asserts
        self.assertEqual(window.children[0], self.screen)
        self.assertEqual(window.children[0].height, window.height)

    # def test_landing_start(self):
    #     self.set_app()
    #     self.bike.y = self.road.y + 200
    #     self.road.set_state(State.ON_LANDING_START)
    #     self.road.on_landing_start()
    #     self.assertEqual(self.road.state, State.ON_LANDING_START)

    def test_landing_move(self):
        self.set_app()

        self.bike.y = self.road.y + 100
        can_do = self.road.on_landing(.1)

        print('>>> WHY ??? <<<')
        print(can_do)
        print(self.road.get_road().state)
        print(self.road.state)
        print('##########################')
        self.assertEqual(self.road.state, State.ON_LANDING_MOVE)

    # def test_bike_has_landed_already(self):
    #     self.set_app()
    #     self.bike.y = self.road.y
    #     self.road.on_landing(.1)
    #     self.assertEqual(self.road.state, State.ON_WAIT_START)
    #
    # def test_start_and_finish_landing_success(self):
    #     self.set_app()
    #     self.assertEqual(self.road.state, State.ON_WAIT_START)
    #
    #     self.bike.y = self.road.y + 10
    #     self.road.on_landing(.1)
    #     self.assertEqual(self.road.state, State.ON_LANDING_MOVE)
    #
    #     # bike is waiting for something actions
    #     self.bike.y = self.road.y
    #     self.road.on_wait(.1)
    #     self.assertEqual(self.road.state, State.ON_WAIT_MOVE)
    #
    # def test_try_go_fail(self):
    #     self.set_app()
    #
    #     self.bike.y = self.road.y + 200
    #     self.road.set_state(State.ON_LANDING_START)
    #     self.road.on_landing(.1)
    #
    #     self.road.set_state(State.ON_GO_START)
    #     self.road.on_go_start()
    #     print(self.road.state, '<<<<<')