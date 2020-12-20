from kivy.lang import Builder
from kivy.properties import StringProperty
from objects.base.game_image import GameImage
from utils.validation import ValidObject
from utils.dir import abstract_path

_dir = 'objects/rock'
Builder.load_file(abstract_path('{}/rock.kv'.format(_dir)))


class Rock(GameImage):
    source = StringProperty(abstract_path('{}/img/rock-1.png'.format(_dir)))

    @staticmethod
    def create(pos):
        rock = Rock(pos=pos)
        rock.size = rock.texture_size
        return rock

    @staticmethod
    def widgets_on_road(road):
        rocks = [ValidObject.rock(w) for w in road.children if w.__class__.__name__ == 'Rock']
        return rocks
