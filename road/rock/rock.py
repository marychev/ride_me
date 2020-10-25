from kivy.uix.image import Image
from kivy.lang import Builder

Builder.load_file("road/rock/rock.kv")


class Rock(Image):
    def set_x(self):
        print('x-rock')
        self.x = self.get_x()

    def get_x(self):
        print('todo-1', self.texture_size, self.size)
        bike = self.parent.parent.children[0]
        road = self.parent.parent.children[1]

        distance_traveled = self.x - bike.speed

        bike.collision_rock()

        if (road.__class__.__name__ == 'Road') and (bike.__class__.__name__ == 'Bike'):
            return distance_traveled
