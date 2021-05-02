from utils.sizes import ROAD_BIKE_POINT_Y, START_POS_X
from objects import Start, Finish, Lamp, Puddle, Rock, Currency


MAP = [
    Start.to_map(START_POS_X),
    Lamp.to_map(120),

    Currency.to_map(600),
    Lamp.to_map(1000),
    Puddle.to_map(1200),

    Lamp.to_map(2000),
    Rock.to_map(2500),

    Lamp.to_map(3000),
    Currency.to_map(3500),
    Rock.to_map(3800),

    Lamp.to_map(4000),
    Currency.to_map(4100, 150),
    Puddle.to_map(4200),
    Puddle.to_map(4800),

    Lamp.to_map(5000),
    Currency.to_map(5550, 250),
    Rock.to_map(5600),
    Puddle.to_map(5900),

    Lamp.to_map(6000),
    Currency.to_map(6550, 230),
    Rock.to_map(6600),

    Lamp.to_map(7000),
    Rock.to_map(7100),
    Puddle.to_map(7400),

    Lamp.to_map(8000),
    Rock.to_map(8100),

    Lamp.to_map(9000),
    Puddle.to_map(9200),
    Puddle.to_map(9500),
    Puddle.to_map(9900),

    Currency.to_map(9950),
    Finish.to_map(12000, ROAD_BIKE_POINT_Y),
]


TEST_MAP = [
    Start.to_map(190),
    Lamp.to_map(600),
    Currency.to_map(1000, 230),

    Lamp.to_map(2000),
    Puddle.to_map(2400),
    Currency.to_map(2600),

    Lamp.to_map(4000),
    Rock.to_map(4500),
    Currency.to_map(4700),

    Lamp.to_map(6000),
    Puddle.to_map(6400),
    Currency.to_map(6750, 250),
    Rock.to_map(6800),

    Lamp.to_map(8000),
    Currency.to_map(8100, 300),
    Puddle.to_map(8400),
    Currency.to_map(8600, 270),
    Rock.to_map(8800),
    Currency.to_map(9000, 280),
    Puddle.to_map(9200),

    Finish.to_map(13000, ROAD_BIKE_POINT_Y)
]
