from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from utils.dir import abstract_path

Builder.load_file(abstract_path('layout/scene.kv'))


class Scene(FloatLayout):

    def map_text(self):
        road = self.parent.ids['road']
        return """[size=9]
        [i]# todo: create < slider to map >[/i] 
        DT: {}
        [color=ff3333]{}[/color]
        {}[/size]""".format(
            road.distance_traveled,
            '      |     '.join([e['name'].lower() for e in road.level.map]),
            '   |   '.join([str(e['pos']) for e in road.level.map])
        )

    def update_map_text(self):
        line_map = self.parent.ids['line_map']
        line_map.text = self.map_text()
        return line_map.text
