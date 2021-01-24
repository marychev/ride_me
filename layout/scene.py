from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from utils.dir import abstract_path

Builder.load_file(abstract_path('layout/scene.kv'))


class Scene(FloatLayout):

    def update_map_text(self):
        devtools = self.parent.ids['devtools']
        line_map = devtools.ids['line_map']
        line_map.text = devtools.map_text()
        return line_map.text
