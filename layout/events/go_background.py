from kivy.clock import Clock

from conf import SECOND_GAME
from road.events.base import BaseDispatcher
from road.events.go import GoDispatcher
from utils.get_object import GetObject
from utils.state import State
from utils.texture import redraw_texture, repeat_texture
from utils.validation import ValidObject


class GoBackgroundDispatcher(BaseDispatcher):
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
            road = None
            for el in self.parent.children[:]:
                if el.__class__.__name__ == 'Road':
                    road = el
                    break
            self.road = ValidObject.road(road)

        if self.bike is None:
            self.bike = GetObject(road=self.road).bike

        if self.road.has_finished() or (
                self.road.state in (State.ON_RELAX_STOP, State.ON_WAIT_MOVE, State.ON_WAIT_STOP)
        ) or self.bike.get_collision_rock():
            self.go_mountains_stop()
            return False

        else:
            if self.is_repeat_texture:
                print('+ GoBackgroundMockDispatcher:on_go_mountains')
                uvpos_x = self.texture.uvpos[0] + (self.bike.speed * dt)/100.0
                self.texture.uvpos = uvpos_x, self.texture.uvpos[1]

                repeat_texture(self.texture)
                redraw_texture(self, 'texture')
                return True
            return False

    def go_mountains_start(self):
        if self.is_repeat_texture and self.road.state in GoBackgroundDispatcher.start_states_list():
            Clock.schedule_interval(self.on_go_mountains, SECOND_GAME)

    def go_mountains_stop(self):
        print('GoBackgroundMockDispatcher:go_mountains_stop')
        if self.road and self.road.state in GoBackgroundDispatcher.stop_states_list():
            # Clock.unschedule(self.on_go_mountains)
            if hasattr(self.on_go_mountains, 'cancel'):
                self.on_go_mountains.cancel()
