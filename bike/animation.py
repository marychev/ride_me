from kivy.animation import Animation
from utils.dir import abstract_path
from kivy.properties import NumericProperty, StringProperty


class AnimationBike:
    def init_source_animation(self, item):
        self.source_go = item['source_go']
        self.source_relax = item['source_relax']
        self.source_wait = item['source_wait']
        self.source_stop = item['source_stop']
        self.source_jump_up = item['source_jump_up']
        self.source_landing = item['source_landing']
        self.source_collision = item['source_collision']

    def anim_go(self):
        # self.source = abstract_path('bike/img/bike-go.png')
        self.source = self.source_go
        anim = Animation(angle=8, duration=.2)
        anim.start(self)

    def anim_relax(self):
        # self.source = abstract_path('bike/img/bike-relax.png')
        self.source = self.source_relax
        anim = Animation(angle=0, duration=.2)
        anim.start(self)

    def anim_wait(self):
        # self.source = abstract_path('bike/img/bike-wait.png')
        self.source = self.source_wait
        anim = Animation(angle=0, duration=.2)
        anim.start(self)

    def anim_stop(self):
        # self.source = abstract_path('bike/img/bike-stop.png')
        self.source = self.source_stop
        anim = Animation(angle=-1, duration=.1)
        anim.start(self)

    def anim_jump_up(self):
        # self.source = abstract_path('bike/img/bike-jump-up.png')
        self.source = self.source_jump_up
        anim = Animation(angle=8, duration=.2)
        anim.start(self)

    def anim_landing(self):
        # self.source = abstract_path('bike/img/bike-landing.png')
        self.source = self.source_landing
        self.source = self.source_landing
        anim = Animation(angle=-8, duration=.2)
        anim.start(self)

    def anim_collision(self):
        # self.source = abstract_path('bike/img/bike-1.png')
        self.source = self.source_collision
        anim = Animation(angle=180, duration=.2)
        anim.start(self)
