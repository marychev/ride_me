from utils.init import get_item_by_title_or_index


BIKES = [
    {
        "title": "Hell Ride",
        "source": "./bike/img/bike-landing.png",
        "power": "180",
        "speed": "20",
        "acceleration": "3",
        "agility": "5",
        "price": "920",
        "text": "Description\nSolar tlar the bike onto with others lar the with others \n"
                       "lar the with others lar the  with others lar the with others lar the with"
                       " others lar the with others lar the with others lar\n the with others lar "
                       "the bike onto with others he bike onto with others words thi road/"
    },
    {
        "title": "Geisha",
        "source": "./bike/img/bike-relax.png",
        "power": "190",
        "speed": "15",
        "acceleration": "0",
        "agility": "0",
        "price": "900",
        "text": "Description\nSolar tlar the bike onto with others lar the with others \n"
                 "the bike onto with others he bike onto with others words thi road/"
    },
    {
        "title": "Default",
        "source": "./bike/img/bike-1.png",
        "power": "180",
        "speed": "20",
        "acceleration": "1",
        "agility": "1",
        "price": "800",
        "text": "Description\nSolar tlar the bike onto with others lar the with others \n"
    }
]


def get_by_title(value):
    return get_item_by_title_or_index(BIKES, value)
