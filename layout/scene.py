import time
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.cache import Cache
from objects import Start, Finish, Lamp, Puddle, Rock, Currency
from utils.dir import abstract_path
from kivy.clock import Clock
from utils.get_object import GetObject

Builder.load_file(abstract_path('layout/scene.kv'))


CACHE_NAME = 'installed'
Cache.register(CACHE_NAME, limit=10000)


class Scene(FloatLayout):
    def __init__(self, **kwargs):
        super(Scene, self).__init__(**kwargs)
        Clock.schedule_interval(self.start_timer, 1)

    @staticmethod
    def get_cache(sid):
        return Cache.get(CACHE_NAME, sid)

    def add_to_road(self, map_elem, gowid, size):
        road = self.parent.ids['road']
        sid = gowid.init_sid(map_elem['pos'])

        if map_elem['name'] == gowid.__name__ and not Scene.get_cache(sid) \
                and road.distance_traveled+size[0] < map_elem['pos'][0]:
            x = Window.width if road.distance_traveled > 0 else map_elem['pos'][0]
            y = map_elem['pos'][1] if map_elem['pos'][1] > 0 else road.line_points[-1]
            widget = gowid.create(sid, (x, y), size)
            widget.set_x()
            road.add_widget(widget)
            Cache.append(CACHE_NAME, widget.sid, widget)

    def define_and_add_map_elements(self):
        if hasattr(self.parent, 'ids'):
            road = self.parent.ids['road']
            old_children = road.children[:]
            road.level.remove_widgets(old_children)

            self._add_visible_map_elems()
            self._update_children_x()

            self.devtools_activate()

    # Curtain's start timer as game object
    def start_timer(self, dt):
        curtain = self.parent.ids['curtain']
        if curtain.text == '3':
            curtain.draw_background()
        elif curtain.text == '2':
            curtain.draw_background(0.5)
        elif curtain.text == '1':
            curtain.draw_background(0.4)
            curtain.text = ''
            self.remove_widget(curtain)

            bike = GetObject(self.parent.ids['road']).bike
            bike.start_dt = time.time()
            return False

        curtain.stop -= 1
        curtain.text = str(curtain.stop)

    def devtools_activate(self):
        try:
            devtools = self.parent.ids['devtools']
            devtools.update_context()
        except KeyError:
            pass

    def _add_visible_map_elems(self):
        road = self.parent.ids['road']
        if len(road.children) >= 0:
            map_elems = road.level.visible_map_elem()
            for me in map_elems:
                if road.visible(me['pos']):
                    if me['name'] in [Start.__name__, Finish.__name__]:
                        self.add_to_road(me, Start, (80, 70))
                        self.add_to_road(me, Finish, (80, 70))
                    elif me['name'] == Lamp.__name__:
                        self.add_to_road(me, Lamp, Lamp.img.texture_size)
                    elif me['name'] == Puddle.__name__:
                        self.add_to_road(me, Puddle, Puddle.img.texture_size)
                    elif me['name'] == Rock.__name__:
                        self.add_to_road(me, Rock, Rock.img.texture_size)
                    elif me['name'] == Currency.__name__:
                        self.add_to_road(me, Currency, (60, 60))

    def _update_children_x(self):
        road = self.parent.ids['road']
        list_classes = [
            Start.__name__, Finish.__name__, Currency.__name__, Lamp.__name__, Puddle.__name__, Rock.__name__]

        for ro in road.children[:]:
            if ro.__class__.__name__ in list_classes and Scene.get_cache(ro.sid) and ro.pos[0]+ro.width > 0:
                ro.set_x()
