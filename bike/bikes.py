from utils.init import get_item_by_title_or_index


BIKES = [
    {
        "title": "Hell Ride",
        "source": "./bike/img/bike-landing.png",
        "source_go": "./bike/img/bike-go.png",
        "source_relax": "./bike/img/bike-relax.png",
        "source_wait": "./bike/img/bike-wait.png",
        "source_stop": "./bike/img/bike-stop.png",
        "source_jump_up": "./bike/img/bike-jump-up.png",
        "source_landing": "./bike/img/bike-landing.png",
        "source_collision": "./bike/img/bike-1.png",
        "power": "180",
        "speed": "20",
        "acceleration": "3",
        "agility": "5",
        "price": "920",
        "text": "Управление:\n" 
                    "Ехать: правая кнопка\n"
                    "Тормоз: левая кнопка\n"
                    "Прыжок: левая кнопка х 2 раза\n"
                    "the bike onto with others he bike onto with others words thi road/"
    },
    {
        "title": "Geisha",
        "source": "./bike/img/bike-landing__draft.png",
        "source_go": "./bike/img/bike-landing__draft.png",
        "source_relax": "./bike/img/bike-landing__draft.png",
        "source_wait": "./bike/img/bike-landing__draft.png",
        "source_stop": "./bike/img/bike-landing__draft.png",
        "source_jump_up": "./bike/img/bike-landing__draft.png",
        "source_landing": "./bike/img/bike-landing__draft.png",
        "source_collision": "./bike/img/bike-landing__draft.png",
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
