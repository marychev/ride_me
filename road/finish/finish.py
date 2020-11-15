from kivy.lang import Builder
from road.start.start import Start
from utils.dir import abstract_path
from utils.texture import redraw_texture

Builder.load_file(abstract_path('road/finish/finish.kv'))


class Finish(Start):

    def set_x(self):
        self.x = self.get_x()
        redraw_texture(self)

    def get_x(self):
        bike = self.get_bike()
        road = self.get_road()
        return (road.total_way - road.distance_traveled) + bike.x + bike.width
