from kivy.lang import Builder
from kivy.cache import Cache
from kivy.uix.floatlayout import FloatLayout
from utils.dir import abstract_path
from kivy.core.window import Window
from kivy.uix.image import Image
Builder.load_file(abstract_path('layout/scene.kv'))

from objects.start import Start
from objects.lamp.lamp import Lamp
from objects.puddle.puddle import Puddle


CACHE_NAME = 'installed'
Cache.register(CACHE_NAME, limit=10)

Cache.remove(CACHE_NAME)


class Scene(FloatLayout):

    def add_to_road(self, map_elem, gowid, size):
        road = self.parent.ids['road']
        sid = gowid.init_sid(map_elem['pos'])
        if map_elem['name'] == gowid.__name__ and not Cache.get(CACHE_NAME, sid):
            # road.clear_widgets()
            print('.. add to road', map_elem, gowid)

            _mpos = map_elem['pos']
            if road.distance_traveled > 0:
                _mpos = (Window.width, map_elem['pos'][1])

            widget = gowid.create(_mpos, size)
            widget.set_x()
            road.add_widget(widget)
            Cache.append(CACHE_NAME, widget.sid, widget)

    def add_to_map(self):
        print('ADD TO MAP ELEMENTS')
        road = self.parent.ids['road']
        map_elems = road.level.visible_map_elem()
        road_elems = road.children[:]

        # Start Element
        all_exist = []
        all_exist.extend([ro for ro in road_elems if ro.__class__.__name__ == Start.__name__])
        all_exist.extend([ro for ro in road_elems if ro.__class__.__name__ == Lamp.__name__])
        all_exist.extend([ro for ro in road_elems if ro.__class__.__name__ == Puddle.__name__])

        if len(all_exist) >= 0 and len(road_elems) <= len(map_elems):
            for me in map_elems:
                self.add_to_road(me, Start, (80, 60))
                self.add_to_road(me, Lamp, Lamp.img.texture_size)
                self.add_to_road(me, Puddle, Puddle.img.texture_size)

        # set new elements to road
        for ro in road.children[:]:
            if ro.__class__.__name__ in [Start.__name__, Lamp.__name__, Puddle.__name__] \
                    and Cache.get(CACHE_NAME, ro.sid) and ro.pos[0]+ro.width > 0:

                ro.set_x()

        self.update_devtools_text()

    def update_devtools_text(self):
        road = self.parent.ids['road']
        devtools = self.parent.ids['devtools']
        line_map = devtools.ids['line_map']
        line_map.text = devtools.map_text()

        btn_add = devtools.ids['btn_add_to_map']
        btn_add.text = f'Add to Map: {len(road.level.visible_map_elem())}'

        slider_map = devtools.ids['slider_map']
        slider_map.value = road.distance_traveled
        slider_map_label = devtools.ids['slider_map_label']
        slider_map_label.text = f'{int(slider_map.value)} => {int(road.total_way)}'
