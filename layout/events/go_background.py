from kivy.clock import Clock
from kivy.properties import ObjectProperty, BooleanProperty
from conf import SECOND_GAME
from road.events.base import BaseDispatcher
from road.events.go import GoDispatcher
from utils.state import State
from utils.texture import redraw_texture, repeat_texture


class GoBackgroundMockDispatcher(BaseDispatcher):
    mountains_texture = ObjectProperty(None)
    cloud_big_texture = ObjectProperty(None)
    cloud_middle_texture = ObjectProperty(None)
    cloud_min_texture = ObjectProperty(None)
    is_repeat_texture = BooleanProperty(False)

    @classmethod
    def start_states_list(cls):
        return GoDispatcher.start_states_list() + (State.ON_GO_START, )

    @classmethod
    def stop_states_list(cls):
        return GoDispatcher.stop_states_list()

    def on_go_mountains(self, dt):
        print('GoBackgroundMockDispatcher:on_go_mountains')
        self.road or self.set_game_object()
        if self.road.has_finished():
            return False

        elif self.road.state == State.ON_RELAX_STOP:
            return False

        elif self.bike.get_collision_rock():
            return False

        else:
            if self.is_repeat_texture:
                uvpos_x = self.mountains_texture.uvpos[0] + (self.bike.speed * dt)/100.0
                self.mountains_texture.uvpos = uvpos_x, self.mountains_texture.uvpos[1]
                repeat_texture(self.mountains_texture)
                redraw_texture(self, 'mountains_texture')

            return True

    def go_mountains_start(self):
        print('GoBackgroundMockDispatcher:go_mountains_start')
        self.set_game_object()
        if self.road.state in GoBackgroundMockDispatcher.start_states_list():
            Clock.schedule_interval(self.on_go_mountains, SECOND_GAME)

    def go_mountains_stop(self):
        print('GoBackgroundMockDispatcher:go_mountains_stop')
        if self.road.state in GoBackgroundMockDispatcher.stop_states_list():
            Clock.unschedule(self.on_go_mountains)

    def get_rocks(self):
        return self.get_road().rocks

    def get_puddles(self):
        return self.get_road().puddles

    def get_lamps(self):
        return self.get_road().lamps
