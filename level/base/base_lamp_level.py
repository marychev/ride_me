from objects.lamp.lamp import Lamp


class BaseLampLevel:

    def lamps(self):
        return Lamp.widgets_on_road(self.road)

    def create_lamp(self, pos):
        pos_y = self.road.line_points[-1] if pos[1] <= 0 else pos[1]
        return Lamp.create(pos=(pos[0], pos_y))

    def create_lamps(self):
        return [self.create_lamp(obj['pos']) for obj in self.init_objects('lamp')]

    def add_lamp(self, lamp):
        if self.bike and self.road:
            self.road.add_widget(lamp)

    def add_lamps(self):
        if len(self.lamps()) == 0:
            [self.add_lamp(lamp) for lamp in self.create_lamps()]

    def remove_lamps(self):
        lamps = self.lamps()
        if len(lamps) > 0:
            [self.road.remove_widget(w) for w in lamps if w.pos[0] < 0]
