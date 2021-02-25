from kivy.app import App


def app_config(section, key):
    app = App.get_running_app()
    return app and app.config.get(section, key)


def get_item_by_title_or_index(array, value):
    if type(value) is int: return array[value]
    for a in array:
        if a['title'] == value:
            return a


def calc_rest_rm(price):
    return int(app_config('bike', 'rm')) - int(price)
