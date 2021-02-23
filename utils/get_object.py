from kivy.app import App
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
            return ValidObject.bike(self.get_child(self.road.parent, 'Bike'))

    @property
    def screen(self):
        if hasattr(self.road, 'parent') and self.road.parent.parent:
            return ValidObject.screen(self.road.parent.parent)

    @property
    def scene(self):
        if hasattr(self.road, 'parent') and self.road.parent:
            return ValidObject.scene(self.road.parent)

    @property
    def tools(self):
        try:
            tools = self.road.parent and GetObject.get_child(self.road.parent.parent.parent, 'Tools')
            return ValidObject.tools(tools)
        except AttributeError:
            return None

    @property
    def background(self):
        if self.road.parent:
            return ValidObject.background(self.get_child(self.road.parent, 'Background'))

    @property
    def curtain(self):
        if hasattr(self.road, 'parent') and self.road.parent:
            return GetObject(self.road).scene.parent.ids['curtain']

    @staticmethod
    def get_child(parent, class_name):
        for w in parent.children[:]:
            if w.__class__.__name__ == class_name:
                return w


def app_config(section, key):
    app = App.get_running_app()
    return app and app.config.get(section, key)
