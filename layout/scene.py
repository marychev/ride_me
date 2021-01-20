from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from utils.dir import abstract_path
from utils.color import Color

Builder.load_file(abstract_path('layout/scene.kv'))


class Scene(FloatLayout):

    @staticmethod
    def format_map_elem(color, name, pos, newline=False):
        res = '[color={}]{}[/color]:[size=9]{}[/size]'.format(color, name, str(pos).replace('(', '').replace(')', ''))
        return '\n' + res if newline else res

    def map_text(self):
        res = [
            Scene.format_map_elem(Color.RED, e['name'], e['pos'], not bool(i))
            for i, e in enumerate(self.parent.ids['road'].level.map)
        ]
        return ', '.join([e for e in res])

    def update_map_text(self):
        line_map = self.parent.ids['line_map']
        line_map.text = self.map_text()
        return line_map.text

    def __map_text_old(self):
        road = self.parent.ids['road']
        return """[size=9]
        [i]# todo: create < slider to map >[/i] 
        >>> {dt:10.2f} ---> {tw}
        [color={color}]{name}[/color]
        {pos}[/size]""".format(
            dt=road.distance_traveled,
            tw=road.total_way,
            name='      |     '.join([e['name'].lower() for e in road.level.map]),
            pos='   |   '.join([str(e['pos']) for e in road.level.map]),
            color=Color.RED
        )
