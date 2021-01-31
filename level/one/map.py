from objects import Start, Finish, Lamp, Puddle, Rock


MAP = [
    Start.to_map((190, 60)),
    # Lamp.to_map((600, 80)),
    Lamp.to_map((1200, 80)),
    # Puddle.to_map((1500, 80)),
    Rock.to_map((2000, 80)),
    Puddle.to_map((3500, 80)),
    # Lamp.to_map((3800, 80)),
    # Lamp.to_map((4000, 80)),
    Finish.to_map((6000, 60)),
]


TEST_MAP = [
    Start.to_map((190, 60)),
    Lamp.to_map((600, 0)),
    #
    Lamp.to_map((4000, 0)),
    Puddle.to_map((4500, 0)),

    Lamp.to_map((6000, 0)),
    Rock.to_map((6500, 0)),

    Lamp.to_map((8000, 0)),
    Puddle.to_map((8400, 0)),
    Rock.to_map((8800, 0)),

    Lamp.to_map((10000, 0)),
    Puddle.to_map((10400, 0)),
    Puddle.to_map((10800, 0)),
    Puddle.to_map((11200, 0)),

    Lamp.to_map((12000, 0)),
    Rock.to_map((12500, 0)),
    Rock.to_map((13000, 0)),
    Rock.to_map((13980, 0)),

    Lamp.to_map((14000, 0)),
    Puddle.to_map((14400, 0)),
    Rock.to_map((14800, 0)),
    Puddle.to_map((15100, 0)),
    Puddle.to_map((15400, 0)),

    Lamp.to_map((16000, 0)),
    Puddle.to_map((16400, 0)),
    Puddle.to_map((16800, 0)),
    Puddle.to_map((17200, 0)),
    Puddle.to_map((17600, 0)),
    Puddle.to_map((18000, 0)),

    Lamp.to_map((18000, 0)),
    Puddle.to_map((18400, 0)),
    Puddle.to_map((18800, 0)),
    Puddle.to_map((19200, 0)),
    Puddle.to_map((19600, 0)),
    Puddle.to_map((19990, 0)),

    Finish.to_map((21000, 80))
]
