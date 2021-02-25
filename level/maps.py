from level.one.level_one import LevelOne
from utils.init import get_item_by_title_or_index


MAPS = [
    {
        "title": "Light Road",
        "level": LevelOne.__name__,
        "source": LevelOne.BACKGROUND_TEXTURE,
        "price": "5",
        "map": 0,
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
        "source": LevelOne.BACKGROUND_TEXTURE,
        "price": "7",
        "text": "Description\nSolar tlar the bike onto with others lar the with others \n"
                "the bike onto with others he bike onto with others words thi road/"
    }
]


def get_by_title(value):
    return get_item_by_title_or_index(MAPS, value)
