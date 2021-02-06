from objects import Start, Finish, Lamp, Puddle, Rock, Currency


MAP = [
    Start.to_map((190, 60)),
    Lamp.to_map((120, 120)),

    Currency.to_map((600, 200)),
    Lamp.to_map((1000, 80)),
    Puddle.to_map((1200, 80)),

    Lamp.to_map((2000, 80)),
    Rock.to_map((2500, 80)),

    Lamp.to_map((3000, 80)),
    Currency.to_map((3500, 120)),
    Rock.to_map((3800, 80)),

    Lamp.to_map((4000, 80)),
    Currency.to_map((4100, 150)),
    Puddle.to_map((4200, 80)),
    Puddle.to_map((4800, 80)),

    Lamp.to_map((5000, 80)),
    Currency.to_map((5550, 150)),
    Rock.to_map((5600, 80)),
    Puddle.to_map((5900, 80)),

    Lamp.to_map((6000, 80)),
    Currency.to_map((6550, 150)),
    Rock.to_map((6600, 80)),

    Lamp.to_map((7000, 80)),
    Rock.to_map((7100, 80)),
    Puddle.to_map((7400, 80)),

    Lamp.to_map((8000, 80)),
    Rock.to_map((8100, 80)),

    Lamp.to_map((9000, 80)),
    Puddle.to_map((9200, 80)),
    Puddle.to_map((9500, 80)),
    Puddle.to_map((9900, 80)),

    Currency.to_map((9950, 200)),
    Finish.to_map((10000, 60)),
]


TEST_MAP = [
    Start.to_map((190, 60)),
    Lamp.to_map((600, 0)),
    Currency.to_map((1000, 180)),

    Lamp.to_map((2000, 0)),
    Puddle.to_map((2400, 0)),
    Currency.to_map((2600, 120)),

    Lamp.to_map((4000, 0)),
    Rock.to_map((4500, 0)),
    Currency.to_map((4700, 200)),

    Lamp.to_map((6000, 0)),
    Puddle.to_map((6400, 0)),
    Currency.to_map((6750, 150)),
    Rock.to_map((6800, 0)),

    Lamp.to_map((8000, 0)),
    Currency.to_map((8100, 200)),
    Puddle.to_map((8400, 0)),
    Currency.to_map((8600, 150)),
    Rock.to_map((8800, 0)),
    Currency.to_map((9000, 180)),
    Puddle.to_map((9200, 0)),

    Finish.to_map((10000, 80))
]
