from kivy.clock import Clock

from conf import SECOND_GAME
from road.events.base import BaseDispatcher
from utils.state import State


class GoDispatcher(BaseDispatcher):

    def __init__(self, **kwargs):
        super(GoDispatcher, self).__init__(**kwargs)
        self.register_event_type(State.EVENT_ON_GO)

    @classmethod
    def start_states_list(cls):
        return (State.ON_LANDING_STOP,
                State.ON_WAIT_MOVE, State.ON_WAIT_STOP,
                State.ON_RELAX_START, State.ON_RELAX_MOVE, State.ON_RELAX_STOP,
                State.ON_STOP_MOVE)

    @classmethod
    def stop_states_list(cls):
        return State.ON_GO_START, State.ON_GO_MOVE, State.ON_GO_STOP

    def go_start(self):
        if self.road.state in GoDispatcher.start_states_list():
            Clock.schedule_interval(self.on_go, SECOND_GAME)
            self.road.set_state(State.ON_GO_START)
            self.bike.anim_go()

    def go_stop(self):
        if self.road.state in GoDispatcher.stop_states_list():
            Clock.unschedule(self.on_go)
            self.road.set_state(State.ON_GO_STOP)
            self.status_bar and self.status_bar.show_status('Stop On GO: ' + self.road.state, self.bike, self.road)

    def on_go(self, dt):
        if self.rock and self.bike.collide_widget(self.rock):
            self.bike.collision_rock()
            self.go_stop()
            self.status_bar and self.status_bar.show_status('Stop On GO/COLLISION: ' + self.road.state, self.bike, self.road)
            return False

        elif self.road.has_finished():
            self.go_stop()
            self.road_finish()
            return False

        elif self.bike.is_in_sky():
            return False

        else:
            self.bike.speed += dt
            self.bike.power -= dt*5

            self.set_distances()
            self.road.set_state(State.ON_GO_MOVE)
            self.status_bar and self.status_bar.show_status('On GO: ' + self.road.state, self.bike, self.road)
            return True

