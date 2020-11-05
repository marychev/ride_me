from .go import GoEventRoad
from .relax import RelaxEventRoad
from .stop import StopEventRoad
from .jump import JumpEventRoad
from .wait import WaitDispatcher
from .landing import LandingDispatcher


class RoadEvents(LandingDispatcher, WaitDispatcher):
    pass
