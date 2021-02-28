from kivy.lang import Builder
from kivy.uix.carousel import Carousel
from kivy.properties import ListProperty
from bike.bikes import BIKES, get_by_title as get_bike_by_title
from level.maps import MAPS, get_by_title as get_map_by_title
from screen.ui.slide import Slide
from screen.ui.bottom_button import RightPanelBtn
from utils.dir import abstract_path
from utils.validation import ValidObject
from utils.init import app_config
from utils.color import Color as UColor

Builder.load_file(abstract_path('screen/ui/menu_carousel.kv'))


class MenuCarousel(Carousel):
    objects = ListProperty()

    def __init__(self, **kwargs):
        super(MenuCarousel, self).__init__(**kwargs)
        slides = [Slide(item=o) for o in self.objects]
        [self.add_widget(slide) for slide in slides]
        self.set_title(self.objects[0]['title'])

    def _screen(self):
        return self.parent.parent.parent.parent

    def on_index(self, *args, **kwargs):
        super(MenuCarousel, self).on_index(*args)
        self.set_title(self.current_slide.item['title'])


class BikeMenuCarousel(MenuCarousel):
    objects = ListProperty(BIKES)

    def set_title(self, value):
        if self.parent:
            screen = ValidObject.bikes_screen(self._screen())
            screen.ids['title'].text = value


class MapMenuCarousel(MenuCarousel):
    objects = ListProperty(MAPS)

    def on_index(self, *args, **kwargs):
        super(MapMenuCarousel, self).on_index(*args, **kwargs)
        maps_screen = ValidObject.maps_screen(self._screen())

        if app_config('map', 'title') == self.current_slide.item['title']:
            color = UColor.hex(UColor.WHITE)
        else:
            color = UColor.hex(UColor.GRAY)

        _map = get_map_by_title(self.current_slide.item['title'])
        maps_screen.ids['title'].color = color

        RightPanelBtn.change_color_labels_right_panel(maps_screen.ids['character_wrap_record'], color)
        maps_screen.ids['character_wrap_record'].title = RightPanelBtn.format_title_right_panel(
            maps_screen.ids['character_wrap_record'], 'dev')
        RightPanelBtn.change_color_labels_right_panel(maps_screen.ids['character_wrap_level'], color)
        maps_screen.ids['character_wrap_level'].title = RightPanelBtn.format_title_right_panel(
            maps_screen.ids['character_wrap_level'], _map['level'])
        RightPanelBtn.change_color_labels_right_panel(maps_screen.ids['character_wrap_map'], color)
        maps_screen.ids['character_wrap_map'].title = RightPanelBtn.format_title_right_panel(
            maps_screen.ids['character_wrap_map'], _map['map'])
        RightPanelBtn.change_color_labels_right_panel(maps_screen.ids['character_wrap_total_way'], color)
        maps_screen.ids['character_wrap_total_way'].title = RightPanelBtn.format_title_right_panel(
            maps_screen.ids['character_wrap_total_way'], _map['total_way'])


    def set_title(self, value):
        if self.parent:
            screen = ValidObject.maps_screen(self._screen())
            if screen.ids['title']:
                if screen.ids:
                    screen.ids['title'].text = value
