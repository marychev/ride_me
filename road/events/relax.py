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
                State.ON_WAIT_MOVE, State.ON_WAIT_STOP,
                State.ON_STOP_STOP)

    @classmethod
    def stop_states_list(cls):
        return (State.ON_RELAX_START, State.ON_RELAX_MOVE, State.ON_RELAX_STOP,
                State.ON_LANDING_STOP)

    def relax_start(self):
        if self.bike.speed > 0 and self.road.state in RelaxDispatcher.start_states_list():
            Clock.schedule_interval(self.on_relax, SECOND_GAME)
            self.road.set_state(State.ON_RELAX_START)
            self.bike.anim_relax()

    def relax_stop(self):
        if self.road.state in RelaxDispatcher.stop_states_list():
            Clock.unschedule(self.on_relax)
            self.road.set_state(State.ON_RELAX_STOP)

            if self.bike.speed <= 0:
                self.road.wait_start()

            self.bike.anim_wait()

    def on_relax(self, dt):
        if self.bike.on_collision_rock():
            self.relax_stop()
            return False

        if self.road.has_finished():
            self.road_finish()
            self.relax_stop()
            return False

        elif self.bike.speed - dt <= 0:
            self.bike.speed = 0

            # self.rock and self.rock.set_x()
            # self.finish and self.finish.set_x()

            self.relax_stop()
            return False

        elif self.road.state in (State.ON_GO_START, State.ON_STOP_START, State.ON_STOP_MOVE):
            return False

        else:
            self.bike.on_collision_puddle()

            self.bike.speed -= dt/1.5

            # self.bike.set_power(dt)
            if self.bike.power + dt < self.bike.max_power:
                self.bike.power += dt*10
            else:
                self.bike.power = self.bike.max_power

            self.set_distances()

            self.road.set_state(State.ON_RELAX_MOVE)
            return True
