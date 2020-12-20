from road.start.start import Start
from road.finish.finish import Finish
from objects.lamp.lamp import Lamp
from objects.rock.rock import Rock
from objects.puddle.puddle import Puddle


MAP = [
    Lamp.to_map((130, 125)),
    Start.to_map((190, 60)),
    Rock.to_map((800, 0)),

    Lamp.to_map((1000, 0)),
    Puddle.to_map((1400, 0)),

    Lamp.to_map((2000, 0)),
    Rock.to_map((2200, 0)),
    Puddle.to_map((2300, 0)),

    Finish.to_map((3000, 80)),
]


TEST_MAP = [
    Start.to_map((190, 60)),
    Lamp.to_map((1000, 0)),
    Puddle.to_map((1600, 0)),
    Lamp.to_map((2400, 0)),
    Rock.to_map((2600, 0)),
    Finish.to_map((4000, 60))
]
