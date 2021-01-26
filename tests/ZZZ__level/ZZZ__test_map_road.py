from tests.event.wait.base_wait_test import BaseWaitTest
from objects.start.start import Start
from objects.finish.finish import Finish
from objects.lamp.lamp import Lamp
from objects.rock.rock import Rock
from objects.puddle.puddle import Puddle
from utils.validation import ValidObject
from kivy.clock import Clock

WIDTH = 1060


TESTMAP = [
    Start.to_map((190, 60)),    # 1
    Lamp.to_map((600, 0)),      # 1
    Puddle.to_map((2000, 0)),   # 2
    Lamp.to_map((5000, 0)),   # 3
    Finish.to_map((10000, 80)), # 4
]


class MapRoadTest(BaseWaitTest):

    def test_gradual_loading_map_elements_onto_road(self):
        self.set_app()
        self.road.level.map = TESTMAP
        scene = ValidObject.scene(self.road.parent)

        # start first position
        first_map_names = [t['name'] for t in TESTMAP[0:2]]
        road_names = [r.__class__.__name__ for r in self.road.children[:]]
        self.assertEqual(sorted(road_names), sorted(first_map_names))

        self.road.distance_traveled = WIDTH
        Clock.schedule_once(scene.add_map_elements)

        # second position
        road_names = [r.__class__.__name__ for r in self.road.children[:]]
        second_map_names = [t['name'] for t in TESTMAP[2:3]]
        self.assertEqual(road_names[-1], second_map_names[0])

        # thirty position
        self.road.distance_traveled = 4200
        Clock.schedule_once(scene.add_map_elements)

        road_names = [r.__class__.__name__ for r in self.road.children[:]]
        thirty_map_names = [t['name'] for t in TESTMAP[3:4]]
        print([r.__class__.__name__ for r in self.road.children])
        print(thirty_map_names)
        self.assertEqual(road_names[-1], thirty_map_names[0])
