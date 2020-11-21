from kivy.lang import Builder
from road.start.start import Start
from utils.dir import abstract_path
from utils.texture import redraw_texture
from utils.validation import ValidObject

Builder.load_file(abstract_path('road/finish/finish.kv'))


class Finish(Start):
    @staticmethod
    def create(pos, size):
        kwargs = {
            "pos": pos,
            "size": size,
            "size_hint": (None, None)}
        return Finish(**kwargs)

    @staticmethod
    def widgets_on_road(road):
        widgets = [ValidObject.finish(w) for w in road.children if w.__class__.__name__ == 'Finish']
        return widgets

    def set_x(self):
        self.x = self.get_x()
        redraw_texture(self)

    def get_x(self):
        bike = self.get_bike()
        road = self.get_road()
        return (road.total_way - road.distance_traveled) + bike.x + bike.width
