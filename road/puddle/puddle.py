from kivy.lang import Builder
from kivy.properties import StringProperty
from road.base.game_image import GameImage
from utils.dir import abstract_path
from utils.validation import ValidObject

Builder.load_file(abstract_path('road/puddle/puddle.kv'))


class Puddle(GameImage):
    source = StringProperty(abstract_path('road/puddle/img/puddle.png'))

    @staticmethod
    def create(pos):
        puddle = Puddle(pos=pos)
        puddle.size = puddle.texture_size
        return puddle

    @staticmethod
    def widgets_on_road(road):
        widgets = [ValidObject.puddle(w) for w in road.children if w.__class__.__name__ == 'Puddle']
        return widgets
