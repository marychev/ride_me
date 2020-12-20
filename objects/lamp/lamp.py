from kivy.lang import Builder
from kivy.properties import StringProperty
from objects.base.game_image import GameImage
from utils.dir import abstract_path
from utils.validation import ValidObject

_dir = 'objects/lamp'
Builder.load_file(abstract_path('{}/lamp.kv'.format(_dir)))


class Lamp(GameImage):
    source = StringProperty(abstract_path('{}/img/lamp.png'.format(_dir)))

    @staticmethod
    def create(pos):
        lamp = Lamp(pos=pos)
        lamp.size = lamp.texture_size
        return lamp

    @staticmethod
    def widgets_on_road(road):
        return [ValidObject.lamp(w) for w in road.children if w.__class__.__name__ == 'Lamp']
