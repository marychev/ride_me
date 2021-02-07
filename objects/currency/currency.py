from kivy.animation import Animation
from kivy.graphics import Color, Ellipse
from kivy.properties import BooleanProperty
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from objects.base.game_image import GameImage
from utils.color import Color as UC


class Currency(GameImage):
    img = None
    TEXTURE = None
    texture = ObjectProperty(TEXTURE)
    label = ObjectProperty(None)
    collected = BooleanProperty(False)
    units = '[color={}]&bl;[b]r[/color][color={}]m[/b]&br;[/color]'.format(UC.GREEN_R, UC.PURPLE)
    color_label = .1, .1, .1, 1

    def __init__(self, **kwargs):
        super(Currency, self).__init__(**kwargs)
        self.size = 40, 40
        self.set_label()

    def set_label(self):
        if not self.label:
            self.label = Label(text=self.units, size=self.size, pos=self.pos, markup=True)
        self.label_canvas_before()
        self.add_widget(self.label)

    def label_canvas_before(self):
        self.label.canvas.before.clear()
        with self.label.canvas.before:
            Color(*self.color_label)
            Ellipse(size=self.size, pos=self.pos)

    def on_collision(self, bike):
        if bike.collide_widget(self) and not self.collected:
            bike.collected_currency += 1
            self.color_label = 1, .6, 0, 1
            self.collected = True
            anim = Animation(y=self.y + 1000, duration=.2)
            anim.start(self)
            return True
        return False
