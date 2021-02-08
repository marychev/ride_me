from kivy.uix.image import Image
from kivy.properties import ObjectProperty
from objects.base.game_image import GameImage
from utils.dir import abstract_path
from utils.validation import ValidObject


class Lamp(GameImage):
    img = Image(source=abstract_path('objects/lamp/img/lamp.png'))
    TEXTURE = img.texture
    texture = ObjectProperty(TEXTURE)
