from kivy.clock import Clock
from kivy.properties import ObjectProperty, BooleanProperty
from conf import SECOND_GAME
from road.events.base import BaseDispatcher
from road.events.go import GoDispatcher
from utils.validation import ValidObject
from utils.state import State
from utils.texture import redraw_texture, repeat_texture
from utils.get_object import GetObject


class GoBackgroundDispatcher(BaseDispatcher):
    mountains_texture = ObjectProperty(None)
    cloud_big_texture = ObjectProperty(None)
    cloud_middle_texture = ObjectProperty(None)
    cloud_min_texture = ObjectProperty(None)
    is_repeat_texture = BooleanProperty(False)

    @classmethod
    def start_states_list(cls):
        return (
            State.ON_GO_START, State.ON_GO_MOVE,
            State.ON_RELAX_START, State.ON_RELAX_MOVE, State.ON_RELAX_STOP,
        )

    @classmethod
    def stop_states_list(cls):
        return GoDispatcher.stop_states_list()

    def on_go_mountains(self, dt):
        # print('GoBackgroundMockDispatcher:on_go_mountains => ', self.road and self.road.state)

        if self.road is None and self.parent.__class__.__name__ == 'Scene' and len(self.parent.children) > 0:
            self.road = ValidObject.road(self.parent.children[1])
        if self.bike is None:
            self.bike = GetObject(road=self.road).bike

        if self.road.has_finished():
            self.go_mountains_stop()
            return False

        elif self.road.state in (State.ON_RELAX_STOP, State.ON_WAIT_MOVE, State.ON_WAIT_STOP):
            self.go_mountains_stop()
            return False

        elif self.bike.get_collision_rock():
            self.go_mountains_stop()
            return False

        else:
            if self.is_repeat_texture:
                # print('+ GoBackgroundMockDispatcher:on_go_mountains')
                uvpos_x = self.mountains_texture.uvpos[0] + (self.bike.speed * dt)/100.0
                self.mountains_texture.uvpos = uvpos_x, self.mountains_texture.uvpos[1]
                repeat_texture(self.mountains_texture)
                redraw_texture(self, 'mountains_texture')

            return True

    def go_mountains_start(self):
        if self.is_repeat_texture and self.road.state in GoBackgroundDispatcher.start_states_list():
            Clock.schedule_interval(self.on_go_mountains, SECOND_GAME)

    def go_mountains_stop(self):
        # print('GoBackgroundMockDispatcher:go_mountains_stop')
        if self.road and self.road.state in GoBackgroundDispatcher.stop_states_list():
            Clock.unschedule(self.on_go_mountains)
