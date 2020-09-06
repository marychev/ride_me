from bike.event_landing import LandingBikeEvent
from bike.event_move import MoveBikeEvent
from bike.event_relax import RelaxBikeEvent


class BikeEvent(LandingBikeEvent, MoveBikeEvent, RelaxBikeEvent):
    pass
