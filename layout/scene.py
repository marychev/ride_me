from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from utils.dir import abstract_path

Builder.load_file(abstract_path('layout/scene.kv'))


from objects.start import Start


class Scene(FloatLayout):
    def add_to_map(self):
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!111')
        road = self.parent.ids['road']
        map_elems = road.level.visible_map_elem()
        road_elems = road.children[:]

        print(road_elems)

        # Start Element
        has_start = [ro for ro in road_elems if ro.__class__.__name__ == Start.__name__]
        if len(has_start) == 0:
            # create map elems
            for me in map_elems:
                print('----------------------------------', me['name'], Start.__name__)
                if me['name'] == Start.__name__:
                    # + текущая позиция позволяет поставить елем
                    start = Start.create(me['pos'], (60, 60))
                    start.set_x()
                    road.add_widget(start)
                    break

        for ro in road_elems:
            if ro.__class__.__name__ == Start.__name__:
                print('*******', ro)
                ro.set_x()

    def update_map_text(self):
        devtools = self.parent.ids['devtools']
        line_map = devtools.ids['line_map']
        line_map.text = devtools.map_text()
        return line_map.text
