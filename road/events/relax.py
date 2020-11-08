from kivy.clock import Clock

from conf import SECOND_GAME
from road.events.base import BaseDispatcher
from utils.state import State


class RelaxDispatcher(BaseDispatcher):

    def __init__(self, **kwargs):
        super(RelaxDispatcher, self).__init__(**kwargs)
        self.register_event_type(State.EVENT_ON_RELAX)

    @classmethod
    def start_states_list(cls):
        return (State.ON_LANDING_STOP,
                State.ON_GO_STOP,
                State.ON_WAIT_MOVE, State.ON_WAIT_STOP)

    @classmethod
    def stop_states_list(cls):
        return (State.ON_RELAX_START, State.ON_RELAX_MOVE, State.ON_RELAX_STOP,
                State.ON_LANDING_STOP)

    def relax_start(self):
        if self.road.state in RelaxDispatcher.start_states_list():
            Clock.schedule_interval(self.on_relax, SECOND_GAME)
            self.road.set_state(State.ON_RELAX_START)
            self.bike.anim_relax()

    def relax_stop(self):
        if self.road.state in RelaxDispatcher.stop_states_list():
            Clock.unschedule(self.on_relax)
            self.road.set_state(State.ON_RELAX_STOP)
            self.status_bar and self.status_bar.show_status('Stop On Relax: ' + self.road.state, self.bike, self.road)

            if self.bike.speed <= 0:
                self.road.wait_start()

            self.bike.anim_wait()

    def on_relax(self, dt):
        if self.rock and self.bike.collide_widget(self.rock):
            self.bike.collision_rock()
            self.relax_stop()
            self.status_bar and self.status_bar.show_status('Stop On Relax: ' + self.road.state, self.bike, self.road)
            return False

        elif self.road.has_finished():
            self.road_finish()
            self.relax_stop()
            return False

        elif self.bike.speed - dt <= 0:
            self.bike.speed = 0
            self.rock and self.rock.set_x()
            self.finish and self.finish.set_x()

            self.relax_stop()
            return False

        else:
            self.bike.speed -= dt/2

            # self.bike.set_power(dt)
            if self.bike.power + dt < self.bike.max_power:
                self.bike.power += dt
            else:
                self.bike.power = self.bike.max_power

            self.set_distances()

            self.road.set_state(State.ON_RELAX_MOVE)
            self.status_bar and self.status_bar.show_status('On Relax: ' + self.road.state, self.bike, self.road)
            return True
