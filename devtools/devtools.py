from kivy.uix.widget import Widget
from utils.dir import abstract_path
from kivy.lang import Builder
from kivy.properties import ObjectProperty

Builder.load_file(abstract_path('devtools/devtools.kv'))


class DevTools(Widget):
    scene = ObjectProperty(None)
    road = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(DevTools, self).__init__(**kwargs)
        print('!!!', self.scene)

