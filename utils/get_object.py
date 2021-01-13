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
        try:
            bike = self.road.bike if self.road.bike else StatusBar.get_bike()
            return ValidObject.bike(bike)
        except AttributeError:
            return None

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
