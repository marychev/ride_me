from typing import NamedTuple, Optional, Tuple
from utils.type import TPos


class GOModel(NamedTuple):
    sid: str
    pos: TPos
    size: Tuple[int, int]
    size_hint: Tuple[Optional[int], Optional[int]] = (None, None)

    def __repr__(self) -> str:
        return f'<GOModel {self.sid}>'
