from kivy.lang import Builder
from kivy.properties import StringProperty
from road.base.game_image import GameImage
from utils.validation import ValidObject
from utils.dir import abstract_path

Builder.load_file(abstract_path('road/rock/rock.kv'))


class Rock(GameImage):
    source = StringProperty(abstract_path('road/rock/img/rock-1.png'))

    @staticmethod
    def create(pos, size=None):
        kwargs = {
            "pos": pos,
            # "size": self.texture_size
        }
        return Rock(**kwargs)

    @staticmethod
    def widgets_on_road(road):
        rocks = [ValidObject.rock(w) for w in road.children if w.__class__.__name__ == 'Rock']
        return rocks
