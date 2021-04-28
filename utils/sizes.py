from kivy.core.window import Window
from enum import Enum
from kivy.metrics import sp, dp
from utils.type import TIntFloatStr

# [note]: kivy doc size % getting debug size, w / h
# _k: about 0.15
# 1.91, 1.38, 1.93, 1.91
# 1,77 ,1.33, 1,78, 1,77
WH = float("{0:.2f}".format(Window.width / Window.height))


def switch_size(v11: TIntFloatStr, v18: TIntFloatStr, small: TIntFloatStr) -> TIntFloatStr:
    def _k(v): return 0.15 + v

    small_height = 600
    step_tablet = (_k(1), _k(1.33))
    has_step_tablet = step_tablet[0] <= WH < step_tablet[1] and Window.height > small_height

    step_normal = (_k(1.33), _k(1.9))
    has_step_normal = step_normal[0] <= WH < step_normal[1] and Window.height > small_height

    has_step_small = Window.height <= small_height

    if has_step_tablet:
        return v11
    elif has_step_normal:
        return v18
    elif has_step_small:
        return small


class FontSize(Enum):
    XSMALL = sp(6+WH)
    SMALL = sp(8+WH)
    NORMAL = sp(10+WH)
    LEAD = sp(15+WH)
    H1 = sp(27+WH)


BASE_WIDTH_BTN = Window.width / 8


class GOSize(Enum):
    WH_PanelBtn = switch_size(v11=BASE_WIDTH_BTN, v18=BASE_WIDTH_BTN, small=BASE_WIDTH_BTN)
    WH_BUTTON_LR = switch_size(v11=BASE_WIDTH_BTN, v18=BASE_WIDTH_BTN, small=BASE_WIDTH_BTN)
    WIDTH_MenuButton = switch_size(v11=(Window.width / 4), v18=(Window.width / 5), small=(Window.width / 5))
    HEIGHT_MenuButton = switch_size(v11=(Window.height / 10), v18=(Window.height/7), small=(Window.height / 7))
    WIDTH_CharacterWrap = switch_size(v11=(Window.width / 5), v18=(Window.width/4), small=(Window.width / 4))
    WIDTH_Slide = switch_size(v11=Window.width, v18=Window.width, small=Window.width)
    HEIGHT_Slide = switch_size(v11=Window.height, v18=Window.height, small=Window.height)
    # HEIGHT_CharacterWrap = dp(40)
    HEIGHT_CharacterWrap = switch_size(v11=Window.height / (4*WH*2), v18=Window.height / (4*WH), small=(Window.height / (4*WH)))


# class SizePhones:
#     redmi_note_8_h = 1080
#     redmi_note_8_w = 2340
#     redmi_note_8 = (redmi_note_8_h, redmi_note_8_w)
#     onex = (1280, 720)                        del: 1.77
#     droid2 = (854, 480)                       del: 1.76
#     phone_samsung_galaxy_s5 = (1920, 1080)    del" 1.77
#     default = redmi_note_8
#
#     def __init__(self, phone_size: tuple = None) -> None:
#         self.current = phone_size or self.default
#
#     @property
#     def height(self) -> int:
#         return self.current[0]
#
#     @property
#     def width(self) -> int:
#         return self.current[1]
