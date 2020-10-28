from kivy.uix.image import Image
from kivy.lang import Builder

Builder.load_file("road/rock/rock.kv")


class Rock(Image):
    def get_distance_traveled(self):
        return self.x - self.get_bike().speed

    def set_x(self):
        self.x = self.get_x()
        self.redraw_texture()

    def get_x(self):
        return self.get_distance_traveled()

    # general elements and functions

    def redraw_texture(self, name='texture'):
        texture = self.property(name)
        texture.dispatch(self)

    def get_bike(self):
        bike = self.parent.parent.children[0]
        if bike.__class__.__name__ == 'Bike':
            return bike
