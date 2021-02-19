from level.base.base_level import BaseLevel
from level.one.map import MAP, TEST_MAP
from utils.texture import image_texture


class LevelOne(BaseLevel):
    """ Straight track """

    BACKGROUND_TEXTURE = 'layout/img/mountains-2.png'
    road_texture = image_texture('road/img/road-l1.jpg')
    background_texture = image_texture(BACKGROUND_TEXTURE)
    name = 'I. Asphalt and mountains'

    def __init__(self, road, bike):
        super().__init__(road, bike, TEST_MAP)


