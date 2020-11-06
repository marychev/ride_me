from .go import GoEventRoad
from .relax import RelaxEventRoad
from .stop import StopDispatcher
from .jump import JumpDispatcher
from .wait import WaitDispatcher
from .landing import LandingDispatcher


class RoadEvents(LandingDispatcher, WaitDispatcher, JumpDispatcher, StopDispatcher):
    pass
