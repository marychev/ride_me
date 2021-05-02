from typing import NamedTuple, Optional, Union


class MapModel(NamedTuple):
    title: str
    level: Union[str, int]
    map: int
    source: str
    source_road: str
    total_way: int
    price: int
    text: Optional[str]

    def __repr__(self) -> str:
        return f'<MapModel {self.title}>'

    @staticmethod
    def create_empty():
        return MapModel(title='None', level='', map=0, source='', source_road='', total_way=0, price=0, text='')
