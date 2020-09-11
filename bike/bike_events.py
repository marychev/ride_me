from bike.event_landing import LandingBikeEvent
from bike.event_move import MoveBikeEvent
from bike.event_relax import RelaxBikeEvent
from bike.event_stop import StopBikeEvent


class BikeEvents(MoveBikeEvent, RelaxBikeEvent, StopBikeEvent, LandingBikeEvent):
    pass
