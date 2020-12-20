from objects.lamp.lamp import Lamp


class BaseLampLevel:

    def lamps(self):
        return Lamp.widgets_on_road(self.road)

    def create_lamps(self):
        pos_y = self.road.line_points[-1]
        return [Lamp.create(
            pos=(o['pos'][0], o['pos'][1] if o['pos'][1] > 0 else pos_y)
        ) for o in self.init_objects('lamp')]

    def add_lamp(self):
        if len(Lamp.widgets_on_road(self.road)) == 0 and (self.bike and self.road):
            [self.road.add_widget(lamp) for lamp in self.create_lamps()]

    def remove_lamps(self):
        lamps = Lamp.widgets_on_road(self.road)
        if len(lamps) > 0:
            [self.road.remove_widget(w) for w in lamps if w.pos[0] < 0]
