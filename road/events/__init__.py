from .go import GoDispatcher
from .relax import RelaxDispatcher
from .stop import StopDispatcher
from .jump import JumpDispatcher
from .wait import WaitDispatcher
from .landing import LandingDispatcher


class RoadEvents(JumpDispatcher, LandingDispatcher,
                 WaitDispatcher, RelaxDispatcher,
                 GoDispatcher, StopDispatcher):
    pass
