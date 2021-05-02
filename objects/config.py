from enum import Enum
from typing import Type
from objects.base.game_image import GameImage
from objects import Start, Finish, Lamp, Currency, Puddle, Rock


class Register(Enum):
    Start = 1
    Finish = 2
    Currency = 3
    Lamp = 4
    Puddle = 5
    Rock = 6

    @classmethod
    def as_list(cls):
        return cls._member_names_

    @classmethod
    def get_class(cls,  class_name: str) -> Type[GameImage]:
        if class_name == cls.Start.name:
            return Start
        elif class_name == cls.Finish.name:
            return Finish
        elif class_name == cls.Lamp.name:
            return Lamp
        elif class_name == cls.Currency.name:
            return Currency
        elif class_name == cls.Puddle.name:
            return Puddle
        elif class_name == cls.Rock.name:
            return Rock
