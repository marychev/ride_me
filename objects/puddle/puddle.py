from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from objects.base.game_image import GameImage
from utils.dir import abstract_path
from utils.validation import ValidObject


class Puddle(GameImage):
    img = Image(source=abstract_path('objects/puddle/img/puddle.png'))
    TEXTURE = img.texture
    texture = ObjectProperty(TEXTURE)

    @staticmethod
    def widgets_on_road(road):
        return [ValidObject.puddle(w) for w in road.children if w.__class__.__name__ == 'Puddle']
