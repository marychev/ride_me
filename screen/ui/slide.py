from kivy.core.window import Window
from kivy.uix.image import AsyncImage
from kivy.uix.label import Label
from kivy.metrics import cm


class SlideLabel(Label):
    def __init__(self, **kwargs):
        super(SlideLabel, self).__init__(**kwargs)
        self.markup = True
        self.text_size = cm(12), cm(6)
        self.size = self.texture_size
        self.pos = self.pos[0], int(Window.height/8)


class Slide(AsyncImage):
    def __init__(self, item, **kwargs):
        super(Slide, self).__init__(**kwargs)
        self.item = item
        self.source = item['source']
        self.add_widget(SlideLabel(text=item['text']))


