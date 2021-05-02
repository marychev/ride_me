from level.base.base_level import BaseLevel
from level.one.map import MAP, TEST_MAP
from utils.texture import image_texture


class LevelOne(BaseLevel):
    BACKGROUND_SOURCE = 'layout/img/mountains-2.png'
    background_texture = image_texture(BACKGROUND_SOURCE)

    BACKGROUND_SOURCE_DEFAULT = 'layout/img/default.png'
    background_texture_default = image_texture(BACKGROUND_SOURCE_DEFAULT)

    ROAD_SOURCE = './road/img/road-l1.jpg'
    road_texture = image_texture(ROAD_SOURCE)

    name = 'I. Asphalt and mountains'
    maps = (MAP, TEST_MAP)

    def __init__(self, road, bike, map=MAP):
        super().__init__(road, bike, map)
