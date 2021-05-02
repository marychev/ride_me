from typing import NamedTuple, Optional, Tuple


class GOModel(NamedTuple):
    sid: str
    pos: Tuple[int, int]
    size: Tuple[int, int]
    size_hint: Tuple[Optional[int], Optional[int]] = (None, None)

    def __repr__(self) -> str:
        return f'<GOModel {self.sid}>'
