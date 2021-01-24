from tests.event.wait.base_wait_test import BaseWaitTest
from objects.start.start import Start
from objects.finish.finish import Finish
from objects.lamp.lamp import Lamp
from kivy.core.window import Window

WIDTH = int(Window.width)

TESTMAP = [
    Start.to_map((190, 60)),
    Lamp.to_map((600, 0)),
    Lamp.to_map((1200, 0)),
    Lamp.to_map((2000, 0)),
    Lamp.to_map((5000, 0)),
    Lamp.to_map((9000, 0)),
    Finish.to_map((10000, 80)),
]


class MapRoadTest(BaseWaitTest):

    def test_gradual_loading_map_elements_onto_road(self):
        self.set_app()
        self.road.level.map = TESTMAP

        # start first position
        first_map_names = [t['name'] for t in TESTMAP[0:2]]
        road_names = [r.__class__.__name__ for r in self.road.children[:]]

        print(self.road.parent)

        self.assertNotEqual(sorted(road_names), sorted(first_map_names))

        self.road.distance_traveled = WIDTH


