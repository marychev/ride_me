from kivy.lang import Builder
from kivy.uix.carousel import Carousel
from bike.bikes import BIKES
from screen.ui.slide import Slide
from utils.dir import abstract_path

Builder.load_file(abstract_path('screen/ui/menu_carousel.kv'))


class MenuCarousel(Carousel):
    def __init__(self, **kwargs):
        super(MenuCarousel, self).__init__(**kwargs)
        slides = [Slide(item=o) for o in BIKES]
        [self.add_widget(slide) for slide in slides]

    def on_touch_up(self, touch):
        super(MenuCarousel, self).on_touch_up(touch)
        title = self.parent.parent.children[1]
        title.text = self.current_slide.item['title']
