class Color:
    RED = 'ff0000'
    RED_LIGHT = 'fb2929'
    ORANGE = 'ff5e00'
    ORANGE_LIGHT = 'ffa500'
    YELLOW = 'ffff00'
    YELLOW_LIGHT = 'ddff23'
    YELLOW_GREEN = 'b0f12e'
    GREEN = '0ac10a'
    GREEN_LIGHT = '20e813'
    GREEN_R = '489c56'
    PURPLE = 'b15fc5'


def switcher_color(min_value, max_value):
    color = Color.RED
    if min_value <= max_value / 10:
        color = Color.RED_LIGHT
    elif min_value <= max_value / 8:
        color = Color.ORANGE
    elif min_value <= max_value / 6:
        color = Color.ORANGE_LIGHT
    elif min_value <= max_value / 4:
        color = Color.YELLOW_LIGHT
    elif min_value <= max_value / 2.5:
        color = Color.YELLOW_GREEN
    elif min_value <= max_value / 1.2:
        color = Color.GREEN_LIGHT
    elif min_value <= max_value / 0.5:
        color = Color.GREEN

    return color
