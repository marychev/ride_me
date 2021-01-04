from kivy.uix.image import Image
from kivy.properties import ObjectProperty
from objects.base.game_image import GameImage
from utils.dir import abstract_path
from utils.validation import ValidObject


class Lamp(GameImage):
    TEXTURE = Image(source=abstract_path('objects/lamp/img/lamp.png')).texture
    texture = ObjectProperty(TEXTURE)

    @classmethod
    def widgets_on_road(cls, road):
        return [ValidObject.lamp(w) for w in road.children if w.__class__.__name__ == cls.__name__]
