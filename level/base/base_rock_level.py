from objects import Rock


class BaseRockLevel:
    def rocks(self):
        return self.road.rocks # or Rock.widgets_on_road(self.road)

    def create_rock(self, pos):
        # if len(self.rocks()) < len(self.init_objects('rock')):
        #     pos_y = self.road.line_points[-1] if pos[1] <= 0 else pos[1]
        #     return Rock.create(pos=(pos[0], pos_y))
        for ro in self.road.rocks[:]:
            if ro.pos[0] == pos[0]:
                return False

        pos_y = self.road.line_points[-1] if pos[1] <= 0 else pos[1]
        return Rock.create(pos=(pos[0], pos_y))

    def add_rock(self, widget):
        # if (self.bike and self.road) and (len(self.rocks()) < len(self.init_objects('rock'))):
        #     self.road.add_widget(widget)
        if widget:
            for ro in self.road.rocks[:]:
                if ro.pos[0] == widget.pos[0]:
                    return False

            if self.bike:
                self.road.rocks.append(widget)
                self.road.add_widget(widget)

    def add_rocks(self):
        # road_objects = self.rocks() and self.rocks()[:]
        # map_objects = self.init_objects('rock') and self.init_objects('rock')[:]
        # new_map_objects = self.new_map_objects(road_objects=road_objects, map_objects=map_objects)
        #
        # if (self.bike and self.road) and (road_objects and len(road_objects) < len(map_objects)):
        #     create_rocks = [self.create_rock(obj['pos']) for obj in new_map_objects]
        #     [self.add_rock(w) for w in create_rocks]
        # zone = VisibleZone.current_visible_zone(self.road)
        res_map_rocks = self.map_objects('rock')[:]

        if self.bike and len(self.road.rocks) <= len(res_map_rocks):
            for mo in res_map_rocks:
                # if zone.collide_point_widget(mo):
                widget = self.create_rock(mo['pos'])
                self.add_rock(widget)

    def remove_rock(self):
        self.remove_widgets(self.road.rocks)
