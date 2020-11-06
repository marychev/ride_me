from kivy.base import EventLoop
from tests.base_gui_test import BaseGameScreenGUITest


class RunTouchAppTest(BaseGameScreenGUITest):
    def set_app(self):
        super().set_app()

    def test_runtouchapp(self):
        self.set_app()

        # get your Window instance safely
        EventLoop.ensure_window()
        window = EventLoop.window

        # your asserts
        self.assertEqual(window.children[0], self.screen)
        self.assertEqual(window.children[0].height, window.height)
