from level.base.base_level import BaseLevel
from level.one.map import MAP


TEST_MAP2 = [
    {"name": 'Start', "pos": (190, 60)},
    {"name": 'Lamp', "pos": (1000, 0)},
    {"name": 'Lamp', "pos": (2000, 0)},
    {"name": 'Lamp', "pos": (3000, 0)},
    {"name": 'Lamp', "pos": (4000, 0)},
    {"name": 'Lamp', "pos": (5000, 0)},
    {"name": 'Lamp', "pos": (6000, 0)},
    {"name": 'Lamp', "pos": (7000, 0)},
    {"name": 'Lamp', "pos": (8000, 0)},
    {"name": 'Lamp', "pos": (9000, 0)},
    {"name": 'Lamp', "pos": (10000, 0)},
    {"name": 'Lamp', "pos": (11000, 0)},
    {"name": 'Lamp', "pos": (12000, 0)},
    {"name": 'Lamp', "pos": (13000, 0)},
    {"name": 'Lamp', "pos": (14000, 0)},
    {"name": 'Lamp', "pos": (15000, 0)},
    {"name": 'Lamp', "pos": (16000, 0)},
    {"name": 'Lamp', "pos": (17000, 0)},
    {"name": 'Lamp', "pos": (18000, 0)},
    {"name": 'Lamp', "pos": (19000, 0)},
    {"name": 'Lamp', "pos": (20000, 0)},
    # {"name": 'Puddle', "pos": (1600, 0)},
    # {"name": 'Lamp', "pos": (2400, 0)},
    # {"name": 'Rock', "pos": (2600, 0)},
    {"name": 'Finish', "pos": (150000, 60)}
]


class LevelOne(BaseLevel):
    """ Straight track """

    def __init__(self, road, bike):
        super().__init__(road, bike, TEST_MAP2)
