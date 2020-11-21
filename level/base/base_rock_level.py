from road.rock import Rock


class BaseRockLevel:

    def rocks(self):
        return Rock.widgets_on_road(self.road)

    def create_rocks(self):
        return [Rock.create(pos=(o['pos'][0], self.road.line_points[-1])) for o in self.init_objects('rock')]

    def add_rock(self):
        if len(Rock.widgets_on_road(self.road)) == 0 and (self.bike and self.road):
            [self.road.add_widget(rock) for rock in self.create_rocks()]

    def remove_rock(self):
        rocks = Rock.widgets_on_road(self.road)
        if len(rocks) > 0:
            [self.road.remove_widget(w) for w in rocks if w.pos[0] < 0]
