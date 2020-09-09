from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from label.status_bar import StatusBar
from layout.tools import Tools
from layout.scene import Scene


class RideMeGame(BoxLayout):
    status_bar = ObjectProperty(None)
    scene = ObjectProperty(None)
    tool = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(RideMeGame, self).__init__(**kwargs)

        self.status_bar = StatusBar()
        self.scene = Scene(status_bar=self.status_bar)
        self.tool = Tools(status_bar=self.status_bar)

        self.scene.add_widget(self.status_bar)
        self.add_widget(self.scene)
        self.add_widget(self.tool)
