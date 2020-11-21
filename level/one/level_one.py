from level.base_level import BaseLevel
from level.one.map import MAP

TEST_MAP2 = [
    {
        "name": 'Start',
        "pos": (120, 100),
    },
    {
        "name": 'Rock',
        "pos": (500, 80),
    },
    {
        "name": 'Rock',
        "pos": (800, 80),
    },
]


class LevelOne(BaseLevel):
    """ Straight track """

    def __init__(self, road, bike):
        super().__init__(road, bike, TEST_MAP2)



# KV LANG
#
# Start:
#    id: start
#    pos: 120 + root.ids.bike.width - 50, root.ids.road.y
#    size: 50, (root.ids.road.height / 2) + 10
#    size_hint: None, None

# Rock:
#    id: rock
#    pos: 800, root.ids.road.line_points[-1]
#    size: self.texture_size
# Puddle:
#    id: puddle
#    pos: 1000, root.ids.road.line_points[-1] - self.height/2
#    size: self.texture_size
# Lamp:
#    id: lamp
#    pos: 1500, root.ids.road.line_points[-1]
#    size: self.texture_size

# Finish:
#    id: finish
#    pos: root.ids.road.total_way, root.ids.tools.height
#    size: 120, (root.ids.road.height / 2) + 10
#    size_hint: None, None
