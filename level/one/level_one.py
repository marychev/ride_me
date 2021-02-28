from level.base.base_level import BaseLevel
from level.one.map import MAP, TEST_MAP
from utils.texture import image_texture


class LevelOne(BaseLevel):
    """ Straight track """

    BACKGROUND_TEXTURE = 'layout/img/mountains-2.png'
    BACKGROUND_TEXTURE_DEFAULT = 'layout/img/default.png'
    road_texture = image_texture('road/img/road-l1.jpg')
    background_texture = image_texture(BACKGROUND_TEXTURE)
    background_texture_default = image_texture(BACKGROUND_TEXTURE_DEFAULT)
    name = 'I. Asphalt and mountains'
    maps = (MAP, TEST_MAP)

    def __init__(self, road, bike, map=MAP):
        super().__init__(road, bike, map)


