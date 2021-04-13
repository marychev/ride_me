from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.metrics import cm


class SlideLabel(Label):
    def __init__(self, **kwargs):
        super(SlideLabel, self).__init__(**kwargs)
        self.markup = True
        self.text_size = cm(12), cm(6)
        self.size = self.text_size
        self.size_hint = None, None
        self.pos = self.center_x, self.center_y - 80


class Slide(Image):
    def __init__(self, item, **kwargs):
        super(Slide, self).__init__(**kwargs)
        self.item = item
        # self.allow_stretch = True
        self.source = item['source']
        self.add_widget(SlideLabel(text=item['text']))


