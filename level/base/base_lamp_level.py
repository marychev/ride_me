from objects.lamp.lamp import Lamp
from kivy.uix.label import Label


class BaseLampLevel:

    def lamps(self):
        return Lamp.widgets_on_road(self.road)

    def new_map_lamps(self):
        return self.new_map_objects(road_objects=self.lamps(), map_objects=self.init_objects('lamp'))

    def create_lamp(self, pos):
        # if len(self.lamps()) < len(self.init_objects('lamp')):
        pos_y = self.road.line_points[-1] if pos[1] <= 0 else pos[1]
        return Lamp.create(pos=(pos[0], pos_y))

    def add_lamp(self, lamp):
        # print(self.bike, self.road, lamp, len(self.lamps()), len(self.init_objects('lamp')))
        label = Label(pos=lamp.pos, text=str(lamp.pos))
        if self.bike and self.road and lamp:
            print(' + + + ADD + + +', lamp.pos)
            # self.road.add_widget(label)
            self.road.add_widget(lamp)

    def add_lamps(self):
        new_map_objects = self.new_map_objects(road_objects=self.lamps(), map_objects=self.init_objects('lamp'))
        print('>> >> new_map_objects:', new_map_objects)

        if len(new_map_objects) > 0:
            create_lamps = [self.create_lamp(obj['pos']) for obj in new_map_objects]
            [self.add_lamp(lamp) for lamp in create_lamps]

    def remove_lamps(self):
        if self.road.distance_traveled > 0:
            self.remove_widgets(self.lamps())
