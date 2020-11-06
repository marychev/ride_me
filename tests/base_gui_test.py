from kivy.tests.common import GraphicUnitTest
from screen.game_screen import GameScreen


class BaseGameScreenGUITest(GraphicUnitTest):
    def set_app(self):
        self.screen = GameScreen()
        self.render(self.screen)
        self.road = self.screen.ids['road']
        self.bike = self.screen.ids['bike']

        # default value
        self.bike.y = self.road.y
        self.bike.speed = 0
        self.bike.max_speed = 20
        self.bike.power = 0
        self.bike.max_power = 300
