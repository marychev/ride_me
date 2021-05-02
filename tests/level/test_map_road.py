from tests.base_gui_test import BaseGameScreenGUITest
from objects import Start, Finish, Lamp, Puddle, Rock

WIDTH = 1060


TESTMAP = [
    Start.to_map(190),        # 1
    Lamp.to_map(600),          # 1
    Puddle.to_map(2000),       # 2
    Rock.to_map(5000),         # 3
    Finish.to_map(10000),     # 4
]


class MapRoadTest(BaseGameScreenGUITest):
    def test_check_error(self):
        self.set_app()
        self.road.level.map = TESTMAP

        # start first position
        self.road.distance_traveled = 0
        self.road.set_distance_traveled()
        start_map_names = [t['name'] for t in TESTMAP[0:2]]
        road_names = [r.__class__.__name__ for r in self.road.children[:]]
        self.assertEqual(road_names[0], start_map_names[1])
        self.assertEqual(road_names[1], start_map_names[0])

        # test initial `sid`
        self.assertEqual(str(self.road.children[1]), Start.init_sid(TESTMAP[0]['pos']))
        self.assertEqual(self.road.children[1].sid, Start.init_sid(TESTMAP[0]['pos']))

    def test_gradual_loading_and_deleting_map_elements_onto_road(self):
        self.set_app()
        self.road.level.map = TESTMAP

        # start first position
        self.road.distance_traveled = 0
        self.road.set_distance_traveled()
        start_map_names = [t['name'] for t in TESTMAP[0:2]]
        road_names = [r.__class__.__name__ for r in self.road.children[:]]
        self.assertEqual(road_names[1], start_map_names[0])
        self.assertEqual(road_names[0], start_map_names[1])

        # second position
        self.road.distance_traveled = 1500
        self.road.set_distance_traveled()
        road_names = [r.__class__.__name__ for r in self.road.children[:]]
        second_map_names = [t['name'] for t in TESTMAP[2:3]]
        self.assertEqual(road_names[0], second_map_names[0])

        # thirty position
        self.road.distance_traveled = 4200
        self.road.set_distance_traveled()
        road_names = [r.__class__.__name__ for r in self.road.children[:]]
        thirty_map_names = [t['name'] for t in TESTMAP[3:4]]
        self.assertEqual(road_names[0], thirty_map_names[0])

        # finish last position
        self.road.distance_traveled = 9500
        self.road.set_distance_traveled()
        road_names = [r.__class__.__name__ for r in self.road.children[:]]
        finish_map_names = [t['name'] for t in TESTMAP[4:5]]
        self.assertEqual(road_names[0], finish_map_names[0])
