from label.status_bar import StatusBar
from utils.validation import ValidObject


class GetObject:
    def __init__(self, road):
        self._road = road

    @property
    def road(self):
        try:
            road = self._road if self._road else StatusBar.get_road()
            return ValidObject.road(road)
        except AttributeError:
            return None

    @property
    def bike(self):
        if hasattr(self.road, 'bike') and self.road.bike:
            return self.road.bike
        elif hasattr(self.road, 'parent') and self.road.parent and len(self.road.parent.children) > 0:
            for o in self.road.parent.children[:]:
                if o.__class__.__name__ == 'Bike':
                    return ValidObject.bike(o)

    @property
    def tools(self):
        try:
            tools = self.road.parent and self.road.parent.parent.parent.children[0]
            return ValidObject.tools(tools)
        except AttributeError:
            return None

    @property
    def background(self):
        try:
            return self.road.parent and ValidObject.background(self.road.parent.children[2])
        except AttributeError:
            return None
