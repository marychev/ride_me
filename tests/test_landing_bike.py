from kivy.base import EventLoop
from kivy.tests.common import GraphicUnitTest

from bike.event_landing import EVENT_NAME as LANDING_EVENT_NAME
from conf import HEIGHT_GAME, WIDTH_GAME
from layout.base import BaseLayout
from rideme_game import RideMeGame


class LandingBikeBehaviorTest(GraphicUnitTest):
    def set_bike_pos(self, x=WIDTH_GAME/2, y=HEIGHT_GAME/2):
        self.app.scene.bike.x = x
        self.app.scene.bike.y = y
        self.app.scene.bike.landing()

    def set_app(self):
        self.app = RideMeGame()
        self.render(self.app)

    def assert_equal_on_release_landing(self, btn):
        btn.on_release()
        self.assertEqual(self.app.scene.bike.pre_event, LANDING_EVENT_NAME)
        self.assertEqual(self.app.scene.bike.current_event, LANDING_EVENT_NAME)

    def assert_equal_on_press_landing(self, btn):
        btn.on_press()
        self.assertEqual(self.app.scene.bike.pre_event, LANDING_EVENT_NAME)
        self.assertEqual(self.app.scene.bike.current_event, LANDING_EVENT_NAME)

    def test_runtouchapp(self):
        self.set_app()

        # get your Window instance safely
        EventLoop.ensure_window()
        window = EventLoop.window

        # your asserts
        self.assertEqual(window.children[0], self.app)
        self.assertEqual(window.children[0].height, window.height)

    def test_try_stop_by_left_button(self):
        self.set_app()
        self.set_bike_pos()

        left_btn = self.app.tool.left_btn
        self.assert_equal_on_press_landing(left_btn)
        self.assert_equal_on_release_landing(left_btn)

    def test_try_move_by_right_button(self):
        self.set_app()
        self.set_bike_pos()

        right_btn = self.app.tool.right_btn
        self.assert_equal_on_press_landing(right_btn)
        self.assert_equal_on_release_landing(right_btn)

    def test_collision_to_land_correctly(self):
        self.set_app()
        self.set_bike_pos()

        self.app.scene.bike.y = BaseLayout.tools_default_height() - 1
        self.app.scene.bike.landing()
        self.assertEqual(self.app.scene.bike.current_event, 'on_wait')
