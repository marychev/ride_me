from tests.base_gui_test import BaseGameScreenGUITest


class GoBackgroundTest(BaseGameScreenGUITest):
    def set_app(self):
        super().set_app()
        self.background = self.screen.ids['background']

        self.bike.speed = 10
        self.bike.max_speed = 20
        self.road.landing_stop()

    def test_go_mountains_start(self):
        self.set_app()
        old_uvpos = self.background.mountains_texture.uvpos
        self.background.is_repeat_texture = True
        self.road.go_start()
        self.background.on_go_mountains(.1)
        new_uvpos = self.background.mountains_texture.uvpos
        self.assertNotEqual(old_uvpos, new_uvpos)

    def test_on_go_mountains_move(self):
        self.set_app()
        self.background.is_repeat_texture = True
        old_uvpos = self.background.mountains_texture.uvpos
        self.bike.speed = self.bike.max_speed/2
        self.road.on_go(.1)
        self.background.on_go_mountains(.5)
        new_uvpos = self.background.mountains_texture.uvpos
        self.assertNotEqual(old_uvpos, new_uvpos)

    def test_go_mountains_stop(self):
        self.set_app()
        old_pos = self.background.mountains_texture.uvpos
        self.bike.speed = 0
        self.road.on_go(.1)
        self.road.go_stop()

        new_pos = self.background.mountains_texture.uvpos
        self.assertEqual(old_pos, new_pos)

