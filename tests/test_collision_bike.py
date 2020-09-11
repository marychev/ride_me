from kivy.tests.common import GraphicUnitTest

from bike.base_event import EVENT_NAME as WAIT_EVENT_NAME
from layout.base import BaseLayout
from rideme_game import RideMeGame


class CollisionBikeTest(GraphicUnitTest):
    def set_app(self):
        self.app = RideMeGame()
        self.render(self.app)

    def test_collision_y_by_on_move(self):
        self.set_app()
        self.app.scene.bike.y = BaseLayout.tools_default_height()
        self.app.scene.bike.set_wait(1)
        self.assertEqual(self.app.scene.bike.current_event, WAIT_EVENT_NAME)
