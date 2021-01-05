from level.base.base_level import BaseLevel
from level.one.map import MAP, TEST_MAP


class LevelOne(BaseLevel):
    """ Straight track """

    def __init__(self, road, bike):
        super().__init__(road, bike, MAP)

