from kivy.tests.common import GraphicUnitTest, UnitTestTouch
from kivy.base import EventLoop
from kivy.app import runTouchApp
from rideme_game import RideMeGame
from bike.event_landing import EVENT_NAME as LANDING_EVENT_NAME


class MyTestCase(GraphicUnitTest):
    def set_app(self):
        self.app = RideMeGame()
        self.render(self.app)
        self.bike = self.app.scene.bike

    def test_runtouchapp(self):
        self.set_app()

        # get your Window instance safely
        EventLoop.ensure_window()
        window = EventLoop.window

        # your asserts
        self.assertEqual(window.children[0], self.app)
        self.assertEqual(window.children[0].height, window.height)

    def test_left_button_touch_start_position_bike(self):
        self.set_app()

        # try to stop
        left_btn = self.app.tool.left_btn
        touch = UnitTestTouch(left_btn.x, left_btn.y)

        # start position - bike is flying
        touch.touch_down()
        self.assertEqual(self.bike.pre_event, LANDING_EVENT_NAME)
        self.assertEqual(self.bike.current_event, LANDING_EVENT_NAME)

        touch.touch_up()
        self.assertEqual(self.bike.pre_event, LANDING_EVENT_NAME)
        self.assertEqual(self.bike.current_event, LANDING_EVENT_NAME)

    def test_right_button_touch_start_position_bike(self):
        self.set_app()

        # try to move
        right_btn = self.app.tool.right_btn
        touch = UnitTestTouch(right_btn.x, right_btn.y)

        # start position - bike is flying
        touch.touch_down()
        self.assertEqual(self.bike.pre_event, LANDING_EVENT_NAME)
        self.assertEqual(self.bike.current_event, LANDING_EVENT_NAME)

        touch.touch_up()
        self.assertEqual(self.bike.pre_event, LANDING_EVENT_NAME)
        self.assertEqual(self.bike.current_event, LANDING_EVENT_NAME)
