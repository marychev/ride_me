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
    Lamp.to_map((2000, 0)),

    Lamp.to_map((4000, 0)),
    Puddle.to_map((4500, 0)),

    Lamp.to_map((6000, 0)),
    Rock.to_map((6500, 0)),

    Lamp.to_map((8000, 0)),
    Puddle.to_map((8400, 0)),
    Rock.to_map((8800, 0)),

    Lamp.to_map((10000, 0)),
    Puddle.to_map((10350, 0)),
    Puddle.to_map((10700, 0)),
    Puddle.to_map((10950, 0)),

    Lamp.to_map((12000, 0)),
    Lamp.to_map((14000, 0)),
    Lamp.to_map((16000, 0)),
    Lamp.to_map((18000, 0)),
    Lamp.to_map((200000, 0)),

    Finish.to_map((21000, 60))
]
