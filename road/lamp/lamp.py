from kivy.lang import Builder
from kivy.properties import StringProperty
from road.base.game_image import GameImage
from utils.dir import abstract_path
from utils.validation import ValidObject

Builder.load_file(abstract_path('road/lamp/lamp.kv'))


class Lamp(GameImage):
    source = StringProperty(abstract_path('road/lamp/img/lamp.png'))

    @staticmethod
    def create(pos):
        lamp = Lamp(pos=pos)
        lamp.size = lamp.texture_size
        return lamp

    @staticmethod
    def widgets_on_road(road):
        return [ValidObject.lamp(w) for w in road.children if w.__class__.__name__ == 'Lamp']
