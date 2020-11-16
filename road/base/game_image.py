from kivy.uix.image import Image
from utils.texture import redraw_texture
from utils.validation import ValidObject


class GameImage(Image):

    def set_x(self):
        self.x = self.get_x()
        redraw_texture(self)

    def get_x(self):
        return self.x - self.get_bike().speed

    # general elements and functions

    def get_bike(self):
        return ValidObject.bike(self.parent.parent.children[0])

    def get_tools(self):
        return ValidObject.tools(self.parent.parent.parent.children[0])
