from objects.puddle.puddle import Puddle


class BasePuddleLevel:

    def puddles(self):
        return self.road.puddles   # Puddle.widgets_on_road(self.road)

    def create_puddle(self, pos):
        for ro in self.road.rocks[:]:
            if ro.pos[0] == pos[0]:
                return False

        pos_y = self.road.line_points[-1] if pos[1] <= 0 else pos[1]
        return Puddle.create(pos=(pos[0], pos_y))

    def add_puddle(self, widget):
        if widget:
            for ro in self.road.puddles[:]:
                if ro.pos[0] == widget.pos[0]:
                    return False

            if self.bike:
                self.road.puddles.append(widget)
                self.road.add_widget(widget)

    def add_puddles(self):
        res_map_puddles = self.map_objects('puddle')[:]
        if self.bike and len(self.road.rocks) <= len(res_map_puddles):
            for mo in res_map_puddles:
                widget = self.create_puddle(mo['pos'])
                self.add_puddle(widget)

    def remove_puddles(self):
        self.remove_widgets(self.road.puddles)
