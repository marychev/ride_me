from bike.event_landing import LandingBikeEvent
from bike.event_move import MoveBikeEvent
from bike.event_relax import RelaxBikeEvent
from bike.event_stop import StopBikeEvent
from bike.base_event import BaseBikeEvent

class BikeEvents:
    on_wait
    on_landing = LandingBikeEvent()
    on_move = MoveBikeEvent()
    on_relax = RelaxBikeEvent(None)
    on_stop = StopBikeEvent(None)
