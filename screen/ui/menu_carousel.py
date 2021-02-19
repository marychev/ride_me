from kivy.lang import Builder
from kivy.uix.carousel import Carousel
from kivy.properties import ListProperty
from bike.bikes import BIKES
from level.maps import MAPS
from screen.ui.slide import Slide
from utils.dir import abstract_path
from utils.validation import ValidObject

Builder.load_file(abstract_path('screen/ui/menu_carousel.kv'))


class MenuCarousel(Carousel):
    objects = ListProperty()

    def __init__(self, **kwargs):
        super(MenuCarousel, self).__init__(**kwargs)
        slides = [Slide(item=o) for o in self.objects]
        [self.add_widget(slide) for slide in slides]
        self.set_title(self.objects[0]['title'])

    def on_index(self, *args, **kwargs):
        super(MenuCarousel, self).on_index(*args)
        self.set_title(self.current_slide.item['title'])


class BikeMenuCarousel(MenuCarousel):
    objects = ListProperty(BIKES)

    def set_title(self, value):
        if self.parent:
            screen = ValidObject.bikes_screen(self.parent.parent.parent.parent)
            screen.ids['title'].text = value


class MapMenuCarousel(MenuCarousel):
    objects = ListProperty(MAPS)

    def set_title(self, value):
        if self.parent:
            screen = ValidObject.maps_screen(self.parent.parent.parent.parent)
            if screen.ids['title']:
                if screen.ids:
                    screen.ids['title'].text = value
