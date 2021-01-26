class BaseLevel:

    def __init__(self, road, bike, map_json, **kwargs):
        super().__init__(**kwargs)
        self.road = road
        self.bike = bike
        self.map = map_json

        print('BASE LEVEL::INIT', self)

    def exist_to_map(self, name):
        return name.title() in list(set(el.get('name') for el in self.map))

    def map_objects(self, name):
        return [m for m in self.map if m['name'] == name.title() and int(self.road.distance_traveled) <= int(m['pos'][0])]

    def visible_map_elem(self):
        return [me for me in self.road.level.map if self.road.visible(me['pos'])]

    def can_remove_widget(self, widget):
        return widget.pos[0] < 0

    def _remove_widget(self, widget):
        self.can_remove_widget(widget) and self.road.remove_widget(widget)

    def remove_widgets(self, road_objects):
        if len(road_objects) > 0 and self.road.distance_traveled > 0:
            [self._remove_widget(w) for w in road_objects]
