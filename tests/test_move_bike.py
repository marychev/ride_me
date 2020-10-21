from kivy.tests.common import GraphicUnitTest

ROAD_START_X = 80
ROAD_START_Y = 120
MOVE_EVENT_NAME = 'on_go'


class MoveBikeTest(GraphicUnitTest):
    def set_bike_pos(self):
        self.app.scene.bike.x = ROAD_START_X
        self.app.scene.bike.y = ROAD_START_Y
        self.app.scene.bike.on_wait()

    def set_app(self):
        self.app = RideMeGame()
        self.set_bike_pos()
        self.render(self.app)

    def assert_equals_move(self):
        self.assertEqual(self.app.scene.bike.current_event, MOVE_EVENT_NAME)

    def test_try_move(self):
        self.set_app()
        self.app.scene.bike.on_go()
        self.assert_equals_move()

    # def test_try_move_by_right_button(self):
    #     self.set_app()
    #     self.app.tool.right_btn.on_press()
    #     self.assert_equals_for_pre_current(MOVE_EVENT_NAME)
