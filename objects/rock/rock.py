from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.properties import ObjectProperty
from objects.base.game_image import GameImage
from utils.validation import ValidObject
from utils.dir import abstract_path

_dir = 'objects/rock'
Builder.load_file(abstract_path('{}/rock.kv'.format(_dir)))


class Rock(GameImage):
    IMG = Image(source=abstract_path('{}/img/rock-1.png'.format(_dir)))
    TEXTURE = IMG.texture
    texture = ObjectProperty(TEXTURE)

    @staticmethod
    def widgets_on_road(road):
        return [ValidObject.rock(w) for w in road.children if w.__class__.__name__ == 'Rock']
