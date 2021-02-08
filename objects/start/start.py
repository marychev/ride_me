from objects.base.game_image import GameImage
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from utils.validation import ValidObject
from utils.dir import abstract_path
from utils.texture import redraw_texture, repeat_texture


class Start(GameImage):
    img = Image(source=abstract_path('objects/finish/img/finish.jpg'))
    TEXTURE = img.texture
    texture = ObjectProperty(TEXTURE)

    def __init__(self, **kwargs):
        super(Start, self).__init__(**kwargs)
        repeat_texture(self.texture, 8, 8)
