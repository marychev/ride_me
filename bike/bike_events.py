from bike.event_relax import RelaxBikeEvent
# from bike.event_stop import StopBikeEvent
from bike.event_wait import WaitBikeEvent
from bike.event_move import MoveBikeEvent
from bike.event_landing import LandingBikeEvent


class BikeEvents(WaitBikeEvent, MoveBikeEvent, RelaxBikeEvent, LandingBikeEvent):
    pass
