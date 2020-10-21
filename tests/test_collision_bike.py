# from kivy.tests.common import GraphicUnitTest
#
# from bike.event_wait import EVENT_NAME as WAIT_EVENT_NAME
# from rideme_game import RideMeGame
#
#
# class CollisionBikeTest(GraphicUnitTest):
#     def set_app(self):
#         self.app = RideMeGame()
#         self.render(self.app)
#
#     def test_collision_y_by_on_move(self):
#         self.set_app()
#         self.app.scene.bike.speed = 0
#         self.app.scene.bike.x = self.app.scene.bike.road_pos.x
#         self.app.scene.bike.y = self.app.scene.bike.road_pos.y
#
#         # self.app.scene.bike.on_wait()
#         # self.assertTrue(self.app.scene.bike.can_wait())
#         # self.assertEqual(self.app.scene.bike.current_event, WAIT_EVENT_NAME)
#
#         self.app.scene.bike.on_go()
#         self.assertTrue(self.app.scene.bike.can_go())
#         self.assertEqual(self.app.scene.bike.current_event, 'on_go')
#
#         # self.app.scene.bike.on_relax(0.1)
#         # self.assertTrue(self.app.scene.bike.can_relax())
#
#         # self.assertEqual(self.app.scene.bike.current_event, 'on_relax')
#         # print(self.app.scene.bike.show_status())
