from kivy.uix.widget import Widget
from utils.dir import abstract_path
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from utils.color import Color
from utils.validation import ValidObject

Builder.load_file(abstract_path('devtools/devtools.kv'))


class DevTools(Widget):
    scene = ObjectProperty(None)
    road = ObjectProperty(None)

    def format_map_elem(self, elem, newline=False):
        name, pos = elem['name'], elem['pos']

        color = Color.RED
        if self.road.passed(pos):
            color = Color.RED_LIGHT
        elif self.road.visible(pos):
            color = Color.GREEN
        elif self.road.future(pos):
            color = Color.ORANGE

        res = '[color={}]{}[/color]:[size=9]{}[/size]'.format(color, name, str(pos).replace('(', '').replace(')', ''))
        return '\n' + res if newline else res

    def map_text(self):
        if not self.road:
            self.road = ValidObject.road(self.scene.children[1])

        res = [
            self.format_map_elem(e, not bool(i))
            for i, e in enumerate(self.road.level.map)]
        return ', '.join([e for e in res])

    def update_context(self):
        road = self.road
        line_map = self.ids['line_map']
        line_map.text = self.map_text()

        btn_add = self.ids['btn_add_map_elements']
        btn_add.text = f'Add to Map: {len(road.level.visible_map_elem())}'

        slider_map = self.ids['slider_map']
        slider_map.value = road.distance_traveled
        slider_map_label = self.ids['slider_map_label']
        slider_map_label.text = f'{int(slider_map.value)} => {int(road.total_way)}'

    # todo:  slider_map
    def slider_map_max(self):
        if not self.road and self.parent:
            screen = ValidObject.screen(self.parent.parent.parent)
            self.road = ValidObject.road(screen.ids['road'])

        return self.road.total_way

