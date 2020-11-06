from kivy.clock import Clock

from conf import SECOND_GAME
from road.events.base import BaseDispatcher
from utils.state import State


class GoDispatcher(BaseDispatcher):

    def __init__(self, **kwargs):
        super(GoDispatcher, self).__init__(**kwargs)
        self.register_event_type(State.EVENT_ON_GO)

    def go_start(self):
        if self.road.state in (State.ON_WAIT_MOVE, State.ON_WAIT_STOP,
                               State.ON_RELAX_MOVE, State.ON_RELAX_STOP):
            Clock.schedule_interval(self.on_go, SECOND_GAME)
            self.road.set_state(State.ON_GO_START)
            self.bike.anim_go()

    def go_stop(self):
        if self.road.state in (State.ON_GO_START, State.ON_GO_MOVE, State.ON_GO_STOP):
            Clock.unschedule(self.on_go)
            self.road.set_state(State.ON_GO_STOP)
            # option
            self.status_bar and self.status_bar.show_status('Stop On GO: ' + self.road.state, self.bike, self.road)

    def on_go(self, dt):
        if self.rock and self.bike.collide_widget(self.rock):
            self.bike.collision_rock()
            self.go_stop()
            self.status_bar and self.status_bar.show_status('Stop On GO/COLLISION: ' + self.road.state, self.bike, self.road)
            return False
        elif self.road.has_finished():
            self.bike.power = 0
            self.bike.speed = 0
            self.bike.acceleration = 0

            self.road.set_state(State.FINISH)
            self.road.unschedule_events()
            self.status_bar and self.status_bar.show_status_finished()
            return False
        else:
            self.bike.speed += dt
            self.set_distances()
            self.road.set_state(State.ON_GO_MOVE)
            self.status_bar and self.status_bar.show_status('On GO: ' + self.road.state, self.bike, self.road)
            return True
