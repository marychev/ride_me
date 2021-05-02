from typing import TypeVar, Union, Dict, List, Tuple, Literal

TIntFloatStr = TypeVar('TIntFloatStr', int, float, str)

TJsonMapItem = Dict[str, Union[str, int, float, tuple]]
TJsonMap = List[TJsonMapItem]

TPosN = Union[int, float]
TPos = Tuple[TPosN, TPosN]
