from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from objects.base.game_image import GameImage
from utils.dir import abstract_path
from utils.validation import ValidObject

_dir = 'objects/puddle'
Builder.load_file(abstract_path('{}/puddle.kv'.format(_dir)))


class Puddle(GameImage):
    IMG = Image(source=abstract_path('{}/img/puddle.png'.format(_dir)))
    TEXTURE = IMG.texture
    texture = ObjectProperty(TEXTURE)

    @staticmethod
    def widgets_on_road(road):
        return [ValidObject.puddle(w) for w in road.children if w.__class__.__name__ == 'Puddle']
