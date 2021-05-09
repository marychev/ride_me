from kivy.logger import Logger
from typing import Union
from level.model import MapModel
from level.one.level_one import LevelOne


MAPS = [
    {
        "title": "Light Road",
        "level": LevelOne.__name__,
        "source": LevelOne.BACKGROUND_SOURCE,
        "price": "5",
        "map": 0,
        "source_road": LevelOne.ROAD_SOURCE,
        "total_way": LevelOne.total_way(LevelOne.maps[0]),
        "text": "Description\nSolar tlar the bike onto with others lar the with others \n"
                "lar the with others lar the  with others lar the with others lar the with"
                " others lar the with others lar the with others lar\n the with others lar "
                "the bike onto with others he bike onto with others words thi road/"
    },
    {
        "title": "Light Road-2",
        "level": LevelOne.__name__,
        "map": 1,
        "total_way": LevelOne.total_way(LevelOne.maps[1]),
        "source": LevelOne.BACKGROUND_SOURCE,
        "source_road": LevelOne.ROAD_SOURCE,
        "price": "7",
        "text": "Description\nSolar tlar the bike onto with others lar the with others \n"
                "the bike onto with others he bike onto with others words thi road/"
    },
    {
        "title": "Default",
        "level": LevelOne.__name__,
        "map": 0,
        "total_way": LevelOne.total_way(LevelOne.maps[0]),
        "source": LevelOne.BACKGROUND_SOURCE_DEFAULT,
        "source_road": LevelOne.ROAD_SOURCE,
        "price": "55",
        "text": "Description\nSolar tlar the bike onto with others lar the with others"
    }
]


def get_by_title(value: Union[str, int]) -> MapModel:
    if value:
        from utils.init import get_item_by_title_or_index

        try:
            return MapModel(**get_item_by_title_or_index(MAPS, value))
        except TypeError as TE:
            Logger.error('{}: {}'.format(value, TE))
            return MapModel(**get_item_by_title_or_index(MAPS, value))
