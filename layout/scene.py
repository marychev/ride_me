from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.cache import Cache
from objects import Start, Finish, Lamp, Puddle, Rock
from utils.dir import abstract_path
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle

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

        if map_elem['name'] == gowid.__name__ and not Scene.get_cache(sid) and road.distance_traveled+size[0] < map_elem['pos'][0]:
            # print('.. .. add to road', map_elem, str(gowid), map_elem['pos'], road.distance_traveled, road.visible(map_elem['pos']))
            x = Window.width if road.distance_traveled > 0 else map_elem['pos'][0]
            y = map_elem['pos'][1] if map_elem['pos'][1] > 0 else road.line_points[-1]
            widget = gowid.create(sid, (x, y), size)
            widget.set_x()
            road.add_widget(widget)
            Cache.append(CACHE_NAME, widget.sid, widget)

    def define_and_add_map_elements(self):
        if hasattr(self.parent, 'ids'):
            road = self.parent.ids['road']
            road_elems = road.children[:]
            list_classes = [Start.__name__, Lamp.__name__, Puddle.__name__, Rock.__name__, Finish.__name__]

            if len(road_elems) >= 0:
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

            # set x for exist elements at road
            for ro in road.children[:]:
                if ro.__class__.__name__ in list_classes and Scene.get_cache(ro.sid) and ro.pos[0]+ro.width > 0:
                    ro.set_x()

            road.level.remove_widgets(road_elems)

            # ACTIVATE DEVTOOLS
            try:
                devtools = self.parent.ids['devtools']
                devtools.update_context()
            except KeyError:
                pass

    def start_timer(self, dt):
        start_timer = self.parent.ids['start_timer']

        if start_timer.text == '3':
            self.start_timer_draw_background()
        elif start_timer.text == '2':
            self.start_timer_draw_background(0.5)
        elif start_timer.text == '1':
            self.start_timer_draw_background(0.4)

            start_timer.text = ''
            self.remove_widget(start_timer)
            return False

        start_timer.stop -= 1
        start_timer.text = str(start_timer.stop)

    def start_timer_draw_background(self, transparent=0.6):
        start_timer = self.parent.ids['start_timer']
        start_timer.canvas.before.clear()
        with start_timer.canvas.before:
            Color(0, 0, 0, transparent)
            Rectangle(pos=(0, 0), size=(Window.width, Window.height))

    def do_start_timer(self):
        self.parent.ids['start_timer'].stop = 3
        self.parent.ids['start_timer'].text = str(self.parent.ids['start_timer'].stop)
        self.start_timer_draw_background(0.7)
        return self.parent.ids['start_timer'].text
