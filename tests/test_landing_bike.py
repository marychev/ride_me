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

    def assert_equals_for_pre_current(self, pre_event, current_event):
        self.assertEqual(self.app.scene.bike.pre_event, pre_event)
        self.assertEqual(self.app.scene.bike.current_event, current_event)

    def assert_equal_on_release_landing(self, btn):
        btn.on_release()
        self.assert_equals_for_pre_current(LANDING_EVENT_NAME, LANDING_EVENT_NAME)

    def assert_equal_on_press_landing(self, btn):
        btn.on_press()
        self.assert_equals_for_pre_current(LANDING_EVENT_NAME, LANDING_EVENT_NAME)

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

        # set landing values
        self.app.scene.bike.x = WIDTH_GAME / 2
        self.app.scene.bike.y = BaseLayout.tools_default_height() * 2    # has sky point
        self.app.scene.bike.set_landing(1)
        self.assert_equals_for_pre_current(LANDING_EVENT_NAME, LANDING_EVENT_NAME)

        # set collision values
        self.app.scene.bike.x = WIDTH_GAME / 2
        self.app.scene.bike.y = BaseLayout.tools_default_height()  # has road point
        self.app.scene.bike.set_landing(1)
        # check collision and a new WAIT state
        self.assert_equals_for_pre_current(LANDING_EVENT_NAME, 'on_wait')
        self.assertTrue(self.app.scene.bike.road_pos.y >= self.app.scene.bike.y)
        self.assertTrue(self.app.scene.bike.road_pos.y >= self.app.scene.bike.pos[1])
        self.assertTrue(self.app.scene.bike.acceleration == 0)
        self.assertTrue(self.app.scene.bike.speed < 1)
