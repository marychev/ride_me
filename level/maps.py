from level.one.level_one import LevelOne


MAPS = [
    {
        "title": "Light Road",
        "level": LevelOne.__class__.__name__,
        "source": LevelOne.BACKGROUND_TEXTURE,
        "price": "5",
        "map": LevelOne.maps[0],
        "text": "Description\nSolar tlar the bike onto with others lar the with others \n"
                "lar the with others lar the  with others lar the with others lar the with"
                " others lar the with others lar the with others lar\n the with others lar "
                "the bike onto with others he bike onto with others words thi road/"
    },
    {
        "title": "Light Road-2",
        "level": LevelOne.__class__.__name__,
        "map": LevelOne.maps[1],
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
