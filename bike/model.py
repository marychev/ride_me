from decimal import Decimal
from typing import NamedTuple, Optional


class BikeModel(NamedTuple):
    title: str
    source: str
    source_go: str
    source_relax: str
    source_wait: str
    source_stop: str
    source_jump_up: str
    source_landing: str
    source_collision: str
    power: float
    max_power: Optional[float]
    speed: float
    max_speed: Optional[float]
    acceleration: float
    agility: float
    price: Decimal
    text: Optional[str]

    def __repr__(self) -> str:
        return f'<Employee {self.title}>'

