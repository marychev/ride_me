from kivy.lang import Builder
from objects.start.start import Start
from utils.dir import abstract_path
from utils.texture import redraw_texture
from utils.validation import ValidObject

Builder.load_file(abstract_path('objects/finish/finish.kv'))


class Finish(Start):
    @staticmethod
    def widgets_on_road(road):
        return [ValidObject.finish(w) for w in road.children if w.__class__.__name__ == 'Finish']

    def get_x(self):
        bike = self.get_bike()
        road = self.get_road()
        return (road.total_way - road.distance_traveled) + bike.x + bike.width
