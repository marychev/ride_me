from level.base.base_level import BaseLevel
from level.one.map import MAP


TEST_MAP2 = [
    {"name": 'Start', "pos": (190, 60)},
    {"name": 'Lamp', "pos": (400, 0)},
    {"name": 'Puddle', "pos": (600, 0)},
    {"name": 'Lamp', "pos": (1400, 0)},
    {"name": 'Rock', "pos": (2000, 0)},
    {"name": 'Finish', "pos": (3000, 60)}
]


class LevelOne(BaseLevel):
    """ Straight track """

    def __init__(self, road, bike):
        super().__init__(road, bike, MAP)
