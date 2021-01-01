from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.properties import ObjectProperty
from objects.base.game_image import GameImage
from utils.dir import abstract_path
from utils.validation import ValidObject


_dir = 'objects/lamp'
Builder.load_file(abstract_path('{}/lamp.kv'.format(_dir)))


class Lamp(GameImage):
    IMG = Image(source=abstract_path('{}/img/lamp.png'.format(_dir)))
    TEXTURE = IMG.texture
    texture = ObjectProperty(TEXTURE)

    @classmethod
    def widgets_on_road(cls, road):
        return [ValidObject.lamp(w) for w in road.children if w.__class__.__name__ == cls.__name__]