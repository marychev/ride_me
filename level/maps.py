from level.one.level_one import LevelOne


MAPS = [
    {
        "title": "Light Road",
        "level": "LevelOne",
        "source": LevelOne.BACKGROUND_TEXTURE,
        "price": "5",
        "text": "Description\nSolar tlar the bike onto with others lar the with others \n"
                       "lar the with others lar the  with others lar the with others lar the with"
                       " others lar the with others lar the with others lar\n the with others lar "
                       "the bike onto with others he bike onto with others words thi road/"
    },
    {
        "title": "Light Road-2",
        "level": "LevelOne",
        "source": LevelOne.BACKGROUND_TEXTURE,
        "price": "7",
        "text": "Description\nSolar tlar the bike onto with others lar the with others \n"
                "the bike onto with others he bike onto with others words thi road/"
    }
]


def get_by_title(value):
    for b in MAPS:
        if b['title'] == value:
            return b
