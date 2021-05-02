from typing import NamedTuple, Optional


class BikeModel(NamedTuple):
    title: str
    source: str
    source_go: Optional[str]
    source_relax: Optional[str]
    source_wait: Optional[str]
    source_stop: Optional[str]
    source_jump_up: Optional[str]
    source_landing: Optional[str]
    source_collision: Optional[str]
    power: float
    max_power: Optional[float]
    speed: float
    max_speed: Optional[float]
    acceleration: float
    agility: float
    price: int  # rm
    text: Optional[str]

    def __repr__(self) -> str:
        return f'<BikeModel {self.title}>'

    @staticmethod
    def create_empty():
        return BikeModel(
            title='None', source='', power=0, max_power=0, speed=0, max_speed=0,
            acceleration=0, agility=0, price=0, text='',
            source_go=None, source_wait=None, source_relax=None, source_stop=None, source_jump_up=None,
            source_landing=None, source_collision=None)
