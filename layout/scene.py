from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from utils.color import Color
from utils.dir import abstract_path

Builder.load_file(abstract_path('layout/scene.kv'))


class Scene(FloatLayout):

    def format_map_elem(self, elem, newline=False):
        name, pos = elem['name'], elem['pos']
        road = self.parent.ids['road']

        color = Color.RED
        if road.passed(pos):
            color = Color.RED_LIGHT
        elif road.visible(pos):
            color = Color.GREEN
        elif road.future(pos):
            color = Color.ORANGE

        res = '[color={}]{}[/color]:[size=9]{}[/size]'.format(color, name, str(pos).replace('(', '').replace(')', ''))
        return '\n' + res if newline else res

    def map_text(self):
        res = [
            self.format_map_elem(e, not bool(i))
            for i, e in enumerate(self.parent.ids['road'].level.map)]
        return ', '.join([e for e in res])

    def update_map_text(self):
        line_map = self.parent.ids['line_map']
        line_map.text = self.map_text()
        return line_map.text
