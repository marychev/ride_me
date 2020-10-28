from conf import SECOND_GAME
from .go import GoEventRoad
from kivy.clock import Clock
from kivy.properties import NumericProperty, ObjectProperty, StringProperty


class JumpEventRoad(GoEventRoad):
    def __init__(self, road, bike, rock, finish=None):
        super().__init__(road, bike, rock, finish)
        self.pre_event = ''

    def define_event(self):
        max_jump = self.road.x + 200
        if self.bike.y <= max_jump and not self.pre_event:
            return 'start'
        elif self.bike.is_in_sky() and self.pre_event:
            return 'landing'
        else:
            print(self.bike.is_in_sky(), self.pre_event)

    def start(self, acceleration):
        max_jump = self.road.x + 200
        if self.bike.y <= max_jump and not self.pre_event:
            self.bike.y += acceleration * 80
            return True
        self.pre_event = 'start'

    def landing(self, acceleration):
        is_in_sky = self.bike.is_in_sky()
        if self.bike.is_in_sky() and self.pre_event:
            self.bike.y -= acceleration * 80
        else:
            self.bike.y = self.road.height
        return is_in_sky and self.pre_event
