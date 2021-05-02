import time
from typing import Tuple, Optional, Type
from kivy.cache import Cache
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.logger import Logger
from kivy.uix.floatlayout import FloatLayout

from objects.base.game_image import GameImage
from objects.config import Register
from utils.dir import abstract_path
from utils.get_object import GetObject
from utils.type import TJsonMapItem

Builder.load_file(abstract_path('layout/scene.kv'))


CACHE_NAME = 'installed'
Cache.register(CACHE_NAME, limit=10000)


class Scene(FloatLayout):
    def __init__(self, **kwargs):
        super(Scene, self).__init__(**kwargs)
        Clock.schedule_interval(self.start_timer, 1)

    @staticmethod
    def get_cache(sid: str):
        return Cache.get(CACHE_NAME, sid)

    def add_to_road(self, map_elem: TJsonMapItem, goclass: Type[GameImage], size: Tuple):
        road = self.parent.ids['road']
        sid = goclass.init_sid(map_elem['pos'])

        if map_elem['name'] == goclass.__name__ and not Scene.get_cache(sid) \
                and road.distance_traveled+size[0] < map_elem['pos'][0]:

            x = Window.width if road.distance_traveled > 0 else map_elem['pos'][0]
            y = map_elem['pos'][1] if int(map_elem['pos'][1]) > 0 else road.line_points[-1]

            widget = goclass.create(sid, (x, y), size)
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

            # self.devtools_activate()

    # Curtain's start timer as game object
    def start_timer(self, dt) -> Optional[bool]:
        curtain = self.parent.ids['curtain']
        if curtain:
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
        except KeyError as e:
            Logger.warning('DevTools was not initial. {}'.format(e))

    def _add_visible_map_elems(self):
        road = self.parent.ids['road']
        if len(road.children) >= 0:
            map_elems = road.level.visible_map_elem()

            for me in map_elems:
                if road.visible(me['pos']):
                    if me['name'] == Register.Start.name:
                        _cls = Register.get_class(Register.Start.name)
                        self.add_to_road(me, _cls, (80, 70))

                    elif me['name'] == Register.Finish.name:
                        _cls = Register.get_class(Register.Finish.name)
                        self.add_to_road(me, _cls, (80, 70))

                    elif me['name'] == Register.Lamp.name:
                        _cls = Register.get_class(Register.Lamp.name)
                        self.add_to_road(me, _cls, _cls.img.texture_size)

                    elif me['name'] == Register.Puddle.name:
                        _cls = Register.get_class(Register.Puddle.name)
                        self.add_to_road(me, _cls, _cls.img.texture_size)

                    elif me['name'] == Register.Rock.name:
                        _cls = Register.get_class(Register.Rock.name)
                        self.add_to_road(me, _cls, _cls.img.texture_size)

                    elif me['name'] == Register.Currency.name:
                        _cls = Register.get_class(Register.Currency.name)
                        self.add_to_road(me, _cls, (60, 60))

    def _update_children_x(self):
        road = self.parent.ids['road']
        for ro in road.children[:]:
            if ro.__class__.__name__ in Register.as_list() and Scene.get_cache(ro.sid) and ro.pos[0]+ro.width > 0:
                ro.set_x()
