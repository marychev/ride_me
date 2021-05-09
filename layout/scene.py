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
from utils.store import CACHE_NAME, Store

Builder.load_file(abstract_path('layout/scene.kv'))


Cache.register(CACHE_NAME, limit=10000)


class Scene(FloatLayout):
    def __init__(self, **kwargs):
        super(Scene, self).__init__(**kwargs)
        Clock.schedule_interval(self.start_timer, 1)

    def add_to_road(self, map_elem: TJsonMapItem, goclass: Type[GameImage], size: Tuple) -> None:
        road = self.parent.ids['road']
        sid = goclass.init_sid(map_elem['pos'])

        store = Store()
        installed = store.get_installed_cache(sid)

        if map_elem['name'] == goclass.__name__ and not installed \
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
        if self.parent.ids['curtain']:
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
        except KeyError as e:
            Logger.warning('DevTools was not initial. {}'.format(e))

    def _add_visible_map_elems(self):
        road = self.parent.ids['road']
        if len(road.children) >= 0:
            map_elems = road.level.visible_map_elem()

            for me in map_elems:
                if road.visible(me['pos']):
                    if me['name'] == Register.Start.name:
                        self.add_to_road_custom_size(me, Register.Start, (80, 70))
                    elif me['name'] == Register.Finish.name:
                        self.add_to_road_custom_size(me, Register.Finish, (80, 70))
                    elif me['name'] == Register.Lamp.name:
                        self.add_to_road_texture_size(me, Register.Lamp)
                    elif me['name'] == Register.Puddle.name:
                        self.add_to_road_texture_size(me, Register.Puddle)
                    elif me['name'] == Register.Rock.name:
                        self.add_to_road_texture_size(me, Register.Rock)
                    elif me['name'] == Register.Currency.name:
                        self.add_to_road_custom_size(me, Register.Currency, (60, 60))

    def add_to_road_custom_size(self, map_elem: TJsonMapItem, register_value: Register, size: Tuple[int, int]) -> None:
        self.add_to_road(map_elem, Register.get_class(register_value.name), size)

    def add_to_road_texture_size(self, map_elem: TJsonMapItem, register_value: Register) -> None:
        cls = Register.get_class(register_value.name)
        self.add_to_road(map_elem, cls, cls.img.texture_size)

    def _update_children_x(self):
        road = self.parent.ids['road']
        store = Store()

        for ro in road.children[:]:
            installed = store.get_installed_cache(ro.sid)
            if ro.__class__.__name__ in Register.as_list() and installed and ro.pos[0]+ro.width > 0:
                ro.set_x()
