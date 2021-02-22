BIKES = [
    {
        "title": "Hell Ride",
        "source": "./bike/img/bike-landing.png",
        "power": "150",
        "speed": "10",
        "acceleration": "3",
        "agility": "5",
        "price": "992",
        "text": "Description\nSolar tlar the bike onto with others lar the with others \n"
                       "lar the with others lar the  with others lar the with others lar the with"
                       " others lar the with others lar the with others lar\n the with others lar "
                       "the bike onto with others he bike onto with others words thi road/"
    },
    {
        "title": "Geisha",
        "source": "./bike/img/bike-relax.png",
        "power": "150",
        "speed": "10",
        "acceleration": "0",
        "agility": "0",
        "price": "992",
        "text": "Description\nSolar tlar the bike onto with others lar the with others \n"
                 "the bike onto with others he bike onto with others words thi road/"
    },
    {
        "title": "Default",
        "source": "./bike/img/bike-1.png",
        "power": "150",
        "speed": "10",
        "acceleration": "0",
        "agility": "0",
        "price": "992",
        "text": "Description\nSolar tlar the bike onto with others lar the with others \n"
    }
]


def get_by_title(value):
    for b in BIKES:
        if b['title'] == value:
            return b
