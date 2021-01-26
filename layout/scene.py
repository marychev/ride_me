from kivy.cache import Cache
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from objects.start import Start
from objects.lamp.lamp import Lamp
from objects.puddle.puddle import Puddle
from objects.rock.rock import Rock
from objects.finish.finish import Finish
from utils.dir import abstract_path
from kivy.lang import Builder
Builder.load_file(abstract_path('layout/scene.kv'))


CACHE_NAME = 'installed'
Cache.register(CACHE_NAME, limit=1000)
# Cache.remove(CACHE_NAME)


class Scene(FloatLayout):
    @staticmethod
    def get_cache(sid):
        return Cache.get(CACHE_NAME, sid)

    def add_to_road(self, map_elem, gowid, size):
        road = self.parent.ids['road']
        sid = gowid.init_sid(map_elem['pos'])

        if map_elem['name'] == gowid.__name__ and not Scene.get_cache(sid):
            # road.clear_widgets()
            # print('.. .. add to road', map_elem, str(gowid))
            _mpos = map_elem['pos']
            if road.distance_traveled > 0:
                x = Window.width
                y = road.line_points[-1] if map_elem['pos'][1] == 0 else 0
                _mpos = (x, y)

            widget = gowid.create(sid, _mpos, size)
            widget.set_x()
            road.add_widget(widget)
            Cache.append(CACHE_NAME, widget.sid, widget)

    def define_and_add_map_elements(self):
        road = self.parent.ids['road']
        road_elems = road.children[:]

        if len(road_elems) >= 0:
            all_exist = []
            all_exist.extend([ro for ro in road_elems if ro.__class__.__name__ == Start.__name__])
            all_exist.extend([ro for ro in road_elems if ro.__class__.__name__ == Lamp.__name__])
            all_exist.extend([ro for ro in road_elems if ro.__class__.__name__ == Puddle.__name__])
            all_exist.extend([ro for ro in road_elems if ro.__class__.__name__ == Rock.__name__])

            # print('ADD MAP ELEMENTS ONTO ROAD')

            map_elems = road.level.visible_map_elem()
            for me in map_elems:
                if road.visible(me['pos']):
                    if me['name'] in [Start.__name__, Finish.__name__]:
                        self.add_to_road(me, Start, (80, 60))
                        self.add_to_road(me, Finish, (80, 60))
                    elif me['name'] == Lamp.__name__:
                        self.add_to_road(me, Lamp, Lamp.img.texture_size)
                    elif me['name'] == Puddle.__name__:
                        self.add_to_road(me, Puddle, Puddle.img.texture_size)
                    elif me['name'] == Rock.__name__:
                        self.add_to_road(me, Rock, Rock.img.texture_size)

        # set new elements to road
        list_classes = [Start.__name__, Lamp.__name__, Puddle.__name__, Rock.__name__, Finish.__name__]
        for ro in road.children[:]:
            if ro.__class__.__name__ in list_classes and Scene.get_cache(ro.sid) and ro.pos[0]+ro.width > 0:
                ro.set_x()

        # clear old game objects
        road.level.remove_widgets(road_elems)

        # # ACTIVATE DEVTOOLS
        # devtools = self.parent.ids['devtools']
        # devtools.update_context()
