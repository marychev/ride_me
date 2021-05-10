from typing import Union
from kivy.cache import Cache


def app_config(section, key):
    value = Cache.get(section, key)
    return value if value != 'None' else None


def get_item_by_title_or_index(array: list, value: Union[str, int, None]):
    if value is None:
        return
    elif type(value) is int:
        return array[value]
    for a in array:
        if a['title'] == value:
            return a


def calc_rest_rm(price):
    return int(app_config('bike', 'rm')) - int(price)
