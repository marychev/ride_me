# from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, StringProperty
from bike.event_relax import RelaxBikeEvent
# from bike.event_stop import StopBikeEvent
from bike.event_wait import WaitBikeEvent
from bike.event_move import MoveBikeEvent
from bike.event_landing import LandingBikeEvent

WAIT_EVENT_NAME = 'on_wait'


class BikeEvents(WaitBikeEvent, MoveBikeEvent, RelaxBikeEvent, LandingBikeEvent):
    # on_wait = ObjectProperty(None)
    # on_landing = ObjectProperty(None)
    # on_move = ObjectProperty(None)
    # on_relax = ObjectProperty(None)
    # on_stop = ObjectProperty(None)

    pass