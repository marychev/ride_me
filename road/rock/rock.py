from kivy.uix.image import Image
from kivy.lang import Builder

Builder.load_file("road/rock/rock.kv")


class Rock(Image):
    def get_distance_traveled(self):
        bike = self.parent.parent.children[0]
        return self.x - bike.speed

    def set_x(self):
        print('x-rock')
        self.x = self.get_x()

    def get_x(self):
        print('todo-1', self.texture_size, self.size)
        bike = self.parent.parent.children[0]
        road = self.parent.parent.children[1]

        if (road.__class__.__name__ == 'Road') and (bike.__class__.__name__ == 'Bike'):
            return self.get_distance_traveled()
