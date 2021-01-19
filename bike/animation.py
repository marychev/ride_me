from kivy.animation import Animation
from utils.dir import abstract_path


class AnimationBike:
    def anim_go(self):
        self.source = abstract_path('bike/img/bike-go.png')
        anim = Animation(angle=8, duration=.2)
        anim.start(self)

    def anim_relax(self):
        self.source = abstract_path('bike/img/bike-relax.png')
        anim = Animation(angle=0, duration=.2)
        anim.start(self)

    def anim_wait(self):
        self.source = abstract_path('bike/img/bike-wait.png')
        anim = Animation(angle=0, duration=.2)
        anim.start(self)

    def anim_stop(self):
        self.source = abstract_path('bike/img/bike-stop.png')
        anim = Animation(angle=-1, duration=.1)
        anim.start(self)

    def anim_jump_up(self):
        self.source = abstract_path('bike/img/bike-jump-up.png')
        anim = Animation(angle=8, duration=.2)
        anim.start(self)

    def anim_landing(self):
        self.source = abstract_path('bike/img/bike-landing.png')
        anim = Animation(angle=-8, duration=.2)
        anim.start(self)

    def anim_collision(self):
        self.source = abstract_path('bike/img/bike-1.png')
        anim = Animation(angle=180, duration=.2)
        anim.start(self)
