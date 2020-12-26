from level.base.base_level import BaseLevel
from level.one.map import MAP, TEST_MAP
from level.utils.map_road import straight_road

straight_map = straight_road()


class LevelOne(BaseLevel):
    """ Straight track """

    def __init__(self, road, bike):
        # super().__init__(road, bike, MAP)
        super().__init__(road, bike, TEST_MAP)
        # super().__init__(road, bike, straight_map)

