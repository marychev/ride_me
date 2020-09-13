from kivy.tests.common import GraphicUnitTest

from layout.base import BaseLayout
from rideme_game import RideMeGame


ROAD_START_X = 80
ROAD_START_Y = BaseLayout.tools_default_height()
MOVE_EVENT_NAME = 'on_move'


class MoveBikeTest(GraphicUnitTest):
    def set_bike_pos(self):
        self.app.scene.bike.x = ROAD_START_X
        self.app.scene.bike.y = ROAD_START_Y
        self.app.scene.bike.on_wait()

    def set_app(self):
        self.app = RideMeGame()
        self.set_bike_pos()
        self.render(self.app)

    def assert_equals_for_pre_current(self, current_event):
        self.assertTrue(self.app.scene.bike.pre_event != current_event)
        self.assertEqual(self.app.scene.bike.current_event, current_event)

    def test_try_move(self):
        self.set_app()
        self.app.scene.bike.on_move(0)
        self.assert_equals_for_pre_current(MOVE_EVENT_NAME)

    def test_try_move_by_right_button(self):
        self.set_app()
        self.app.tool.right_btn.on_press()
        self.assert_equals_for_pre_current(MOVE_EVENT_NAME)
