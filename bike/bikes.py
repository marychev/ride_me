from typing import Union
from kivy.logger import Logger
from bike.model import BikeModel


BIKES = [
    {
        "title": "Hell Ride",
        "source": "./bike/img/1/landing.png",
        "source_go": "./bike/img/1/go.png",
        "source_relax": "./bike/img/1/relax.png",
        "source_wait": "./bike/img/1/wait.png",
        "source_stop": "./bike/img/1/stop.png",
        "source_jump_up": "./bike/img/1/jump-up.png",
        "source_landing": "./bike/img/1/landing.png",
        "source_collision": "./bike/img/1/collision.png",
        "power": 180,
        "max_power": 300,
        "speed": 20,
        "max_speed": 40,
        "acceleration": 3,
        "agility": 5,
        "price": 920,
        "text": "Управление:\n" 
                    "Ехать: правая кнопка\n"
                    "Тормоз: левая кнопка\n"
                    "Прыжок: левая кнопка х 2 раза\n"
                    "the bike onto with others he bike onto with others words thi road/"
    },
    {
        "title": "Geisha",
        "source": "./bike/img/2/landing.png",
        "source_go": "./bike/img/2/go.png",
        "source_relax": "./bike/img/2/relax.png",
        "source_wait": "./bike/img/2/wait.png",
        "source_stop": "./bike/img/2/stop.png",
        "source_jump_up": "./bike/img/2/jump-up.png",
        "source_landing": "./bike/img/2/landing.png",
        "source_collision": "./bike/img/2/collision.png",
        "power": 190,
        "max_power": 280,
        "speed": 15,
        "max_speed": 28,
        "acceleration": 0,
        "agility": 0,
        "price": 900,
        "text": "Description\nSolar tlar the bike onto with others lar the with others \n"
                 "the bike onto with others he bike onto with others words thi road/"
    },
    {
        "title": "Default",
        "source": "./bike/img/bike-1.png",
        "source_go": "./bike/img/bike-1.png",
        "source_relax": "./bike/img/bike-1.png",
        "source_wait": "./bike/img/bike-1.png",
        "source_stop": "./bike/img/bike-1.png",
        "source_jump_up": "./bike/img/bike-1.png",
        "source_landing": "./bike/img/bike-1.png",
        "source_collision": "./bike/img/bike-1.png",
        "power": 180,
        "max_power": 290,
        "speed": 20,
        "max_speed": 30,
        "acceleration": 1,
        "agility": 1,
        "price": 800,
        "text": "Description\nSolar tlar the bike onto with others lar the with others \n"
    }
]


def get_by_title(value: Union[str, int]) -> BikeModel:
    from utils.init import get_item_by_title_or_index

    try:
        return BikeModel(**get_item_by_title_or_index(BIKES, value))
    except TypeError as TE:
        Logger.error('{}: {}'.format(value, TE))

        # [note]: __new__() missing 7 required positional arguments:
        _model = get_item_by_title_or_index(BIKES, value)
        _model['source_go'] = None
        _model['source_relax'] = None
        _model['source_wait'] = None
        _model['source_stop'] = None
        _model['source_jump_up'] = None
        _model['source_landing'] = None
        _model['source_collision'] = None

        return BikeModel(**_model)

