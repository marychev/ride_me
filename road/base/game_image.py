from kivy.uix.image import Image
from label.status_bar import StatusBar
from utils.texture import redraw_texture
from utils.validation import ValidObject


class GameImage(Image):

    def set_x(self):
        self.x = self.get_x()
        redraw_texture(self)

    def get_x(self):
        bike = self.get_bike()
        return self.x - bike.speed if bike else self.x

    # general elements and functions

    def get_bike(self):
        if self.parent:
            return self.parent.get_bike()
        else:
            return StatusBar.get_bike()

    def get_tools(self):
        return ValidObject.tools(self.parent.parent.parent.children[0])
