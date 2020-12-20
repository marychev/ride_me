from objects.puddle.puddle import Puddle


class BasePuddleLevel:

    def puddles(self):
        return Puddle.widgets_on_road(self.road)

    def create_puddles(self):
        return [Puddle.create(pos=(o['pos'][0], self.road.line_points[-1])) for o in self.init_objects('puddle')]

    def add_puddle(self):
        if len(Puddle.widgets_on_road(self.road)) == 0 and (self.bike and self.road):
            [self.road.add_widget(rock) for rock in self.create_puddles()]

    def remove_puddles(self):
        puddles = Puddle.widgets_on_road(self.road)
        if len(puddles) > 0:
            [self.road.remove_widget(w) for w in puddles if w.pos[0] < 0]
