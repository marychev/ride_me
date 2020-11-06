from kivy.clock import Clock

from conf import SECOND_GAME
from road.events.base import BaseDispatcher
from utils.state import State


class StopDispatcher(BaseDispatcher):

    def __init__(self, **kwargs):
        super(StopDispatcher, self).__init__(**kwargs)
        self.register_event_type(State.EVENT_ON_STOP)

    @classmethod
    def start_states_list(cls):
        return (State.ON_RELAX_MOVE, State.ON_RELAX_STOP,
                State.ON_GO_MOVE)

    @classmethod
    def stop_states_list(cls):
        return State.ON_STOP_START, State.ON_STOP_MOVE, State.ON_STOP_STOP

    def stop_start(self):
        if self.road.state in StopDispatcher.start_states_list():
            Clock.schedule_interval(self.on_stop, SECOND_GAME)
            self.road.set_state(State.ON_STOP_START)
            self.bike.anim_stop()

    def stop_stop(self):
        if self.road.state in StopDispatcher.stop_states_list():
            Clock.unschedule(self.on_stop)
            self.road.wait_start()

    def on_stop(self, dt):
        stop_way = dt * 2

        if self.rock and self.bike.collide_widget(self.rock):
            self.bike.collision_rock()
            self.road.set_state(State.ON_STOP_STOP)
            self.status_bar and self.status_bar.show_status('Stop On Stop: COLLISION' + self.road.state, self.bike, self.road)
            return False

        elif float(self.bike.speed) - float(stop_way) <= 0.0:
            self.bike.speed = 0
            self.rock and self.rock.set_x()
            self.finish and self.finish.set_x()
            self.road.set_state(State.ON_STOP_STOP)
            self.status_bar and self.status_bar.show_status('Stop On Stop' + self.road.state, self.bike, self.road)
            return False

        else:
            self.bike.speed -= stop_way
            self.set_distances()

            self.road.set_state(State.ON_STOP_MOVE)
            self.status_bar and self.status_bar.show_status('On Stop: ' + self.road.state, self.bike, self.road)
            return True
