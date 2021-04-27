from kivy.core.window import Window
from utils.sizes import FontSize as FS, GOSize as GOS
from kivy.uix.image import Image
from kivy.uix.label import Label


class SlideLabel(Label):
    def __init__(self, **kwargs):
        super(SlideLabel, self).__init__(**kwargs)
        self.markup = True
        self.font_size = FS.SMALL.value
        self.text_size = Window.width/2, Window.height/2
        self.size = self.text_size

        self.size_hint = None, None
        self.pos = self.center_x, self.center_y/2


class Slide(Image):
    def __init__(self, item, **kwargs):
        super(Slide, self).__init__(**kwargs)
        # self.allow_stretch = True
        # self.pos_hint = {'x': 0, 'y': 0.1}
        self.item = item
        self.size_hint = None, None
        self.size = GOS.WIDTH_Slide.value, GOS.HEIGHT_Slide.value
        self.source = item['source']

        self.add_widget(SlideLabel(text=item['text']))


