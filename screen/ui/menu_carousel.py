from kivy.lang import Builder
from kivy.uix.carousel import Carousel
from bike.bikes import BIKES
from screen.ui.slide import Slide
from utils.dir import abstract_path
from utils.validation import ValidObject

Builder.load_file(abstract_path('screen/ui/menu_carousel.kv'))


class MenuCarousel(Carousel):
    def __init__(self, **kwargs):
        super(MenuCarousel, self).__init__(**kwargs)
        slides = [Slide(item=o) for o in BIKES]
        [self.add_widget(slide) for slide in slides]
        self.set_title(BIKES[0]['title'])

    def on_index(self, *args, **kwargs):
        super(MenuCarousel, self).on_index(*args)
        self.set_title(self.current_slide.item['title'])

    def set_title(self, value):
        if self.parent:
            bikes_screen = ValidObject.bikes_screen(self.parent.parent.parent.parent)
            bikes_screen.ids['title'].text = value
